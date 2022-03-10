import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()
import numpy
import tflearn
import tensorflow as tf
import json
import pickle
import gzip



def naturalWords(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for st in s_words:
        for i, w in enumerate(words):
            if w == st:
                bag[i] = 1

    return numpy.array(bag)


class Bot:
    def chat(msg):
        with open("intents.json") as file:
            data = json.load(file)

        with gzip.open('data', 'rb') as f:
            words, labels, training, output = pickle.load(f)
        tf.compat.v1.reset_default_graph()
        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 32)
        net = tflearn.fully_connected(net, 32)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)

        model = tflearn.DNN(net)

        model.load('model.h5')

        results = model.predict([naturalWords(msg, words)])[0]
        results_index = numpy.argmax(results)
        tag_index = labels[results_index]

        if results[results_index] > 0.4:
            for tag in data["intents"]:
                if tag['tag'] == tag_index:
                    response = tag['responses']
                    msg = {
                            "table_name": response[0],
                            "index": response[1],
                            "associated_indexes": response[2],
                            "messages": response[3]
                        }
        else:
            msg = {
                "table_name": "",
                "index": "",
                "associated_indexes": "",
                "messages": "I am sorry. I don\'t know  what you are asking."
            }
        return msg
