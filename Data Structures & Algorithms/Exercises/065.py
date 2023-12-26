#
# Graph: Add Vertex
#
# Implement the add_vertex method.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796294
#


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
