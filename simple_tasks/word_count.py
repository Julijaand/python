def count_words(sentence):
    word_count = len(sentence.split())
    return word_count

# test function
sentence = input("Please insert you sentence: ")
word_count = count_words(sentence)
print(f"Number of words in sentence is {word_count}")