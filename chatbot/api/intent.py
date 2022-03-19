import json
from scrapers.clubs import ClubScraper
from scrapers.departments import DepartmentScraper
from scrapers.important_dates import ImportantDatesScraper
from scrapers.courses import CoursesScraper
from scrapers.programs import ProgramScraper
from scrapers.exams import ExamScraper
from scrapers.restaurant import RestaurantScraper

dates = ImportantDatesScraper().get()
departments = DepartmentScraper().get()
clubs = ClubScraper().get()
courses = CoursesScraper().get()
programs = ProgramScraper().get()
exams = ExamScraper().get()
restaurant = RestaurantScraper().get()

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
                "Hi there, how can I help?",
                "Hello, there, how can I help you today?",
                "Good to see you, do you have any question?"
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
                "Bye, hope to talk to you again soon.",
                "Good bye, its been great talking to you",
                "Glad I could help, Bye!"
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
                "No problem, is there anything else you need?",
                "Glad I could help!",
                "It's nice to feel useful once in awhile ;)"
            ]
        },
        {
            "tag": "restaurant_list",
            "patterns": [
                "what restaurants are available at brock",
                "I'm Hungry",
                "What is good to eat at brock",
                "What food offerings are available at brock"
            ],
            "responses": [
                "Here is a list of restaurants available at Brock:",
                "restaurant_list"
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
                "Get the latest Brock University News at: https://brocku.ca/brock-news/",
                "Here is the latest news at Brock University: https://brocku.ca/brock-news/"
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
                "Click the link to get a list of important dates at Brock University: https://brocku.ca/important-dates/",
                "Here is a list of important dates at Brock University: https://brocku.ca/important-dates/"
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
                "Click the link to get a list of fall/winter important dates at Brock University: https://brocku.ca/important-dates/#fall-winter",
                "Here is a list of fall/winter important dates at Brock University: https://brocku.ca/important-dates/#fall-winter"
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
                "Click the link for directions to Brock University: https://www.google.com/maps?q=Brock+University",
                "Here is directions to Brock University: https://www.google.com/maps?q=Brock+University"
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
        pattern = departments[i]['name'] + " department ", "tell me about the " + departments[i][
            'name'] + " department "
        response = i, 'departments', departments[i]['name']
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
            pattern = courses[i - 1]['course_code'] + " course", courses[i - 1]['title'] + " course", "tell me about " + \
                      courses[i - 1]['course_code'] + " course"
            response = i - 1, 'courses', courses[i - 1]['course_code'], cnt
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

    for i in dates:
        tag = dates[i]['occasion'] + " dates"
        pattern = dates[i]['occasion'] + " important dates " + dates[i]['date']
        response = i, 'dates', dates[i]['occasion'], dates[i]['date']
        new = {
            "tag": tag,
            "patterns": [
                pattern
            ],
            "responses":
                response
        }
        intent['intents'].append(new)
        f.seek(0)
        json.dump(intent, f, indent=2)

    for i in clubs:
        tag = clubs[i]['name'] + " clubs"
        pattern = clubs[i]['name'] + " club", "tell me about the " + clubs[i]['name'] + " club"
        response = i, 'clubs', clubs[i]['name']
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
        pattern = programs[i]['name'] + " program", "tell me about the " + programs[i]['name'] + " program"
        response = i, 'programs', programs[i]['name']
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
        pattern = exams[i]['course_code'] + " exam", "when is the " + exams[i]['course_code'] + " exam"
        response = i, 'exams', exams[i]['course_code']
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
        pattern = restaurant[i]['name'] + " restaurant", "when is " + restaurant[i]['name'] + " open"
        response = i, 'restaurants', restaurant[i]['name']
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
