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
            "tag": "restaurant_list",
            "patterns": [
                "what restaurants are available at brock",
                "I'm Hungry",
                "What is good to eat at brock",
                "What food offerings are available at brock",
                "can you tell restaurants at brock"
            ],
            "responses": [
                "restaurant_list", None, None, None, None
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
        return write
