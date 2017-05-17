# -*- coding:utf-8 -*-
import re


class Parser(object):

    @staticmethod
    def parser(target, result):

        with open(target, 'r') as fin:
            with open(result, 'w') as fout:
                title = fin.readline()
                elements = title.split(',')[:6]
                fout.write(','.join(elements) + '\n')
                for line in fin:
                    elements = line.split(',')[:6]     # 保留前N个数据
                    elements[4] = Parser.format_time(elements[4])
                    if Parser.is_dirty(elements):
                        line = ','.join(elements)
                        fout.write(line + '\n')

    @staticmethod
    def parse_phone_and_time(target, result):

        hash_table = {}
        with open(target, 'r') as fin:
            fin.readline()
            for line in fin:
                elements = line.split(',')[:6]
                hash_table[elements[3]] = hash_table.get(elements[3], 0) + int(elements[4])

        with open(result, 'w') as fout:
            for key in hash_table:
                fout.write(key + ',' + str(hash_table[key]) + '\n')

    @staticmethod
    def get_time(target):
        result = []
        with open(target, 'r') as fin:
            for line in fin:
                result.append(int(line.split(',')[1].rstrip('\n')))
        return result

    @staticmethod
    def is_dirty(elements):
        result = True
        for element in elements:
            result = result and (element != '--')
        return result

    @staticmethod
    def format_time(t):
        hour = Parser.format_time_re('(\d)+小时', t)
        minute = Parser.format_time_re('(\d)+分', t)
        second = Parser.format_time_re('(\d)+秒', t)
        return str(hour*3600+minute*60+second)

    @staticmethod
    def format_time_re(expr, t):
        expr_re = re.search(expr, t)
        if expr_re:
            return int(expr_re.group(1))
        else:
            return 0




