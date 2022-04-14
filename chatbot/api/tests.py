import unittest

from bot import process_message


class GeneralTests(unittest.TestCase):
    '''Tests regarding basic communication with the chatbot.'''

    def test_greeting(self):
        '''Saying a greeting to the chatbot.'''
        self.assertEqual(
            process_message('Hello', 'en'),
            {
                'table_name': None,
                'index': None,
                'associated_indexes': None,
                'messages': [
                    'Hi there, how can I help?',
                    'Hello, there, how can I help you today?',
                    'Good to see you, do you have any question?'
                ],
                'attributes': None
            }
        )
        self.assertEqual(
            process_message('Hey there!', 'en'),
            {
                'table_name': None,
                'index': None,
                'associated_indexes': None,
                'messages': [
                    'Hi there, how can I help?',
                    'Hello, there, how can I help you today?',
                    'Good to see you, do you have any question?'
                ],
                'attributes': None
            }
        )
        self.assertEqual(
            process_message('Hi', 'en'),
            {
                'table_name': None,
                'index': None,
                'associated_indexes': None,
                'messages': [
                    'Hi there, how can I help?',
                    'Hello, there, how can I help you today?',
                    'Good to see you, do you have any question?'
                ],
                'attributes': None
            }
        )

    def test_farewell(self):
        '''Saying goodbye to the chatbot.'''
        self.assertEqual(
            process_message('Bye', 'en'),
            {
                'table_name': None,
                'index': None,
                'associated_indexes': None,
                'messages': [
                    'Bye, hope to talk to you again soon!',
                    'Good bye, its been great talking to you!',
                    'Glad I could help, Bye!'
                ],
                'attributes': None
            }
        )
        self.assertEqual(
            process_message('Goodbye', 'en'),
            {
                'table_name': None,
                'index': None,
                'associated_indexes': None,
                'messages': [
                    'Bye, hope to talk to you again soon!',
                    'Good bye, its been great talking to you!',
                    'Glad I could help, Bye!'
                ],
                'attributes': None
            }
        )

    def test_misc(self):
        '''Saying any miscellaneous questions unrelated to the scraped data.'''
        self.assertEqual(
            process_message('Who made you?', 'en'),
            {
                'table_name': None,
                'index': None,
                'associated_indexes': None,
                'messages': [
                    'I was developed by Marmik Bhatt, Tom Wallace, Jakob Shortell, Aedel Panicker, Hyejin Kim, Liam Mckissock and Lucas Kumara'
                ],
                'attributes': None
            }
        )
        self.assertEqual(
            process_message('Easter egg', 'en'),
            {
                'table_name': None,
                'index': None,
                'associated_indexes': None,
                'messages': [
                    'This is an Easter-egg!',
                    'Turbo Encabulator: https://www.youtube.com/watch?v=Ac7G7xOG2Ag'
                ],
                'attributes': None
            }
        )


