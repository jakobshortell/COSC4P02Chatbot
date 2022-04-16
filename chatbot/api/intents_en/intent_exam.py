from scrapers.exams import ExamScraper

exams = ExamScraper().get()


class IntentExam:

    def generate(self, write):
        for i in exams:
            tag = exams[i]['course_code'] + " exams"
            pattern = exams[i]['course_code'] + " exam", "can you tell me when is the " + exams[i]['course_code'] + " exam", \
                      "can you tell me where is the " + exams[i]['course_code'] + " exam", "what is the schedule for "\
                      + exams[i]['course_code'] + " exam", "when is the " + exams[i]['course_code'] + " exam",\
                      exams[i]['course_code'] + " exam schedule"
            response = 'exams', i, None, None, None
            intent = {
                "tag": tag,
                "patterns":
                    pattern,
                "responses":
                    response
            }
            write['intents'].append(intent)

        return write
