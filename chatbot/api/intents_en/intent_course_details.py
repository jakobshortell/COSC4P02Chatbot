from scrapers.course_details import CoursesDetailsScraper

details = CoursesDetailsScraper().get()

class IntentCoursesDetails:

    def generate(self, write):
        for i in details:
            tag = details[i]['course_code'] + " details"
            pattern = details[i]['course_code'] + " details", "can you tell me about " + details[i][
                'course_code'] + " course", \
                      "can you get information on " + details[i]['course_code'] + " course", "can you tell me about " \
                      + details[i]['course_name'] + " course", "can you get information on " + details[i][
                          'course_name'] + " course"
            response = 'course_details', i, None, None, None
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

        return write