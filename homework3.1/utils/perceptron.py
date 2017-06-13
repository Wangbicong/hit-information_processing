# -*- coding:utf-8 -*-
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, roc_curve, auc
from matplotlib import pyplot as plt


class MyPerceptron(object):

    def __init__(self, *args, **kwargs):
        self.ppn = Perceptron(*args, **kwargs)
        self.sc = StandardScaler()

    def train(self, x_train, y_train):
        self.sc.fit(x_train)
        x_train_std = self.sc.transform(x_train)
        self.ppn.fit(x_train_std, y_train)

    def predict(self, x_test, y_test):
        x_test_std = self.sc.transform(x_test)
        y_predict = self.ppn.predict(x_test_std)

        self.x_test = x_test_std
        self.y_test = y_test

        print('准确率: %.5f' % accuracy_score(y_test, y_predict))
        print('错误数: %d' % (y_predict!=y_test).sum())

    def draw_roc(self):

        false_positive_rate, true_positive_rate, thresholds = roc_curve(map(int, self.y_test), self.ppn.decision_function(self.x_test))

        # print len(self.y_test)
        # print len(self.ppn.decision_function(self.x_test))
        # print len(true_positive_rate)
        # print len(false_positive_rate)

        roc_auc = auc(false_positive_rate, true_positive_rate)

        plt.title('Receiver Operating Characteristic')
        plt.plot(false_positive_rate, true_positive_rate, 'b',
                 label='AUC = %0.4f' % roc_auc)
        plt.legend(loc='lower right')
        plt.plot([0, 1], [0, 1], 'r--')
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.ylabel('True Positive Rate')
        plt.xlabel('False Positive Rate')
        plt.show()

    def get_weights(self):
        print self.ppn.densify().coef_
        print self.ppn.intercept_


if __name__ == '__main__':
    pass
