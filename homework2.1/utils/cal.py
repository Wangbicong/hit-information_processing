# -*- coding:utf-8 -*-


class Calculation(object):
    def __init__(self, data):
        data.sort()
        self.data = data

    def cal(self):
        result = dict()
        result['avg'] = self.avg()
        result['large'] = self.large()
        result['min'] = self.min()
        result['q1'] = self.q1()
        result['mid'] = self.mid()
        result['q3'] = self.q3()
        result['max'] = self.max()
        return result

    def avg(self):
        return sum(self.data) / len(self.data)

    def mid(self):
        data = self.data
        if len(data) % 2:
            return data[len(data) / 2]
        else:
            return (data[len(data) / 2] + data[len(data) / 2 - 1]) / 2

    def large(self):
        data = self.data
        hash_map = {}

        for element in data:
            hash_map[element] = hash_map.get(element, 0) + 1

        max = 0
        target = None
        for key in hash_map:
            if hash_map[key] > max:
                max = hash_map[key]
                target = key

        return target

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def q1(self):
        return self.data[int(len(self.data) / 100.0 * 25)]

    def q3(self):
        return self.data[int(len(self.data) / 100.0 * 75)]
