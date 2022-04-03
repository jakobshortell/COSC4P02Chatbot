from scrapers.restaurant import RestaurantScraper

restaurant = RestaurantScraper().get()

class IntentRestaurant:

    def generate(self, write):
        for i in restaurant:
            tag = restaurant[i]['name'] + " restaurant"
            pattern = restaurant[i]['name'] + " restaurant", "tell me about " + restaurant[i]['name'] + " restaurant", \
                      "can you get information on " + restaurant[i]['name'] + " restaurant"
            response = 'restaurants', i, None, None, None
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

        for i in restaurant:
            tag = restaurant[i]['name'] + " restaurant hours"
            pattern = restaurant[i]['name'] + " restaurant hours", "when is " + restaurant[i]['name'] + " open", \
                      "hours for " + restaurant[i]['name'] + " restaurant", "when does " + restaurant[i]['name'] + \
                      " restaurant close"
            response = 'restaurants', i, None, None, 'hours'
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)


        return write
