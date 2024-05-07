# Hash-Table:
# Python already have an inbuilt type called dictionary to serve as the hashtable data structure.
# It is accessible by declaring a variable like my_dict = dict(), or simply my_dict = {}.
# However, here I will be implementing one by scratch, using arrays.

# In this basic implementation I'll have methods for adding a key:value pair, removing a key and some others
# getters to see the keys or values stored so far, as well as getting a specified key or value:

class Hash_Table:
    def __init__(self):
        self.keys = []
        self.values = []
        self.items = []

    def __repr__(self):
        return str(self.items)

    def keys(self):
        return self.keys

    def values(self):
        return self.values

    def get_value(self, key):
        idx = self.keys.index(key)
        return self.values[idx]

    def get_key(self, value):
        idx = self.values.index(value)
        return self.keys[idx]

    def items(self):
        return self.items

    def remove(self, key):
        idx = self.keys.index(key)
        self.keys.remove(self.keys[idx])
        self.values.remove(self.values[idx])
        self.items.remove(self.items[idx])

    def add(self, key, value):
        self.keys.append(key)
        self.values.append(value)
        self.items.append(str(key)+" : "+str(value))


# Testing:
european_capitals = Hash_Table()
european_capitals.add('Belgium', 'Brussels')
european_capitals.add('UK', 'London')
print(european_capitals)  # ['Belgium : Brussels', 'UK : London']
print(european_capitals.get_value('UK'))  # London
print(european_capitals.get_key('Brussels'))  # Belgium
print(european_capitals.values)  # ['Brussels', 'London']
european_capitals.remove('Belgium')
print(european_capitals)  # ['UK : London']
