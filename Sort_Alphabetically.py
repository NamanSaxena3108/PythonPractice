def sort_sentence(sentence):
    words = sentence.split()
    print(words)
    sorted_words = sorted(words)
    print(sorted_words)
    sorted_sentence = ' '.join(sorted_words)
    return sorted_sentence

input_sentence = "the quick brown fox jumps over the lazy dog"
sorted_sentence = sort_sentence(input_sentence)
print("Sorted Sentence:", sorted_sentence)