# -*- coding:utf-8 -*-
import os
import glob


class Parser(object):

    @staticmethod
    def parser(file_path, title=None):

        result = dict()
        result['data'] = []

        if os.path.isdir(file_path):
            result['title'] = title
            for files in os.listdir(file_path):
                with open(file_path + '/' + files) as f:

                    for line in f:
                        result['data'].append(Parser.parser_str(line))

        elif os.path.isfile(file_path):
            with open(file_path) as f:

                if not title:
                    title = Parser.parser_str(f.readline())
                result['title'] = title

                for line in f:
                    result['data'].append(Parser.parser_str(line))
        else:
            raise IOError, 'The file path is wrong!'

        return result

    @staticmethod
    def parser_str(text, sep=','):
        return text.strip().split(sep)


if __name__ == '__main__':
    pass
