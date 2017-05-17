# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt


class Graph(object):

    @staticmethod
    def draw_box_plot(data):
        bplot = plt.boxplot(data,
                    vert=True,
                    patch_artist=True,
                            whis=1.5)

        bplot['boxes'][0].set_facecolor('lightgreen')
        plt.axes().set_xlabel(u'Communication')
        plt.axes().set_ylabel(u'Second(s)')

        plt.show()

