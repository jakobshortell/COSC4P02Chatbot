import random
from flask import Flask, request
from scrapers.clubs import ClubScraper
from scrapers.departments import DepartmentScraper
from scrapers.important_dates import ImportantDatesScraper
from scrapers.courses import CoursesScraper
from scrapers.programs import ProgramScraper
from scrapers.exams import ExamScraper
from scrapers.restaurant import RestaurantScraper
from scrapers.buildings import BuildingScraper
from scrapers.weather import WeatherScraper
from scrapers.course_details import CoursesDetailsScraper
from scrapers.brock_news import brockNewsScraper
from scrapers.events import eventScraper
from scrapers.news import newsScraper
from scrapers.transportation import TransportationScraper
from scrapers.contact import ContactScraper
from bot import process_message

app = Flask(__name__)

# Instantiate scheduler and pass in instances of scrapers
scrapers = {
    'clubs': ClubScraper(),
    'departments': DepartmentScraper(),
    'dates': ImportantDatesScraper(),
    'courses': CoursesScraper(),
    'programs': ProgramScraper(),
    'exams': ExamScraper(),
    'restaurants': RestaurantScraper(),
    'restaurant_list': RestaurantScraper(),
    'buildings': BuildingScraper(),
    'weather': WeatherScraper(),
    'course_details': CoursesDetailsScraper(),
    'brock_news': brockNewsScraper(),
    'news': newsScraper(),
    'events': eventScraper(),
    'transportation': TransportationScraper(),
    'contacts': ContactScraper()
}
def club(data, index, attributes):
    if (attributes == 'contact'):
        msg = data[index]['name'] + ":\nEmail: " + data[index]['email']
    else:
        msg = data[index]['name'] + ":\n" + data[index]['description'] + "\nEmail: " + data[index]['email']
    return msg

def contact(data, index):
    msg = data[index]['name'] + " contact information:\n" + \
          "\tDepartment: " + data[index]['department'] + "\n\tTitle: " + data[index]['title'] + \
          "\n\tEmail: " + data[index]['email'] + "\n\tPhone: " + data[index]['phone'] + \
          "\n\tLocation: " + data[index]['location']
    return msg

def department(data, index):
    msg = data[index]['name'] + ":\n" + data[index]['description'] + "\nLink:\t" + data[index]['link'] +\
          "\nSocial:\t" + data[index]['social'] + "\nEmail:\t" + data[index]['email'] + "\nPhone:\t" + \
          data[index]['extension']
    return msg

def date(data, index):
    msg = data[index]['occasion'] + " " + data[index]['date']
    return msg

def transport(data, index):
    msg = data[index]['name'] + "\n" + data[index]['description'] + "\nClick here for a " + \
          data[index]['name'] + " map: " + data[index]['link']
    return msg

def details(data, index):
    msg = data[index]['course_code'] + ": " + data[index]['course_name'] + "\n" + data[index]['alt_course_code'] + \
          "\n" + data[index]['course_description'] + "\n" + data[index]['hours'] + "\nRestrictions: " + \
          data[index]['restrictions'] + "\nPrerequisites: " + data[index]['prerequisite'] + \
          "\n" + data[index]['corequisite'] + "\n" + data[index]['notes'] + "\n" + data[index]['replace_grade']
    return msg

def building(data, index):
    msg = data[index]['code'] + " code stands for " + data[index]['name'] + "\nClick the link to learn more: " + \
          data[index]['link']
    return  msg

def restaurant(data, index):
    if (index is not None):
        msg = data[index]['name'] + ":\n" + data[index]['description'] + "\n" + data[index]['hour']
    else:
        msg = 'Here is a list of restaurants available at Brock:'
        for index in data:
            msg = msg + "\n" + data[index]['name']
        msg = msg + "\nIs there one you would like more information on?"
    return msg

def exam(data, index):
    msg = data[index]['course_code'] + " " + data[index]['duration'] + " " + data[index]['day'] + " " \
          + data[index]['start'] + " " + data[index]['end'] + " " + data[index]['location']
    return  msg

def program(data, index):
    msg = data[index]['name'] + "\n" + data[index]['description'] + "\n" + data[index]['prerequisites']
    return msg

def course(data, index, associated_indexes):
    msg_temp = ''
    for i in range(associated_indexes):
        x = index - i
        msg_temp = msg_temp + "\n" + data[x]['duration'] + " " + data[x]['day'] + " " + data[x]['time'] + " " + \
                   data[x]['type'] + " " + data[x]['instructor']

    msg = data[index]['course_code'] + " " + data[index]['title'] + msg_temp
    return msg

@app.route('/api', methods=['POST', 'GET'])
def main():
    '''The main enpoint for requests made to the chatbot.'''
    request_data = request.get_json()
    user_message = request_data['userMessage'].lower()
    #language = request_data['language']
    # Default response
    response = {
        'content': 'Error, something went wrong.'
    }
    bot_response = process_message(user_message)
    table_name, index, associated_indexes, messages, attributes = bot_response.values()

    # Output an attribute of the first element in the response as a test
    if (table_name is not None):
        data = scrapers[table_name].get()

    if 'clubs' == table_name:
        response['content'] = club(data, index, attributes)

    elif 'contacts' == table_name:
        response['content'] = contact(data, index)

    elif 'departments' == table_name:
        response['content'] = department(data, index)

    elif 'dates' == table_name:
        response['content'] = date(data, index)

    elif 'transportation' == table_name:
        response['content'] = transport(data, index)

    elif 'course_details' == table_name:
        response['content'] = details(data, index)

    elif 'buildings' == table_name:
        response['content'] = building(data, index)

    elif 'restaurants' == table_name:
        response['content'] = restaurant(data, index)

    elif 'exams' == table_name:
        response['content'] = exam(data, index)

    elif 'programs' == table_name:
        response['content'] = program(data, index)

    elif 'courses' == table_name:
        response['content'] = course(data, index, associated_indexes)

    elif 'weather' == table_name:
        response['content'] = data

    elif 'events' == table_name:
        response['content'] = data

    elif 'brock_news' == table_name:
        response['content'] = data

    elif 'news' == table_name:
        response['content'] = data

    else:
        response['content'] = random.choice(messages)

    return response


if __name__ == '__main__':
    app.run(debug=True)
