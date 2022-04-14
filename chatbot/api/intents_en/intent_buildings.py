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

        for i in buildings:
            tag = buildings[i]['name'] + " code"
            pattern = buildings[i]['name'] + " buildings", "what is the building code for " + buildings[i]['name'], \
                      buildings[i]['name'] + " stand for what code"
            response = 'buildings', i, None, None, 'code'
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

        return write