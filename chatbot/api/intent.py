import json
import custom_words
from scrapers.clubs import ClubScraper
from scrapers.departments import DepartmentScraper
#from scrapers.important_dates import ImportantDatesScraper
from scrapers.courses import CoursesScraper
from scrapers.programs import ProgramScraper
from scrapers.exams import ExamScraper
from scrapers.restaurant import RestaurantScraper
from scrapers.course_details import CoursesDetailsScraper
from scrapers.buildings import BuildingScraper

#dates = ImportantDatesScraper().get()
departments = DepartmentScraper().get()
clubs = ClubScraper().get()
courses = CoursesScraper().get()
programs = ProgramScraper().get()
exams = ExamScraper().get()
restaurant = RestaurantScraper().get()
details = CoursesDetailsScraper().get()
buildings = BuildingScraper().get()

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
                ["Bye, hope to talk to you again soon!",
                "Good bye, its been great talking to you!",
                "Glad I could help, Bye!"]
            ]
        },
        {
            "tag": "who are you",
            "patterns": [
                "who are you",
                "tell me about yourself",
                "what are you"
            ],
            "responses": [
                None, None, None,
                ["I'm a bot!",
                 "I'm a series of 1's and 0's.",
                 "I'm just a computer program and have no self awareness."]
            ]
        },
        {
            "tag": "who made you",
            "patterns": [
                "who made you",
                "who are your creators",
                "who developed you",
                "where do you come from"
            ],
            "responses": [
                None, None, None,
                ["I was developed by Marmik Bhatt, Tom Wallace, Jakob Shortell, Aedel Panicker, Hyejin Kim, Liam Mckissock and Lucas Kumara",
                 "Some people, I think?",
                 "No one cares.",
                 "Why do you care?"]
            ]
        },
        {
            "tag": "easteregg",
            "patterns": [
                "easteregg",
                "easter egg"
            ],
            "responses": [
                None, None, None,
                ["This is an Easter-egg!",
                 "Turbo Encabulator: https://www.youtube.com/watch?v=Ac7G7xOG2Ag",
                 "Click this link: https://i.pinimg.com/474x/63/19/6c/63196c900cfc344875d32a637ef17adc.jpg"]
            ]
        },
        {
            "tag": "thankyou",
            "patterns": [
                "thanks",
                "thank you",
                "thankyou",
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
            "tag": "weather",
            "patterns": [
                "weather",
                "can you get the weather at brock university",
                "what is the weather like at brock",
                "weather St. Catharines",
                "is it snowing",
                "is it raining",
                "is it sunny"
            ],
            "responses": [
                "weather", None, None, None
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
                 "Did you know that population of Australia is 25.7 million",
                 "Founding Fathers and former presidents John Adams, Thomas Jefferson and James Monroe each died on Independence Day (July 4th)"]
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
                "upcoming events at brock",
                "whats up at brock"
            ],
            "responses": [
                "news", None, None, None
            ]
        },
        {
            "tag": "maps",
            "patterns": [
                "map of brock university",
                "show me an interactive map of brock university",
                "get a map of brock university",
                "map of brock",
                "show me the layout of brock"
            ],
            "responses": [
                None, None, None,
                ["Click this link for an Interactive Map of Brock University: https://brocku.ca/blogs/campus-map/\nClick this link for a downloadable Map of Brock University: https://brocku.ca/facilities-management/wp-content/uploads/sites/84/2-BROCK-UNIVERSITY-CAMPUS-MAPS.pdf"]
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
                "directions to brock",
                "travel to brock"
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
                      + " course", "where is " + courses[i - 1]['course_code'], courses[i - 1]['course_code'] + "location"
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

    for i in buildings:
        tag = buildings[i]['code'] + " building"
        pattern = buildings[i]['code'] + " buildings", "what building is " + buildings[i]['code'], "what does " + buildings[i]['code'] + " stand for"
        response = 'buildings', i, None, None
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
