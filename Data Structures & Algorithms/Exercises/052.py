#
# HT: Set
#
# Implement the set_item method for the HashTable class
# that inserts a key-value pair into the hash table.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796304
#


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        hash = 0
        for letter in key:
            hash = (hash + ord(letter) * 23) % len(self.data_map)
        return hash

    def set_item(self, key, value):
        hash = self.__hash(key)
        if self.data_map[hash] is None:
            self.data_map[hash] = [[key, value]]
        else:
            self.data_map[hash].append([key, value])
