from scrapers.contact import ContactScraper

contacts = ContactScraper().get()

class IntentContact:

    def generate(self, write):
        for i in contacts:
            tag = contacts[i]['name'] + " contact"
            pattern = contacts[i]['name'] + " phone number", "what is " + contacts[i][
                'name'] + " phone number ", "how can i contact " + contacts[i]['name'], contacts[i]['name'] + " email", \
                      "what is " + contacts[i]['name'] + " email ", "where is " + contacts[i]['name'] + " office "
            response = 'contacts', i, None, None, None
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

        return write