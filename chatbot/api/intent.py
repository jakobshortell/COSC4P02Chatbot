import json
from scrapers.clubs import ClubScraper
from scrapers.departments import DepartmentScraper
from scrapers.important_dates import ImportantDatesScraper
from scrapers.courses import CoursesScraper
from scrapers.programs import ProgramScraper
from scrapers.exams import ExamScraper

dates = ImportantDatesScraper().get()
departments = DepartmentScraper().get()
clubs = ClubScraper().get()
courses = CoursesScraper().get()
programs = ProgramScraper().get()
exams = ExamScraper().get()

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
                "",
                ""
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
                "",
                ""
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
                "",
                ""
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
                "Get the latest Brock University News at https://brocku.ca/brock-news/",
                ""
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
                ""
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
                ""
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
                ""
            ]
        },
    ]
}
with open('intents.json', 'r+') as f:
    f.truncate(0)
    f.seek(0)
    json.dump(intent, f)

    for i in departments:
        tag = departments[i]['name']
        pattern = departments[i]['name'] + " department ", "tell me about the " + departments[i]['name'] + " department "
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
            tag = courses[i-1]['course_code']
            pattern = courses[i-1]['course_code'] + " course", courses[i-1]['title'] + " course", "tell me about " + courses[i-1]['course_code'] + " course"
            response = i-1, 'courses', courses[i-1]['course_code'], cnt
            new = {
                "tag": tag,
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
        tag = dates[i]['occasion']
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
        tag = clubs[i]['name']
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
        tag = programs[i]['name']
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
        tag = exams[i]['course_code']
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

