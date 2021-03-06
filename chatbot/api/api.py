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

app = Flask(__name__, static_folder='../build', static_url_path='/')

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
    name = data[index]['name'].replace(' Club', '')
    if attributes == 'contact':
        msg = "Here is the email address for the " + name + " Club:\nEmail: " + data[index]['email']
    else:
        msg = "Here is some information about the " + name + " Club:\nDescription: " + data[index]['description'] + "\nEmail: " + data[index]['email']
    return msg

def contact(data, index):
    msg = "Here is the contact information for " + data[index]['name'] + ":\n" + \
          "\tDepartment: " + data[index]['department'] + "\n\tTitle: " + data[index]['title'] + \
          "\n\tEmail: " + data[index]['email'] + "\n\tPhone: " + data[index]['phone'] + \
          "\n\tLocation: " + data[index]['location']
    return msg

def department(data, index, attributes):
    if attributes == 'contact':
        msg = "Here is the contact information for " + data[index]['name'] + ":\nLink:\t" + data[index]['social'] + "\nEmail:\t" + data[index]['email'] + "\nPhone:\t" \
              + data[index]['extension']
    else:
        msg = "Here is some information about the " + data[index]['name'] + ":\nDescription: " + data[index]['description'] + "\nLink:\t" + data[index]['link'] +\
              "\nSocial:\t" + data[index]['social'] + "\nEmail:\t" + data[index]['email'] + "\nPhone:\t" + \
              data[index]['extension']
    return msg

def date(data, index):
    msg = data[index]['occasion'] + " " + data[index]['date']
    return msg

def transport(data, index):
    msg = "Here is some information about the " + data[index]['name'] + " transit:\n" + data[index]['description'] + "\nClick here for a " + \
          data[index]['name'] + " map: " + data[index]['link']
    return msg

def details(data, index, attributes):
    if attributes == 'prerequisites':
        msg = data[index]['course_code'] + " " + data[index]['course_name'] + " requires " + data[index]['prerequisite'] + " as a prerequisite"

    else:
        msg = "Here is some information about " + data[index]['course_code'] + " " + data[index]['course_name'] + "\nAlt Course-Code: " + data[index]['alt_course_code'] + \
              "\nDescription: " + data[index]['course_description'] + "\nHours:" + data[index]['hours'] + "\nRestrictions: " + \
              data[index]['restrictions'] + "\nPrerequisites: " + data[index]['prerequisite'] + \
              "\nCorequisite: " + data[index]['corequisite'] + "\nNotes: " + data[index]['notes'] + "\nReplace Grade: " + data[index]['replace_grade']
    return msg

def building(data, index, attributes):
    if attributes == 'code':
        msg = "The code for " + data[index]['name'] + " is " + data[index]['code'] + "\nClick the link to learn more: "\
              + data[index]['link']
    else:
        msg = data[index]['code'] + " code stands for " + data[index]['name'] + "\nClick the link to learn more: " + \
              data[index]['link']
    return  msg

def restaurant(data, index, attributes):
    if index is not None:
        if attributes == 'hours':
            msg = "Here the hours for " + data[index]['name'] + ":\n" + data[index]['hour']
        else:
            msg = data[index]['name'] + ":\nDescription: " + data[index]['description'] + "\nHours: " + data[index]['hour']
    else:
        msg = 'Here is a list of restaurants available at Brock:'
        for index in data:
            msg = msg + "\n" + data[index]['name']
        msg = msg + "\nIs there one you would like more information on?"
    return msg

def exam(data, index):
    msg = data[index]['course_code'] + " exam with duration " + data[index]['duration'] + " is on " + data[index]['day'] + ", starts at " \
          + data[index]['start'] + ", ends at " + data[index]['end'] + " and is located at " + data[index]['location']
    return  msg

def program(data, index, attributes):
    if attributes == 'prerequisites':
        msg = data[index]['name'] + " requires " + data[index]['prerequisites']  + " as a prerequisite"
    else:
        msg = "Here is some information about " + data[index]['name'] + "\nDescription: " + data[index]['description'] + "\nPrerequisites: " + data[index]['prerequisites']
    return msg

def course(data, index, associated_indexes):
    msg_temp = ''
    for i in range(associated_indexes):
        x = index - i
        msg_temp = msg_temp + "\n" + data[x]['duration'] + " - " + data[x]['day'] + " - " + data[x]['time'] + " - " + \
                data[x]['type'] + " - " + data[x]['instructor']

    msg = "Here is the schedule for " + data[index]['course_code'] + " " + data[index]['title'] + "\nDuration - Day - Time - Type - Instructor" + msg_temp
    return msg

@app.route('/api', methods=['POST', 'GET'])
def main():
    '''The main enpoint for requests made to the chatbot.'''
    request_data = request.get_json()
    user_message = request_data['userMessage'].lower()
    language = request_data['language']
    # Default response
    response = {
        'content': 'Error, something went wrong.'
    }
    bot_response = process_message(user_message, language)
    table_name, index, associated_indexes, messages, attributes = bot_response.values()

    # Output an attribute of the first element in the response as a test
    if (table_name is not None):
        data = scrapers[table_name].get()

    if 'clubs' == table_name:
        response['content'] = club(data, index, attributes)

    elif 'contacts' == table_name:
        response['content'] = contact(data, index)

    elif 'departments' == table_name:
        response['content'] = department(data, index, attributes)

    elif 'dates' == table_name:
        response['content'] = date(data, index)

    elif 'transportation' == table_name:
        response['content'] = transport(data, index)

    elif 'course_details' == table_name:
        response['content'] = details(data, index, attributes)

    elif 'buildings' == table_name:
        response['content'] = building(data, index, attributes)

    elif 'restaurants' == table_name:
        response['content'] = restaurant(data, index, attributes)

    elif 'exams' == table_name:
        response['content'] = exam(data, index)

    elif 'programs' == table_name:
        response['content'] = program(data, index, attributes)

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
