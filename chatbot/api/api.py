from flask import Flask, request

from scrapers.clubs import ClubScraper
from scrapers.departments import DepartmentScraper
from scrapers.important_dates import ImportantDatesScraper
from scrapers.courses import CoursesScraper
from scrapers.programs import ProgramScraper
from scrapers.exams import ExamScraper
from scrapers.restaurant import RestaurantScraper
from bot import Bot
import random

app = Flask(__name__)

# Instantiate scheduler and pass in instances of scrapers
scrapers = {
    'clubs': ClubScraper(),
    'departments': DepartmentScraper(),
    'dates': ImportantDatesScraper(),
    'courses': CoursesScraper(),
    'programs': ProgramScraper(),
    'exams': ExamScraper(),
    'restaurant': RestaurantScraper()
}



@app.route('/api', methods=['POST', 'GET'])
def main():
    '''The main enpoint for requests made to the chatbot.'''
    request_data = request.get_json()
    user_message = request_data['userMessage']

    # Default response
    response = {
        'content': 'Error, something went wrong.'
    }
    msg = Bot.chat(user_message.lower())
    # Output an attribute of the first element in the response as a test
    if 'club' in msg[1]:
        clubs = scrapers['clubs'].get()
        response['content'] = clubs[msg[0]]['name'] + ":\n" + clubs[msg[0]]['description'] + "\nEmail: " + clubs[msg[0]]['email']

    elif 'department' in msg[1]:
        departments = scrapers['departments'].get()
        response['content'] = departments[msg[0]]['name'] + ":\n" + departments[msg[0]]['description'] + "\nLink:\t" + departments[msg[0]]['link'] + "\nSocial:\t" + departments[msg[0]]['social'] + "\nEmail:\t" + departments[msg[0]]['email'] + "\nPhone:\t" + departments[msg[0]]['extension']

    elif 'dates' in msg[1]:
        dates = scrapers['dates'].get()
        response['content'] = dates[msg[0]]['occasion'] + " " + dates[msg[0]]['date']

    elif 'restaurants' in msg[1]:
        restaurant = scrapers['restaurant'].get()
        response['content'] = restaurant[msg[0]]['name'] + " " + restaurant[msg[0]]['description'] + " " + restaurant[msg[0]]['hour']

    elif 'restaurant_list' in msg[1]:
        restaurant = scrapers['restaurant'].get()
        msg_temp = ''
        for index in restaurant:
            msg_temp = msg_temp + "\n" + restaurant[index]['name']
        response['content'] = msg[0] + msg_temp + "\nIs there one you would like more information on?"

    elif 'exam' in msg[1]:
        exams = scrapers['exams'].get()
        response['content'] = exams[msg[0]]['course_code'] + " " + exams[msg[0]]['duration'] + " " + exams[msg[0]]['day'] + " " + exams[msg[0]]['start'] + " " + exams[msg[0]]['end'] + " " + exams[msg[0]]['location']

    elif 'programs' in msg[1]:
        programs = scrapers['programs'].get()
        response['content'] = programs[msg[0]]['name'] + "\n" + programs[msg[0]]['description'] + "\n" + programs[msg[0]]['prerequisites']

    elif 'courses' in msg[1]:
        courses = CoursesScraper().get()
        msg_temp = ''
        for i in range(msg[3]):
            x = msg[0] - i
            msg_temp = msg_temp + "\n" + courses[x]['duration'] + " " + courses[x]['day'] + " " + courses[x]['time'] + " " + courses[x]['type'] + " " + courses[x]['instructor']
        response['content'] = courses[msg[0]]['course_code'] + " " + courses[msg[0]]['title'] + msg_temp

    else:
        response['content'] = random.choice(msg)


    return response


if __name__ == '__main__':
    app.run(debug=True)