class BrockBuildingCodeTests(unittest.TestCase):
    '''Tests regarding the request for building codes Brock University.'''

    def test_building_name(self):
        '''Requesting a building name.'''
        self.assertEqual(
            process_message('What building is WH?', 'en'),
            {
                'table_name': 'buildings',
                'index': 73,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )
        self.assertEqual(
            process_message('What is the building name of MCJ?', 'en'),
            {
                'table_name': 'buildings',
                'index': 36,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )

    def test_building_code(self):
        '''Requesting a building code.'''
        self.assertEqual(
            process_message(
                'What is the building code for Mackenzie Chown Block J?', 'en'),
            {
                'table_name': 'buildings',
                'index': 36,
                'associated_indexes': None,
                'messages': None,
                'attributes': 'code'
            }
        )
        self.assertEqual(
            process_message(
                'Can you tell me the building code of Mackenzie Chown J Block?',
                'en'),
            {
                'table_name': 'buildings',
                'index': 36,
                'associated_indexes': None,
                'messages': None,
                'attributes': 'code'
            }
        )


class BrockClubTests(unittest.TestCase):
    '''Tests regarding the request for club data from Brock University.'''

    def test_club_email(self):
        '''Requesting the contact email of a club.'''
        self.assertEqual(
            process_message(
                'Can you give me the contact email for the american sign language club?',
                'en'),
            {
                'table_name': 'clubs',
                'index': 1,
                'associated_indexes': None,
                'messages': None,
                'attributes': 'contact'
            }
        )
        self.assertEqual(
            process_message(
                'What is the email for the chess club?', 'en'),
            {
                'table_name': 'clubs',
                'index': 22,
                'associated_indexes': None,
                'messages': None,
                'attributes': 'contact'
            }
        )

    def test_club_description(self):
        '''Requesting the description of a club.'''
        self.assertEqual(
            process_message(
                'Tell me about the american sign language club.', 'en'),
            {
                'table_name': 'clubs',
                'index': 1,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )
        self.assertEqual(
            process_message(
                'What is the chess club about?', 'en'),
            {
                'table_name': 'clubs',
                'index': 22,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )

    def test_unknown_club(self):
        '''Requesting club info that the bot doesn't have.'''
        self.assertEqual(
            process_message(
                'Can you tell me about the computer science club?', 'en'),
            {
                'table_name': None,
                'index': None,
                'associated_indexes': None,
                'messages': [
                    'Computer Science is not a listed club.'
                ],
                'attributes': None
            }
        )


class BrockCourseTests(unittest.TestCase):
    '''Tests regarding the request for course information from Brock University.'''

    def test_course_description(self):
        '''Requesting the description of a course.'''
        self.assertEqual(
            process_message('Can you tell me about COSC 4P02 course?', 'en'),
            {
                'table_name': 'course_details',
                'index': 789,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )
        self.assertEqual(
            process_message('What is COSC 4P02 about?', 'en'),
            {
                'table_name': 'course_details',
                'index': 789,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )

    def test_course_prerequisites(self):
        '''Requesting the prerequisites of a course.'''
        self.assertEqual(
            process_message(
                'Can you tell me the prerequisites for the COSC 4P02 course?',
                'en'),
            {
                'table_name': 'course_details',
                'index': 789,
                'associated_indexes': None,
                'messages': None,
                'attributes': 'prerequisites'
            }
        )
        self.assertEqual(
            process_message('What are the prerequisites for COSC 4P02?', 'en'),
            {
                'table_name': 'course_details',
                'index': 789,
                'associated_indexes': None,
                'messages': None,
                'attributes': 'prerequisites'
            }
        )


class BrockDepartmentTests(unittest.TestCase):
    '''Tests regarding the request for department related information from Brock University.'''

    def test_department_phone(self):
        '''Requesting the phone number of a department.'''
        self.assertEqual(
            process_message(
                'Can you tell me the phone number for the Critical Animal Studies department?',
                'en'),
            {
                'table_name': 'departments',
                'index': 75,
                'associated_indexes': None,
                'messages': None,
                'attributes': 'contact'
            }
        )
        self.assertEqual(
            process_message(
                'What is the phone number of the Computer Science department?',
                'en'),
            {
                'table_name': 'departments',
                'index': 68,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )

    def test_department_email(self):
        '''Requesting the email of a department.'''
        self.assertEqual(
            process_message(
                'Can you tell me the email for the Critical Animal Studies department?',
                'en'),
            {
                'table_name': 'departments',
                'index': 75,
                'associated_indexes': None,
                'messages': None,
                'attributes': 'contact'
            }
        )
        self.assertEqual(
            process_message(
                'What is the email for the Department of Computer Science?',
                'en'),
            {
                'table_name': 'departments',
                'index': 68,
                'associated_indexes': None,
                'messages': None,
                'attributes': 'contact'
            }
        )

    def test_department_description(self):
        '''Requesting the description of a department.'''
        self.assertEqual(
            process_message(
                'Can you tell me about the Critical Animal Studies department?',
                'en'),
            {
                'table_name': 'departments',
                'index': 75,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )
        self.assertEqual(
            process_message(
                'Can you give me information about the Department of Computer Science?',
                'en'),
            {
                'table_name': 'departments',
                'index': 68,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )


class BrockExamsTests(unittest.TestCase):
    '''Tests regarding to the exam schedule for Brock University.'''

    def test_exam_info(self):
        '''Requesting the information about a courses exam.'''
        self.assertEqual(
            process_message('can you when is the ACTG 1P02 exam', 'en'),
            {
                'table_name': 'exams',
                'index': 3,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )


class BrockImportantDatesTests(unittest.TestCase):
    '''Tests regarding various important dates at Brock University.'''

    def test_important_date(self):
        '''Requesting the date of a specific important event.'''
        pass


class BrockNewsTests(unittest.TestCase):
    '''
    Tests regarding the request for news from Brock University.

    NOTE: Mock data will be required as function pulls dynamic data
    '''
    pass


class BrockOfferingTests(unittest.TestCase):
    '''Tests regarding the request for course offering information from Brock University.'''

    def test_offering_instructor(self):
        '''Requesting the instructor of an offering.'''
        pass

    def test_offering_time(self):
        '''Requesting the time an offering takes place.'''
        pass


class BrockProgramsTests(unittest.TestCase):
    '''Tests regarding the request for program information from Brock University.'''

    def test_program_description(self):
        '''Requests a description of a program.'''
        self.assertEqual(
            process_message(
                'Can you tell me about the Engineering Science program?',
                'en'),
            {
                'table_name': 'programs',
                'index': 31,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )

    def test_program_prerequisites(self):
        '''Requests the prerequisites of a program.'''
        self.assertEqual(
            process_message(
                'Can you tell me about the prerequisites for the Engineering Science program?',
                'en'),
            {
                'table_name': 'programs',
                'index': 31,
                'associated_indexes': None,
                'messages': None,
                'attributes': 'prerequisites'
            }
        )


class BrockRestaurantsTests(unittest.TestCase):
    '''Tests regarding information about dining options at Brock University.'''

    def test_restaurant_list(self):
        '''Requests a list of dining options.'''
        self.assertEqual(
            process_message('What restaurants are available at Brock?', 'en'),
            {
                'table_name': 'restaurants',
                'index': None,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )
        self.assertEqual(
            process_message(
                'What dining options does Brock have available to students?',
                'en'),
            {
                'table_name': 'restaurants',
                'index': None,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )

    def test_restaurant_description(self):
        '''Requests a description of a specific restaurant.'''
        self.assertEqual(
            process_message(
                'Can you tell me about Burrito Boyz restaurant?', 'en'),
            {
                'table_name': 'restaurants',
                'index': 7,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )

    def test_restaurant_hours(self):
        '''Requests the hours of a specific restaurant.'''
        self.assertEqual(
            process_message('when is the Burrito Boyz restaurant open?', 'en'),
            {
                'table_name': 'restaurants',
                'index': 7,
                'associated_indexes': None,
                'messages': None,
                'attributes': 'hours'
            }
        )


class BrockTransportationTests(unittest.TestCase):
    '''Tests regarding the request for information about transportation to Brock University.'''

    def test_specific_transportation(self):
        '''Requesting transportation information in a specific area.'''
        self.assertEqual(
            process_message(
                'Can you tell me about the transportation options for Welland?',
                'en'),
            {
                'table_name': 'transportation',
                'index': 2,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )


class BrockNewsTests(unittest.TestCase):
    '''
    Tests regarding the request for news at Brock University.

    NOTE: Mock data will be required as function pulls dynamic data
    '''

    def test_brock_news(self):
        self.assertEqual(
            process_message('What is the latest news at Brock?', 'en'),
            {
                'table_name': 'brock_news',
                'index': None,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )
        self.assertEqual(
            process_message(
                'What sort of things are happening at Brock University?',
                'en'),
            {
                'table_name': 'brock_news',
                'index': None,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )


class NiagaraEventsTests(unittest.TestCase):
    '''
    Tests regarding the request for events happening in the Niagara Region.

    NOTE: Mock data will be required as function pulls dynamic data
    '''

    def test_niagara_events(self):
        self.assertEqual(
            process_message(
                'What events are taking place in the Niagara region?', 'en'),
            {
                'table_name': 'events',
                'index': None,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )
        self.assertEqual(
            process_message(
                'Whats events are happening in Niagara right now?', 'en'),
            {
                'table_name': 'events',
                'index': None,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )


class NiagaraNewsTests(unittest.TestCase):
    '''
    Tests regarding the request for news related to the Niagara Region.

    NOTE: Mock data will be required as function pulls dynamic data
    '''

    def test_niagara_news(self):
        self.assertEqual(
            process_message('Whats on the news in Niagara?', 'en'),
            {
                'table_name': 'news',
                'index': None,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )
        self.assertEqual(
            process_message('What is happening in the Niagara region?', 'en'),
            {
                'table_name': 'news',
                'index': None,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )


class NiagaraWeatherTests(unittest.TestCase):
    '''
    Tests regarding information about the weather in the Niagara Region.

    NOTE: Mock data will be required as function pulls dynamic data
    '''

    def test_niagara_weather(self):
        self.assertEqual(
            process_message('What is the weather like at Brock?', 'en'),
            {
                'table_name': 'weather',
                'index': None,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )
        self.assertEqual(
            process_message(
                'What is the weather like in St. Catharines?', 'en'),
            {
                'table_name': 'weather',
                'index': None,
                'associated_indexes': None,
                'messages': None,
                'attributes': None
            }
        )


if __name__ == '__main__':
    unittest.main()
