# -*- coding:utf-8 -*-
from data import hit, romania


class AStar(object):

    def __init__(self, data):
        self.nodes = data.nodes
        self.edges = data.edges
        self.direct_distances = data.direct_distances

        self.init_data()

    def init_data(self):
        nodes_table = {}
        for node in self.nodes:
            nodes_table[node] = {}
            for edge in self.edges:
                if node == edge[0]:
                    nodes_table[node][edge[1]] = edge[2]
                elif node == edge[1]:
                    nodes_table[node][edge[0]] = edge[2]
        self.nodes_table = nodes_table

    def search(self, start, end):
        fronts = [(start, None, 0, self.direct_distances[start])]  #数据含义：（节点, 前一节点, g(x), h(x), )
        while fronts:
            node = fronts.pop(0)
            if node[0] == end:
                return self.path(start, node)
            for node_front in self.nodes_table[node[0]]:
                # print node_front
                fronts.append((node_front, node, node[2]+self.nodes_table[node[0]][node_front], self.direct_distances[node_front]))
            fronts.sort(key=lambda x:x[2]+x[3])
        return 'Error!'

    def path(self, start, end_node):

        path_list = [end_node[0]]

        while end_node[1]:

            end_node = end_node[1]
            path_list.insert(0, end_node[0])

        return self.print_path(path_list)

    def print_path(self, path_list):
        print '从%s到%s: ' % (path_list[0], path_list[-1]),
        print '->'.join(path_list)


if __name__ == '__main__':
    hit_data = AStar(hit)
    hit_data.search("正心楼", "诚意楼")

    romania_data = AStar(romania)
    for romania_node in romania.nodes:
        print romania_node
        romania_data.search(romania_node, "Bucharest")
