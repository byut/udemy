#
# Graph: Remove Edge
#
# Write a method called remove_edge that removes an edge
# between two vertices in the graph's adjacency list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796288
#


class Graph:
    def __init__(self):
        self.adj_list = {}

    def remove_edge(self, a, b):
        if a in self.adj_list and b in self.adj_list:
            try:
                self.adj_list[a].remove(b)
                self.adj_list[b].remove(a)
            except ValueError:
                pass
            return True
        return False
