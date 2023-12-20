#
# HT: Keys
#
# Implement the keys method for the HashTable class that
# returns a list of all the keys present in the hash table.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796298
#


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def keys(self):
        result = []
        for data in self.data_map:
            if data is None:
                continue
            for item in data:
                result.append(item[0])
        return result
