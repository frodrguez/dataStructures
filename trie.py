# Trie tree (or Prefix tree):
# This data structure is used to efficiently store strings, check for prefixes and words validation.
# In this implementation we'll have an insert, search and starts_with methods.
# How it works: we store letters in the children nodes recursively, and the last letter has an indication that is the end of the word.
# The main gain here is the starts_with method which allows us to return if the desired prefix exists in any stored word.
# This return is very fast due to the format the trie DS in built.

class trie_node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie_Tree:
    def __init__(self):
        self.root = trie_node()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = trie_node()
            cur_node = cur_node.children[c]
        cur_node.end_of_word = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]
        return cur_node.end_of_word

    def starts_with(self, prefix: str) -> bool:
        cur_node = self.root
        for c in prefix:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]
        return True


# Testing:
words = Trie_Tree()
words.insert('pen')
words.insert('pencil')
words.insert('peppers')
words.insert('be')
words.insert('hot')

# The words trie should look like this (T or F indicates our end_of_word boolean):

#              root
#             /  |  \
#        p(F)  b(F)  h(F)
#          |     |     |
#        e(F)  e(T)  o(F)
#       /    \         |
#   n(T)     p(F)    t(T)
#     |        |
#   c(F)     p(F)
#     |        |
#   i(F)     e(F)
#     |        |
#   l(T)     r(F)
#              |
#            s(T)

print(words.search('pen'))         # True
print(words.search('penc'))        # False
print(words.starts_with('penc'))   # True
print(words.starts_with('ho'))     # True
print(words.starts_with('hot'))    # True
print(words.starts_with('a'))      # False
print(words.starts_with('bee'))    # False
print(words.starts_with('ppers'))  # False
