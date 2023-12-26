#
# Graph: Add Edge
#
# Write a method called add_edge to the Graph class that
# adds a new edge between two vertices in the graph's
# adjacency list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796290
#


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, a, b):
        if a in self.adj_list and b in self.adj_list:
            self.adj_list[a].append(b)
            self.adj_list[b].append(a)
            return True
        return False
