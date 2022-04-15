import nltk
import numpy
import tflearn
import tensorflow as tf
import json
import pickle
import gzip
import enchant
from enchant.checker import SpellChecker
from textblob import TextBlob
from nltk.stem.lancaster import LancasterStemmer


# nltk.download('punkt')

language = 'en'

stemmer = LancasterStemmer()
with open("intents_" + language + "/intents.json") as file:
    data = json.load(file)

with gzip.open('model_' + language + '/data', 'rb') as f:
    words, labels, training, output = pickle.load(f)

dic = enchant.DictWithPWL("en_US", "intents_en/customWords.txt")
chkr = SpellChecker(dic)


def naturalWords(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for st in s_words:
        for i, w in enumerate(words):
            if w == st:
                bag[i] = 1

    return numpy.array(bag)


def spell_check(message):

    chkr.set_text(message)
    for err in chkr:
        corr = TextBlob(err.word)
        message = message.replace(err.word, str(corr.correct()))
    return message


def process_message(message, lang):
    language = lang
    message = spell_check(message)

    tf.compat.v1.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 64)
    net = tflearn.fully_connected(net, 64)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)
    model.load('model_' + language + '/model.h5')

    results = model.predict([naturalWords(message, words)])[0]
    results_index = numpy.argmax(results)
    tag_index = labels[results_index]

    if results[results_index] > 0.3:
        for tag in data["intents"]:
            if tag['tag'] == tag_index:
                table_name, index, associated_indexes, messages, attributes = tag['responses']
                msg = {
                    "table_name": None or table_name,
                    "index": None or index,
                    "associated_indexes": None or associated_indexes,
                    "messages": None or messages,
                    "attributes": None or attributes
                }
    else:
        message = message.replace(' ', '+')
        msg = {
            "table_name": None,
            "index": None,
            "associated_indexes": None,
            "messages": ["I am sorry. I don\'t know  what you are asking.\nClick the link to Google your question https://www.google.com/search?q=" + message],
            "attributes": None
        }

    return msg
