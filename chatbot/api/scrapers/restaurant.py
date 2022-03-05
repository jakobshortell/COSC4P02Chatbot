from codecs import ignore_errors
import mechanicalsoup
import sqlite3


class RestaurantScraper:

    def __init__(self):
        self.browser = mechanicalsoup.StatefulBrowser()
        self.db_conn = sqlite3.connect('chatbot.db', check_same_thread=False)
        self.db_conn.row_factory = sqlite3.Row

        with self.db_conn as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS restaurants (
                    name TEXT, 
                    description TEXT,
                    hour TEXT,
                    PRIMARY KEY (name)
                )
                '''
            )
            conn.commit()

    def fetch(self):
        self.browser.open(
            'https://brocku.ca/dining-services/dining-on-campus/locations-on-campus-and-hours-of-operation/')
        restaurants_list = self.browser.page.find_all('div', attrs={
            'class': 'wpb_wrapper'
        })
        # restaurants_list = self.browser.page.find_all('div', attrs={
        # 	'class': 'wpb_text_column'
        # })
        return self.read_restaurants(restaurants_list)

    def get(self):

        restaurants = self.get_restaurants()

        if not restaurants:
            self.fetch()
            return self.get_restaurants()

        return restaurants

    def read_restaurants(self, restaurants_list):
        output = {}

        for index, restaurant in enumerate(restaurants_list):
            try:
                data = restaurant.contents
                if (len(data) == 8):
                    # special case
                    entry = {
                        'name': self.get_name(restaurant, 1),
                        'description': self.get_description(restaurant, 1),
                        'hour': self.get_hour(restaurant, 3)
                    }
                    output[index] = entry

                    entry = {
                        'name': self.get_name(restaurant, 5),
                        'description': self.get_description(restaurant, 5),
                        'hour': self.get_hour(restaurant, 7)
                    }
                    output[index] = entry

                else:
                    entry = {
                        'name': self.get_name(restaurant, -1),
                        'description': self.get_description(restaurant, -1),
                        'hour': self.get_hour(restaurant, -1)
                    }
                    if (entry.get('name') is not None):
                        output[index] = entry

            except:
                ignore_errors

        self.store_restaurants(output)

        return output

    def get_name(self, restaurant, i):
        try:
            # special case
            if (i > 0):
                data = restaurant.contents
                counter = 0
                for d in data:
                    if (d.name == 'div' and counter == i):
                        return d.find('div', attrs={'class': 'wpb_wrapper'}).find('h2').text
                    counter += 1

            else:
                return restaurant.find('div', attrs={'class': 'wpb_wrapper'}).find('h2').text

        except:
            return None

    def get_description(self, restaurant, i):
        try:
            # special case
            if (i > 0):
                paragraphs = ""
                data = restaurant.contents
                counter = 0
                for d in data:
                    if (d.name == 'div' and counter == i):
                        content = d.find('div', attrs={'class': 'wpb_wrapper'}).contents

                        for c in content:
                            try:
                                if (c.name == 'p'):
                                    paragraphs += c.text + '\n'
                            except:
                                ignore_errors
                        return paragraphs

                    counter += 1

            else:
                paragraphs = ""
                content = restaurant.find('div', attrs={'class': 'wpb_wrapper'}).contents
                for c in content:
                    try:
                        if (c.name == 'p'):
                            paragraphs += c.text + '\n'
                    except:
                        ignore_errors
                return paragraphs

        except:
            return "N/A"

        # paragraphs = ""
        # data = restaurant.find('div', attrs={'class': 'wpb_wrapper'}).contents

        # for d in data :
        # 	try :
        # 		if (d.name == 'p') :
        # 			paragraphs += d.text + '\n'
        # 	except:
        # 		ignore_errors

        # return paragraphs

    # except:
    # 	try :
    # 		paragraphs = ""
    # 		ps = restaurant.contents

    # 		for p in ps :
    # 			if (p.name == 'p') :
    # 				paragraphs += p.text + '\n'

    # 		return paragraphs

    def get_hour(self, restaurant, i):

        try:
            # special case
            if (i > 0):
                paragraphs = ""
                data = restaurant.contents
                counter = 0
                for d in data:
                    if (d.name == 'section' and counter == i):
                        content = d.find('div', attrs={'class': 'vc_cta3-content'}).contents

                        for c in content:
                            try:
                                if (c.name == 'p' or c.name == 'h4'):
                                    paragraphs += c.text + '\n'
                            except:
                                ignore_errors

                        return paragraphs

                    counter += 1

            else:
                paragraphs = ""
                content = restaurant.find('div', attrs={'class': 'vc_cta3-content'}).contents
                for c in content:
                    try:
                        if (c.name == 'p' or c.name == 'h4'):
                            paragraphs += c.text + '\n'
                    except:
                        ignore_errors
                return paragraphs

        except AttributeError:
            return "N/A"

    def store_restaurants(self, restaurants):
        with self.db_conn as conn:
            for index in restaurants:
                conn.execute(
                    '''
                    INSERT OR REPLACE INTO restaurants
                    VALUES (?, ?, ?)
                    ''',
                    (
                        restaurants[index]['name'],
                        restaurants[index]['description'],
                        restaurants[index]['hour']
                    )
                )
                conn.commit()

    def get_restaurants(self):
        output = {}

        with self.db_conn as conn:
            rows = conn.execute(
                '''
                SELECT *
                FROM restaurants
                '''
            ).fetchall()

        for index, row in enumerate(rows):
            output[index] = {
                'name': row['name'],
                'description': row['description'],
                'hour': row['hour']
            }

        return output
