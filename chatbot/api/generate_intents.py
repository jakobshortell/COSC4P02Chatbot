import json
import custom_words
from intents_en.intent_misc import IntentMisc
from intents_en.intent_clubs import IntentClub
from intents_en.intent_departments import IntentDepartment
from intents_en.intent_courses import IntentCourse
from intents_en.intent_programs import IntentProgram
from intents_en.intent_exam import IntentExam
from intents_en.intent_restaurants import IntentRestaurant
from intents_en.intent_course_details import IntentCoursesDetails
from intents_en.intent_buildings import IntentBuilding
from intents_en.intent_transportation import IntentTransportation
from intents_en.intent_contacts import IntentContact

intents = [
    IntentMisc(),
    IntentClub(),
    IntentDepartment(),
    IntentCourse(),
    IntentProgram(),
    IntentExam(),
    IntentRestaurant(),
    IntentCoursesDetails(),
    IntentBuilding(),
    IntentTransportation(),
    IntentContact()
]


def gen_intents():
    '''Runs the generate() method on all intents.'''
    language = []

    for line in open("language.txt", "r"):
        language.append(line)

    for lang in language:
        total = len(intents)
        with open('intents_' + lang + '/intents.json', 'r+') as f:
            f.truncate(0)
            write = {
                "intents": [
                    ]
            }
            # Loop through intents and generating the intents.json
            for index, intent in enumerate(intents):
                print(f'[{index + 1}/{total}]', 'Generating... ', end='')

                try:
                    write = (intent.generate(write))
                    f.seek(0)
                    json.dump(write, f, indent=2)
                except Exception as e:
                    raise e
                finally:
                    print('Done.')

            print(f'Intent generation completed.')


if __name__ == '__main__':
    gen_intents()
