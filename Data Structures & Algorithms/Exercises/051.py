#
# HT: Constructor
#
# Create a HashTable class that represents a hash table data
# structure with a fixed-size array implementation.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796302
#


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        hash = 0
        for letter in key:
            hash = (hash + ord(letter) * 23) % len(self.data_map)
        return hash
