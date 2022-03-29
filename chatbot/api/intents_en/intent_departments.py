import json
from scrapers.departments import DepartmentScraper

departments = DepartmentScraper().get()


class IntentDepartment:

    def generate(self, write):
        for i in departments:
            tag = departments[i]['name'] + " departments"
            pattern = departments[i]['name'] + " department ", "can you tell me about the " + departments[i][
                'name'] + " department ", "can you get information on the " + departments[i]['name'] + " department"
            response = 'departments', i, None, None, None
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

            tag = departments[i]['name'] + " club"
            pattern = departments[i]['name'] + " club", "can you tell me about the " + departments[i][
                'name'] + " club", "can you get information on the " + departments[i]['name'] + " club"
            response = None, None, None, [departments[i]['name'] + " is not a listed club."], None
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

        return write
