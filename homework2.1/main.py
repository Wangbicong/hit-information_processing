# -*- coding:utf-8 -*-
from utils.csv import Parser
from utils.graph import Graph
from utils.cal import Calculation


if __name__ == '__main__':

    Parser.parser('data/phone.csv', 'data/phone_clean.csv')
    Parser.parse_phone_and_time('data/phone_clean.csv', 'data/phone_and_time.csv')

    time_data = Parser.get_time('data/phone_and_time.csv')
    cal = Calculation(time_data)
    print time_data, len(time_data), time_data[80]
    print cal.cal()
    Graph.draw_box_plot(time_data)