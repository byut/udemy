#
# Graph: Remove Vertex
#
# The remove_vertex method takes a vertex as input and
# removes it from the graph, along with all edges connected to it.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796284
#


class Graph:
    def __init__(self):
        self.adj_list = {}

    def remove_vertex(self, a):
        if a not in self.adj_list:
            return False
        for v in self.adj_list.keys():
            if v == a or v not in self.adj_list[a]:
                continue
            try:
                self.adj_list[v].remove(a)
            except ValueError:
                pass
        self.adj_list.pop(a)
        return True
