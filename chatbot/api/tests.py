import unittest

from bot import process_message


class GeneralTests(unittest.TestCase):
    '''Tests regarding basic communication with the chatbot.'''

    def test_greeting(self):
        '''Saying a greeting to the chatbot.'''
        pass

    def test_farewell(self):
        '''Saying goodbye to the chatbot.'''
        pass


class BrockBuildingCodeTests(unittest.TestCase):
    '''Tests regarding the request for building codes Brock University.'''

    def test_building_code(self):
        '''Requesting a building code.'''
        pass


class BrockClubTests(unittest.TestCase):
    '''Tests regarding the request for club data from Brock University.'''

    def test_club_email(self):
        '''Requesting the contact email of a club.'''
        self.assertEqual(
            process_message(
                'Can you give me the contact email for the american sign language club?'),
            {
                'table_name': 'clubs',
                'index': 1,
                'associated_indexes': None,
                'messages': None
            }
        )

    def test_club_description(self):
        '''Requesting the description of a club.'''
        self.assertEqual(
            process_message('Tell me about the american sign language club.'),
            {
                'table_name': 'clubs',
                'index': 1,
                'associated_indexes': None,
                'messages': None
            }
        )


class BrockCourseTests(unittest.TestCase):
    '''Tests regarding the request for course information from Brock University.'''

    def test_course_description(self):
        '''Requesting the description of a course.'''
        pass

    def test_course_prerequisites(self):
        '''Requesting the prerequisites of a course.'''
        pass


class BrockDepartmentTests(unittest.TestCase):
    '''Tests regarding the request for department related information from Brock University.'''

    def test_department_phone(self):
        '''Requesting the phone number of a department.'''
        pass

    def test_department_email(self):
        '''Requesting the email of a department.'''
        pass

    def test_department_description(self):
        '''Requesting the description of a department.'''
        pass


class BrockExamsTests(unittest.TestCase):
    '''Tests regarding to the exam schedule for Brock University.'''

    def test_exam_info(self):
        '''Requesting the information about a courses exam.'''
        pass


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
        pass

    def test_program_prerequisites(self):
        '''Requests the prerequisites of a program.'''
        pass


class BrockRestaurantsTests(unittest.TestCase):
    '''Tests regarding information about dining options at Brock University.'''

    def test_restaurant_list(self):
        '''Requests a list of dining options.'''
        pass

    def test_restaurant_description(self):
        '''Requests a description of a specific restaurant.'''
        pass

    def test_restaurant_hours(self):
        '''Requests the hours of a specific restaurant.'''
        pass


class BrockTransportationTests(unittest.TestCase):
    '''Tests regarding the request for information about transportation to Brock University.'''

    def test_specific_transportation(self):
        '''Requesting transportation information in a specific area.'''
        pass


class NiagaraEventsTests(unittest.TestCase):
    '''
    Tests regarding the request for events happening in the Niagara Region.

    NOTE: Mock data will be required as function pulls dynamic data
    '''
    pass


class NiagaraNewsTests(unittest.TestCase):
    '''
    Tests regarding the request for news related to the Niagara Region.

    NOTE: Mock data will be required as function pulls dynamic data
    '''
    pass


class NiagaraWeatherTests(unittest.TestCase):
    '''
    Tests regarding information about the weather in the Niagara Region.

    NOTE: Mock data will be required as function pulls dynamic data
    '''
    pass


if __name__ == '__main__':
    unittest.main()
