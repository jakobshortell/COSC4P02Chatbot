from flask import Flask, request
from scrapers.clubs import ClubScraper
from scrapers.departments import DepartmentScraper
from scrapers.important_dates import ImportantDatesScraper
from scrapers.courses import CoursesScraper
from scrapers.programs import ProgramScraper
from scrapers.exams import ExamScraper
from scrapers.restaurant import RestaurantScraper
from bot import Bot

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

    # Obtain user message from the POST request
    request_data = request.get_json()
    user_message = request_data['userMessage'].lower()




    # CLEAN UP HERE DOWN

    response = {}
    
    msg = Bot.chat(user_message)
    print(msg)

    index = msg[0] # The index of data in the category
    category = msg[1] # The category of data to get

    # Access selection data using category and index
    all_data = scrapers[category].get()
    selection_data = all_data[index]

    '''
    The pieces of data below all have some form of standardized response and seem
    to work well enough to be tested.

    Example standard response

    {
        "table_name": TABLE_NAME,
        "index": INDEX,
        "associated_indexes": [INDEX, INDEX]  # Can be left empty if not pertinant
        ...
    }

    '''

    if category == 'clubs':
        # name = selection_data['name']
        # description = selection_data['description']
        # email = selection_data['email']

        values = list(selection_data.values())
        response['content'] = ', '.join(values)

    elif category == 'departments':
        # name = selection_data['name']
        # description = selection_data['description']
        # link = selection_data['link']
        # social = selection_data['social']
        # email = selection_data['email']
        # extension = selection_data['extension']

        values = list(selection_data.values())
        response['content'] = ', '.join(values)

    elif category == 'exams':
        # course_code = selection_data['course_code']
        # duration = selection_data['duration']
        # day = selection_data['day']
        # start = selection_data['start']
        # end = selection_data['end']
        # location = selection_data['location']

        values = list(selection_data.values())
        response['content'] = ', '.join(values)

    '''
    These categories below come with a different output from Bot.chat() or don't
    appear to be working correctly so they haven't really been touched. The value
    in bot.py was left unchanged for now.
    '''

    if 'dates' in msg[1]:
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

    elif 'programs' in msg[1]:
        programs = scrapers['programs'].get()
        response['content'] = programs[msg[0]]['name'] + "\n" + programs[msg[0]]['description'] + "\n" + programs[msg[0]]['prerequisites']

    elif 'courses' in msg[1]:
        courses = CoursesScraper().get()
        msg_temp = ''
        for i in range(msg[3]):
            x = msg[0] - i
            msg_temp += "\n" + courses[x]['duration'] + " " + courses[x]['day'] + " " + courses[x]['time'] + " " + courses[x]['type'] + " " + courses[x]['instructor']
        response['content'] = courses[msg[0]]['course_code'] + " " + courses[msg[0]]['title'] + msg_temp

    else:
        response['content'] = 'Error, something went wrong.'

    return response


if __name__ == '__main__':
    app.run(debug=True)
