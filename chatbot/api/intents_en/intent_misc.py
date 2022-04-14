import json


class IntentMisc:

    def generate(self, write):
        intent = {
            "tag": "hello",
            "patterns": [
                "Hi",
                "Hello",
                "Hey",
                "Hi there",
                "Is anyone there?",
                "Good day"
            ],
            "responses": [
                None, None, None,
                ["Hi there, how can I help?",
                 "Hello, there, how can I help you today?",
                 "Good to see you, do you have any question?"],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "bye",
            "patterns": [
                "Bye",
                "See ya",
                "Talk to you later",
                "Good bye",
                "goodbye",
                "farewell"
            ],
            "responses": [
                None, None, None,
                ["Bye, hope to talk to you again soon!",
                 "Good bye, its been great talking to you!",
                 "Glad I could help, Bye!"],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "about brock",
            "patterns": [
                "tell me about brock",
                "tell me about brock university",
                "information about brock",
                "information about brock university",
                "brock university info",
                "is brock a good school"
            ],
            "responses": [
                None, None, None,
                ["Brock University is one of Canada’s top post-secondary institutions. Located in historic Niagara \
                region, Brock offers all the benefits of a young and modern university in a safe, community-minded city\
                 with beautiful natural surroundings.\nClick the link to learn more: https://brocku.ca/about/"],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "brock covid",
            "patterns": [
                "what is brock university doing about covid-19",
                "brock covid",
                "brock covid-19",
                "information about covid-19 at brock university",
                "covid at brock",
                "covid-19 requirements at brock"
            ],
            "responses": [
                None, None, None,
                ["Brock is committed to delivering to students a high-quality education and providing an outstanding \
                experience while taking steps to address COVID-19.\nClick the link to learn more: https://brocku.ca/coronavirus/"],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "brock residence",
            "patterns": [
                "residence at brock university",
                "I am looking for residence at brock",
                "tell me about living at brock",
                "staying at brock",
                "living at brock",
                "brock on campus living"
            ],
            "responses": [
                None, None, None,
                ["Live in one of Brock’s convenient and welcoming residences. You’ll stay close to campus, meet new \
                friends, and become a part of our vibrant community. Residences at Brock are home to almost 2,800 \
                students each year.\nClick the link to learn more: https://discover.brocku.ca/living/"],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "who are you",
            "patterns": [
                "who are you",
                "tell me about yourself",
                "what are you"
            ],
            "responses": [
                None, None, None,
                ["I'm a bot!",
                 "I'm a series of 1's and 0's.",
                 "I'm just a computer program and have no self awareness."],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "who made you",
            "patterns": [
                "who made you",
                "who are your creators",
                "who developed you",
                "where do you come from"
            ],
            "responses": [
                None, None, None,
                [
                    "I was developed by Marmik Bhatt, Tom Wallace, Jakob Shortell, Aedel Panicker, Hyejin Kim, Liam Mckissock and Lucas Kumara"],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "easteregg",
            "patterns": [
                "easteregg",
                "easter egg"
            ],
            "responses": [
                None, None, None,
                ["This is an Easter-egg!",
                 "Turbo Encabulator: https://www.youtube.com/watch?v=Ac7G7xOG2Ag"],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "thankyou",
            "patterns": [
                "thanks",
                "thank you",
                "thankyou",
                "thx",
                "i appreciate that ",
                "good response",
                "good bot"
            ],
            "responses": [
                None, None, None,
                ["No problem, is there anything else you need?",
                 "Glad I could help!",
                 "It's nice to feel useful once in awhile ;)"],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "weather",
            "patterns": [
                "weather",
                "can you get the weather at brock university",
                "what is the weather like at brock",
                "weather St. Catharines",
                "is it snowing",
                "is it raining",
                "is it sunny"
            ],
            "responses": [
                "weather", None, None, None, None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "do not know",
            "patterns": [
                "tell me something",
                "tell me something i do not know",
                "tell me something interesting",
                "give me a random fact"
            ],
            "responses": [
                None, None, None,
                ["Did you know that Bamboo is not wood, it is actually a type of grass.",
                 "Did you know that population of Australia is 25.7 million",
                 "Founding Fathers and former presidents John Adams, Thomas Jefferson and James Monroe each died on Independence Day (July 4th)"],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "restaurants",
            "patterns": [
                "what restaurants are available at brock",
                "I'm Hungry",
                "What is good to eat at brock",
                "What food offerings are available at brock",
                "can you tell restaurants at brock"
            ],
            "responses": [
                "restaurants", None, None, None, None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "brock news",
            "patterns": [
                "brock university news",
                "What is the latest news at brock",
                "upcoming events at brock",
                "whats up at brock"
            ],
            "responses": [
                "brock_news", None, None, None, None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "news",
            "patterns": [
                "news",
                "What is the latest news",
                "niagara news",
                "what is up around niagara"
            ],
            "responses": [
                "news", None, None, None, None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "events",
            "patterns": [
                "events",
                "What are some upcoming events",
                "niagara events",
                "events in the niagara region"
            ],
            "responses": [
                "events", None, None, None, None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "maps",
            "patterns": [
                "map of brock university",
                "show me an interactive map of brock university",
                "get a map of brock university",
                "map of brock",
                "show me the layout of brock"
            ],
            "responses": [
                None, None, None,
                [
                    "Click this link for an Interactive Map of Brock University: https://brocku.ca/blogs/campus-map/\nClick this link for a downloadable Map of Brock University: https://brocku.ca/facilities-management/wp-content/uploads/sites/84/2-BROCK-UNIVERSITY-CAMPUS-MAPS.pdf"],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "important_dates",
            "patterns": [
                "brock university important dates",
                "i need a list of important dates at brock university",
                "important dates"
            ],
            "responses": [
                None, None, None,
                [
                    "Click the link to get a list of important dates at Brock University: https://brocku.ca/important-dates/",
                    "Here is a list of important dates at Brock University: https://brocku.ca/important-dates/"],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "important_dates_fall",
            "patterns": [
                "brock university fall winter important dates",
                "i need a list of fall winter important dates at brock university",
                "fall winter important dates"
            ],
            "responses": [
                None, None, None,
                [
                    "Click the link to get a list of fall/winter important dates at Brock University: https://brocku.ca/important-dates/#fall-winter",
                    "Here is a list of fall/winter important dates at Brock University: https://brocku.ca/important-dates/#fall-winter"],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "directions",
            "patterns": [
                "directions to brock university",
                "Where is brock university",
                "directions to brock",
                "travel to brock"
            ],
            "responses": [
                None, None, None,
                [
                    "Click the link for directions to Brock University: https://www.google.com/maps?q=Brock+University",
                    "Here is directions to Brock University: https://www.google.com/maps?q=Brock+University"],
                None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "break chatbot",
            "patterns": [
                "break chatbot"
            ],
            "responses": [
                None, None, None, None, None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "brock departments",
            "patterns": [
                "tell me about brocks departments",
                "brock departments",
                "brock university departments"
            ],
            "responses": [
                None, None, None, ["Brock is a comprehensive university with an expansive undergraduate system as well as advanced research, post-graduate and doctoral programs.\nClick the link to learn more: https://brocku.ca/academics/"], None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "brock programs",
            "patterns": [
                "tell me about brocks programs",
                "brock programs",
                "brock university programs",
                "what programs are available at brock"
            ],
            "responses": [
                None, None, None, ["As a comprehensive university, Brock has an expansive selection of undergraduate programs as well as advanced research, post-graduate and doctoral options.\nClick the link to learn more: https://brocku.ca/programs/"], None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "brock clubs",
            "patterns": [
                "tell me about brocks clubs",
                "brock clubs",
                "brock university clubs",
                "what clubs are available at brock"
            ],
            "responses": [
                None, None, None, ["Brock University features over 100 unique and amazing clubs! \nClick the link to learn more: https://www.brockbusu.ca/involvement/clubs/directory"], None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "brock parking",
            "patterns": [
                "tell me about parking at brock",
                "brock parking",
                "brock university parking",
                "what parking options are available at brock"
            ],
            "responses": [
                None, None, None, ["Brock University features a number of different parking services. From hourly to season parking passes. \nClick the link to learn more: https://brocku.ca/parking-services/"], None
            ]
        }
        write['intents'].append(intent)
        intent = {
            "tag": "brock visiting",
            "patterns": [
                "tell me about visiting brock",
                "brock visit",
                "brock university visit",
                "i would like to visit brock",
                "brock tours",
                "are tours available at brock",
                "touring brock"
            ],
            "responses": [
                None, None, None, ["Many of our alumni say they fell in love with Brock when they toured our beautiful campus. We hope that you’ll feel the same way once you’ve visited the University. Campus tours are led by Brock students eager to show you what makes this such a special place to live and learn. \nClick the link to learn more: https://brocku.ca/about/visit-brock"], None
            ]
        }
        write['intents'].append(intent)
        return write
