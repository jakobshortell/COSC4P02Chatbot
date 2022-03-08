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
    if 'club' in msg[0]:
        clubs = scrapers['clubs'].get()
        response['content'] = clubs[msg[1]]['name'] + ":\n" + clubs[msg[1]]['description'] + "\nEmail: " + clubs[msg[1]]['email']

    elif 'department' in msg[0]:
        departments = scrapers['departments'].get()
        response['content'] = departments[msg[1]]['name'] + ":\n" + departments[msg[1]]['description'] + "\nLink:\t" + departments[msg[1]]['link'] + "\nSocial:\t" + departments[msg[1]]['social'] + "\nEmail:\t" + departments[msg[1]]['email'] + "\nPhone:\t" + departments[msg[1]]['extension']

    elif 'dates' in msg[0]:
        dates = scrapers['dates'].get()
        response['content'] = dates[msg[1]]['occasion'] + " " + dates[msg[1]]['date']

    elif 'restaurants' in msg[0]:
        restaurant = scrapers['restaurant'].get()
        response['content'] = restaurant[msg[1]]['name'] + " " + restaurant[msg[1]]['description'] + " " + restaurant[msg[1]]['hour']

    elif 'restaurant_list' in msg[0]:
        restaurant = scrapers['restaurant'].get()
        msg_temp = ''
        for index in restaurant:
            msg_temp = msg_temp + "\n" + restaurant[index]['name']
        response['content'] = msg[1] + msg_temp + "\nIs there one you would like more information on?"

    elif 'exam' in msg[0]:
        exams = scrapers['exams'].get()
        response['content'] = exams[msg[1]]['course_code'] + " " + exams[msg[1]]['duration'] + " " + exams[msg[1]]['day'] + " " + exams[msg[1]]['start'] + " " + exams[msg[1]]['end'] + " " + exams[msg[1]]['location']

    elif 'programs' in msg[0]:
        programs = scrapers['programs'].get()
        response['content'] = programs[msg[1]]['name'] + "\n" + programs[msg[1]]['description'] + "\n" + programs[msg[1]]['prerequisites']

    elif 'courses' in msg[0]:
        courses = CoursesScraper().get()
        msg_temp = ''
        for i in range(msg[3]):
            x = msg[1] - i
            msg_temp = msg_temp + "\n" + courses[x]['duration'] + " " + courses[x]['day'] + " " + courses[x]['time'] + " " + courses[x]['type'] + " " + courses[x]['instructor']
        response['content'] = courses[msg[1]]['course_code'] + " " + courses[msg[1]]['title'] + msg_temp

    else:
        response['content'] = msg


    return response


if __name__ == '__main__':
    app.run(debug=True)
