from collections import Counter

class TextUtil:
    def __init__(self):
        self.text = ''
    
    def count_words(self, t):
        return len(t.split())
    
    def unique_words(self, t):
        uniq = set()
        result = ''
        for w in t.split():
            if w not in uniq:
                uniq.add(w)
                result = result + w + ' '
        return result.strip()
    
    def rev_string(self, t):
        return t[::-1]

tutil = TextUtil()
x = tutil.unique_words("Hello World Hello Bye Bye")
print(x)