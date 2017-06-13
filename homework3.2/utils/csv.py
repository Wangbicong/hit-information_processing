# -*- coding:utf-8 -*-


class Parser(object):

    @staticmethod
    def parser(file_path):
        x = []
        y = []
        with open(file_path) as f :
            for line in f:
                features = line.strip().split(',')
                x.append(features[:-1])
                y.append(features[-1])
        return x, y

    @staticmethod
    def part_parser(file_path):

        x, y = Parser.parser(file_path)

        i_1 = i_2 = 0
        result_x = []
        result_y = []

        for i in xrange(len(x)):
            if i_1 < len(x) / 4 and y[i] == '1':
                i_1 += 1
            elif i_2 < len(x) / 4 and y[i] == '-1':
                i_2 += 1
            else:
                continue
            result_x.append(x[i])
            result_y.append(y[i])

        return result_x, result_y


if __name__ == '__main__':
    pass
