from model.Hashtable import HashTable

class HashTableController:
    def __init__(self, size):
        self.hash_table = HashTable(size)

    def add(self, key, value):
        self.hash_table.put(key, value)

    def remove(self, key):
        self.hash_table.remove(key)

    def get(self, key):
        return self.hash_table.get(key)

    def print_table(self):
        for index, bucket in enumerate(self.hash_table.table):
            if bucket is not None:
                print(f'Index {index}: {bucket}')