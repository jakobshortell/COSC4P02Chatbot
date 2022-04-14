import json
from scrapers.clubs import ClubScraper

clubs = ClubScraper().get()


class IntentClub:

    def generate(self, write):

        for i in clubs:
            tag = clubs[i]['name'] + " clubs"
            pattern = clubs[i]['name'] + " club", "can you tell me about the " + clubs[i]['name'] + " club", \
                      "can you get information on the " + clubs[i]['name'] + " club", "What is the " + clubs[i]['name'] \
                      + " club about"
            response = 'clubs', i, None, None, None
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

        for i in clubs:
            tag = clubs[i]['name'] + " club contact"
            pattern = clubs[i]['name'] + " club email", "Can you give me the contact email for the " + clubs[i]['name'] \
                      + " club", clubs[i]['name'] + " club phone number", "Can you give me the phone number for the " \
                      + clubs[i]['name'] + " club", "how do i contact the " + clubs[i]['name'] + " club"
            response = 'clubs', i, None, None, 'contact'
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

        return write
