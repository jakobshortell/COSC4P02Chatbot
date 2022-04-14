from scrapers.transportation import TransportationScraper

transportation = TransportationScraper().get()

class IntentTransportation:

    def generate(self, write):
        for i in transportation:
            tag = transportation[i]['name'] + " departments"
            pattern = transportation[i]['name'] + " transit ", "can you tell me about the " + transportation[i][
                'name'] + " transit ", "can you get information on the " + transportation[i]['name'] + " transit"
            response = 'transportation', i, None, None, None
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

        return write