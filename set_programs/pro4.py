#to find all the unique words and count the frequency of occurrence from a given list of strings.

def word_count(words):
    word_set = set(words)
    word_counts = {}
    for word in word_set:
        word_counts[word] = words.count(word)
    return word_counts

words = ["red","blue","green", "red", "blue"]

print(word_count(words))