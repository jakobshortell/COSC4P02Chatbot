from scrapers.restaurant import RestaurantScraper

restaurant = RestaurantScraper().get()

class IntentRestaurant:

    def generate(self, write):
        for i in restaurant:
            tag = restaurant[i]['name'] + " restaurant"
            pattern = restaurant[i]['name'] + " restaurant", "when is " + restaurant[i]['name'] + " open", \
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

        return write
