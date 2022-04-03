from scrapers.programs import ProgramScraper

programs = ProgramScraper().get()

class IntentProgram:

    def generate(self, write):
        for i in programs:
            tag = programs[i]['name'] + " programs"
            pattern = programs[i]['name'] + " program", "can you tell me about the " + programs[i]['name'] + " program", \
                      "can you get information on the " + programs[i]['name'] + " program"
            response = 'programs', i, None, None, None
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

            tag = programs[i]['name'] + " club"
            pattern = programs[i]['name'] + " club", "can you tell me about the " + programs[i]['name'] + " club", \
                      "can you get information on the " + programs[i]['name'] + " club"
            response = None, None, None, [programs[i]['name'] + " is not a listed club."], None
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

        for i in programs:
            tag = programs[i]['name'] + " program prerequisites"
            pattern = programs[i]['name'] + " program prerequisites", "can you tell me about the prerequisites for the "\
                      + programs[i]['name'] + " program", "can you get information on the prerequisites for "\
                      + programs[i]['name'] + " program"
            response = 'programs', i, None, None, 'prerequisites'
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

        return write