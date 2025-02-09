class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)

        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[key_hash].append([key, value])

    def get(self, key):
        key_hash = self.hash_function(key)

        for pair in self.table[key_hash]:
            if pair[0] == key:
                return pair[1]

        return None

    def delete(self, key):

        key_hash = self.hash_function(key)
        bucket = self.table[key_hash]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True

        return False


H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))  # 10
print(H.get("orange"))  # 20
print(H.get("banana"))  # 30

print(H.delete("orange"))
print(H.delete("orange"))
