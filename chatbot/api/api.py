import random

from flask import Flask, request
from scrapers.clubs import ClubScraper
from scrapers.departments import DepartmentScraper
from scrapers.important_dates import ImportantDatesScraper
from scrapers.courses import CoursesScraper
from scrapers.programs import ProgramScraper
from scrapers.exams import ExamScraper
from scrapers.restaurant import RestaurantScraper
from scrapers.buildings import BuildingScraper
from scrapers.weather import WeatherScraper
from scrapers.course_details import CoursesDetailsScraper
from scrapers.brock_news import newsScraper
from bot import process_message

app = Flask(__name__)

# Instantiate scheduler and pass in instances of scrapers
scrapers = {
    'clubs': ClubScraper(),
    'departments': DepartmentScraper(),
    'dates': ImportantDatesScraper(),
    'courses': CoursesScraper(),
    'programs': ProgramScraper(),
    'exams': ExamScraper(),
    'restaurant': RestaurantScraper(),
    'buildings': BuildingScraper(),
    'weather': WeatherScraper(),
    'course_details': CoursesDetailsScraper(),
    'news': newsScraper()
}


@app.route('/api', methods=['POST', 'GET'])
def main():
    '''The main enpoint for requests made to the chatbot.'''
    request_data = request.get_json()
    user_message = request_data['userMessage'].lower()

    # Default response
    response = {
        'content': 'Error, something went wrong.'
    }
    print(response)
    bot_response = process_message(user_message)
    table_name, index, associated_indexes, messages = bot_response.values()
    # Output an attribute of the first element in the response as a test
    if (table_name is not None ):
        data = scrapers[table_name].get()

    if 'clubs' == table_name:
        response['content'] = data[index]['name'] + ":\n" + data[index]['description'] + "\nEmail: " + data[index]['email']

    elif 'departments' == table_name:
        response['content'] = data[index]['name'] + ":\n" + data[index]['description'] + "\nLink:\t" + data[index][
            'link'] + "\nSocial:\t" + data[index]['social'] + "\nEmail:\t" + data[index]['email'] + "\nPhone:\t" + \
                              data[index]['extension']

    elif 'dates' == table_name:
        response['content'] = data[index]['occasion'] + " " + data[index]['date']

    elif 'weather' == table_name:
        response['content'] = data

    elif 'news' == table_name:
        response['content'] = data

    elif 'course_details' == table_name:
        response['content'] = data[index]['course_code'] + ": " + data[index]['course_name'] + "\n" + data[index]['course_description']

    elif 'buildings' == table_name:
        response['content'] = data[index]['code'] + " code stands for " + data[index]['name'] + "\nClick the link to learn more: " + data[index]['link']

    elif 'restaurants' == table_name:
        response['content'] = data[index]['name'] + " " + data[index]['description'] + " " + data[index]['hour']

    elif 'restaurant_list' == table_name:
        msg_temp = ''
        for index in data:
            msg_temp = msg_temp + "\n" + data[index]['name']
        response['content'] = index + msg_temp + "\nIs there one you would like more information on?"

    elif 'exams' == table_name:
        response['content'] = data[index]['course_code'] + " " + data[index]['duration'] + " " + data[index]['day'] + " " + data[index]['start'] + " " + data[index]['end'] + " " + data[index]['location']

    elif 'programs' == table_name:
        response['content'] = data[index]['name'] + "\n" + data[index]['description'] + "\n" + data[index]['prerequisites']

    elif 'courses' == table_name:
        msg_temp = ''
        for i in range(associated_indexes):
            x = index - i
            msg_temp = msg_temp + "\n" + data[x]['duration'] + " " + data[x]['day'] + " " + data[x]['time'] + " " + data[x]['type'] + " " + data[x]['instructor']
        response['content'] = data[index]['course_code'] + " " + data[index]['title'] + msg_temp

    else:
        response['content'] = random.choice(messages)

    return response


if __name__ == '__main__':
    app.run(debug=True)