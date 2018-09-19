
import collections
#searching String version1

def string_find(x):

    x2 = x.replace(' ','')
    x2 = x2.lower()
    c = collections.Counter(x2)
    y = [char for char in x2 if c[char] ==1]
    print (x)
    print (y[0])

string_find('Deep data structure')
#Version2
def firstnonrepeatletter(word):
#  Function that accepts a string and returns the first non-repeating letter
    print(word)
# initialize variable count as list
    count = {}
# remove spaces and make string lowercase
    word.replace(' ','')
    word = word.lower()
    for letter in word:
        if letter not in count:
            count[letter] = 0
        count[letter] += 1
    for letter in word:
        if count[letter] == 1:
            return letter
print (firstnonrepeatletter('Deep data structure'))
