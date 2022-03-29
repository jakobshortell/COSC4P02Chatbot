from scrapers.buildings import BuildingScraper

buildings = BuildingScraper().get()

class IntentBuilding:

    def generate(self, write):
        for i in buildings:
            tag = buildings[i]['code'] + " building"
            pattern = buildings[i]['code'] + " buildings", "what building is " + buildings[i]['code'], "what does " + \
                      buildings[i]['code'] + " stand for"
            response = 'buildings', i, None, None, None
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

        return write