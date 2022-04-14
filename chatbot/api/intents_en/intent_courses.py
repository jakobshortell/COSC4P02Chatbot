from scrapers.courses import CoursesScraper

courses = CoursesScraper().get()

class IntentCourse:

    def generate(self, write):
        cnt = 1
        tagTemp = courses[0]['course_code']
        for i in range(1, len(courses)):
            tag = courses[i]['course_code']
            if tag == tagTemp:
                cnt = cnt + 1
            if tag != tagTemp:
                tag = courses[i - 1]['course_code']
                pattern = courses[i - 1]['course_code'] + " course time schedule", courses[i - 1][
                    'title'] + " course time schedule", "can you tell me when is the " + \
                          courses[i - 1]['course_code'] + " course", "can you get a time table for the " + \
                          courses[i - 1]['title'] + " course", "can you get a time table for the " + courses[i - 1][
                              'course_code'] \
                          + " course", "where is " + courses[i - 1]['course_code'], courses[i - 1][
                              'course_code'] + "location"
                response = 'courses', i - 1, cnt, None, None
                intent = {
                    "tag": tag + " courses",
                    "patterns":
                        pattern,
                    "responses":
                        response
                }
                cnt = 1
                tagTemp = courses[i]['course_code']
                write['intents'].append(intent)

        return write
