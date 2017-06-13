# encoding:utf-8
from utils.csv import Parser
from utils.multi_perceptron import MultiPerceptron


def load():

    global x_train
    global y_train
    global x_test
    global y_test

    x_train, y_train = Parser.part_parser('data/trnOverTraj30K.csv')
    x_test, y_test = Parser.parser('data/tstOverTraj10K.csv')


def multi_perceptron():

    ppn = MultiPerceptron(hidden_layer_sizes=(2, 5, 5), alpha=0.001, max_iter=50)
    ppn.train(x_train, y_train)
    ppn.predict(x_test, y_test)
    ppn.get_weights()
    ppn.draw_roc()


if __name__ == '__main__':
    load()
    multi_perceptron()