import json
from scrapers.clubs import ClubScraper
from scrapers.departments import DepartmentScraper
#from scrapers.important_dates import ImportantDatesScraper
from scrapers.courses import CoursesScraper
from scrapers.programs import ProgramScraper
from scrapers.exams import ExamScraper
from scrapers.restaurant import RestaurantScraper
from scrapers.course_details import CoursesDetailsScraper

#dates = ImportantDatesScraper().get()
departments = DepartmentScraper().get()
clubs = ClubScraper().get()
courses = CoursesScraper().get()
programs = ProgramScraper().get()
exams = ExamScraper().get()
restaurant = RestaurantScraper().get()
details = CoursesDetailsScraper().get()

cnt = 1
tagTemp = ""

intent = {
    "intents": [
        {
            "tag": "hello",
            "patterns": [
                "Hi",
                "Hello",
                "Hey",
                "Hi there",
                "Is anyone there?",
                "Good day"
            ],
            "responses": [
                None, None, None,
                ["Hi there, how can I help?",
                "Hello, there, how can I help you today?",
                "Good to see you, do you have any question?"]
            ]
        },
        {
            "tag": "bye",
            "patterns": [
                "Bye",
                "See ya",
                "Talk to you later",
                "Good bye",
                "goodbye",
                "farewell"
            ],
            "responses": [
                None, None, None,
                ["Bye, hope to talk to you again soon.",
                "Good bye, its been great talking to you",
                "Glad I could help, Bye!"]
            ]
        },
        {
            "tag": "thankyou",
            "patterns": [
                "thanks",
                "thank you",
                "thx",
                "i appreciate that ",
                "good response",
                "good bot"
            ],
            "responses": [
                None, None, None,
                ["No problem, is there anything else you need?",
                "Glad I could help!",
                "It's nice to feel useful once in awhile ;)"]
            ]
        },
        {
            "tag": "do not know",
            "patterns": [
                "tell me something",
                "tell me something i do not know",
                "tell me something interesting",
                "give me a random fact"
            ],
            "responses": [
                None, None, None,
                ["Did you know that Bamboo is not wood, it is actually a type of grass.",
                 "Did you know that Homers the Odyssey was the first written book",
                 "Did you know that population of Australia is 25.7 million",
                 "Did you know that sweet potatoes in New Zealand are called Kumara"]
            ]
        },
        {
            "tag": "restaurant_list",
            "patterns": [
                "what restaurants are available at brock",
                "I'm Hungry",
                "What is good to eat at brock",
                "What food offerings are available at brock",
                "can you tell restaurants at brock"
            ],
            "responses": [
                "restaurant_list", None, None,
                "Here is a list of restaurants available at Brock:"
            ]
        },

        {
            "tag": "news",
            "patterns": [
                "brock university news",
                "What is the latest news",
                "upcoming events at brock"
            ],
            "responses": [
                None, None, None,
                ["Get the latest Brock University News at: https://brocku.ca/brock-news/",
                "Here is the latest news at Brock University: https://brocku.ca/brock-news/"]
            ]
        },
        {
            "tag": "important_dates",
            "patterns": [
                "brock university important dates",
                "i need a list of important dates at brock university",
                "important dates"
            ],
            "responses": [
                None, None, None,
                ["Click the link to get a list of important dates at Brock University: https://brocku.ca/important-dates/",
                "Here is a list of important dates at Brock University: https://brocku.ca/important-dates/"]
            ]
        },
        {
            "tag": "important_dates_fall",
            "patterns": [
                "brock university fall winter important dates",
                "i need a list of fall winter important dates at brock university",
                "fall winter important dates"
            ],
            "responses": [
                None, None, None,
                ["Click the link to get a list of fall/winter important dates at Brock University: https://brocku.ca/important-dates/#fall-winter",
                "Here is a list of fall/winter important dates at Brock University: https://brocku.ca/important-dates/#fall-winter"]
            ]
        },
        {
            "tag": "directions",
            "patterns": [
                "directions to brock university",
                "Where is brock university",
                "get brock university map"
            ],
            "responses": [
                None, None, None,
                ["Click the link for directions to Brock University: https://www.google.com/maps?q=Brock+University",
                "Here is directions to Brock University: https://www.google.com/maps?q=Brock+University"]
            ]
        },
    ]
}
with open('intents.json', 'r+') as f:
    f.truncate(0)
    f.seek(0)
    json.dump(intent, f)

    for i in departments:
        tag = departments[i]['name'] + " departments"
        pattern = departments[i]['name'] + " department ", "can you tell me about the " + departments[i][
            'name'] + " department ", "can you get information on the " + departments[i]['name'] + " department"
        response = 'departments', i, None, None
        new = {
            "tag": tag,
            "patterns":
                pattern,
            "responses":
                response
        }
        intent['intents'].append(new)
        tag = departments[i]['name'] + " club"
        pattern = departments[i]['name'] + " club", "can you tell me about the " + departments[i][
            'name'] + " club", "can you get information on the " + departments[i]['name'] + " club"
        response = None, None, None, departments[i]['name'] + " is not a listed club."
        new = {
            "tag": tag,
            "patterns":
                pattern,
            "responses":
                response
        }
        intent['intents'].append(new)
    f.seek(0)
    json.dump(intent, f, indent=2)

    tagTemp = courses[0]['course_code']
    for i in range(1, len(courses)):
        tag = courses[i]['course_code']
        if tag == tagTemp:
            cnt = cnt + 1
        if tag != tagTemp:
            tag = courses[i - 1]['course_code']
            pattern = courses[i - 1]['course_code'] + " course time schedule", courses[i - 1]['title'] + " course time schedule", "can you tell me when is the " + \
                      courses[i - 1]['course_code'] + " course", "can you get a time table for the " +\
                      courses[i-1]['title'] + " course", "can you get a time table for the " + courses[i-1]['course_code']\
                      + " course"
            response = 'courses', i-1, cnt, None
            new = {
                "tag": tag + " courses",
                "patterns":
                    pattern,
                "responses":
                    response
            }
            cnt = 1
            tagTemp = courses[i]['course_code']
            intent['intents'].append(new)
    f.seek(0)
    json.dump(intent, f, indent=2)



    for i in clubs:
        tag = clubs[i]['name'] + " clubs"
        pattern = clubs[i]['name'] + " club", "can you tell me about the " + clubs[i]['name'] + " club", \
                  "can you get information on the " + clubs[i]['name'] + " club"
        response = 'clubs', i, None, None
        new = {
            "tag": tag,
            "patterns":
                pattern,
            "responses":
                response
        }
        intent['intents'].append(new)
    f.seek(0)
    json.dump(intent, f, indent=2)

    for i in programs:
        tag = programs[i]['name'] + " programs"
        pattern = programs[i]['name'] + " program", "can you tell me about the " + programs[i]['name'] + " program", \
                  "can you get information on the " + programs[i]['name'] + " program"
        response = 'programs', i, None, None
        new = {
            "tag": tag,
            "patterns":
                pattern,
            "responses":
                response
        }
        intent['intents'].append(new)
        tag = programs[i]['name'] + " club"
        pattern = programs[i]['name'] + " club", "can you tell me about the " + programs[i]['name'] + " club", \
                  "can you get information on the " + programs[i]['name'] + " club"
        response = None, None, None, programs[i]['name'] + " is not a listed club."
        new = {
            "tag": tag,
            "patterns":
                pattern,
            "responses":
                response
        }
        intent['intents'].append(new)
    f.seek(0)
    json.dump(intent, f, indent=2)

    for i in exams:
        tag = exams[i]['course_code'] + " exams"
        pattern = exams[i]['course_code'] + " exam", "can you when is the " + exams[i]['course_code'] + " exam",\
                  "can you tell me where is the " + exams[i]['course_code'] + "exam"
        response = 'exams', i, None, None
        new = {
            "tag": tag,
            "patterns":
                pattern,
            "responses":
                response
        }
        intent['intents'].append(new)
    f.seek(0)
    json.dump(intent, f, indent=2)

    for i in restaurant:
        tag = restaurant[i]['name'] + " restaurant"
        pattern = restaurant[i]['name'] + " restaurant", "when is " + restaurant[i]['name'] + " open",\
                  "can you get information on " + restaurant[i]['name'] + " restaurant"
        response = 'restaurants', i, None, None
        new = {
            "tag": tag,
            "patterns":
                pattern,
            "responses":
                response
        }
        intent['intents'].append(new)
    f.seek(0)
    json.dump(intent, f, indent=2)

    for i in details:
        tag = details[i]['course_code'] + " details"
        pattern = details[i]['course_code'] + " details", "can you tell me about " + details[i]['course_code'] + " course",\
                  "can you get information on " + details[i]['course_code'] + " course", "can you tell me about "\
                  + details[i]['course_name'] + " course", "can you get information on " + details[i]['course_name'] + " course"
        response = 'course_details', i, None, None
        new = {
            "tag": tag,
            "patterns":
                pattern,
            "responses":
                response
        }
        intent['intents'].append(new)
    f.seek(0)
    json.dump(intent, f, indent=2)

