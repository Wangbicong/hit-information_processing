# encoding:utf-8
from utils.csv import Parser
from utils.perceptron import MyPerceptron
from utils.nearest_centroid import MyNearestCentroid


def load():

    global x_train
    global y_train
    global x_test
    global y_test

    x_train, y_train = Parser.part_parser('data/trnOverTraj30K.csv')
    x_test, y_test = Parser.parser('data/tstOverTraj10K.csv')


def perceptron():

    ppn = MyPerceptron(alpha=0.01, eta0=1, n_iter=5, class_weight={'1': 100, '-1':1})
    ppn.train(x_train, y_train)
    ppn.predict(x_test, y_test)
    ppn.get_weights()
    ppn.draw_roc()


def nearest_centroid():

    nrt = MyNearestCentroid(metric='euclidean')
    nrt.train(x_train, y_train)
    nrt.predict(x_test, y_test)
    nrt.draw_roc()


if __name__ == '__main__':
    load()
    # perceptron()
    nearest_centroid()