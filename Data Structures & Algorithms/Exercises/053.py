#
# HT: Get
#
# Implement the get_item method for the HashTable class
# that retrieves the value associated with a given key from the
# hash table
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796300
#


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        hash = 0
        for letter in key:
            hash = (hash + ord(letter) * 23) % len(self.data_map)
        return hash

    def get_item(self, key):
        hash = self.__hash(key)
        if self.data_map[hash] is None:
            return None
        for item in self.data_map[hash]:
            if item[0] == key:
                return item[1]
        return None
