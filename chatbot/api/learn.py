import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn
import tensorflow as tf
import json
import pickle
import gzip

language = []

for line in open("language.txt", "r"):
    language.append(line)


with open("intents_en/intents.json") as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        words_p = nltk.word_tokenize(pattern)
        words.extend(words_p)
        docs_x.append(words_p)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))
labels = sorted(labels)
training = []
output = []
out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []
    words_p = [stemmer.stem(w.lower()) for w in doc]
    for w in words:
        if w in words_p:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1
    training.append(bag)
    output.append(output_row)

training = numpy.array(training)
output = numpy.array(output)
with gzip.open('model_en/data', 'wb') as f:
    pickle.dump((words, labels, training, output), f)
print("Saving data")
tf.compat.v1.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 64)
net = tflearn.fully_connected(net, 64)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)
model = tflearn.DNN(net)

model.fit(training, output, n_epoch=1000, batch_size=4096, show_metric=True)
model.save("model_en/model.h5")







