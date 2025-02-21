"""Strings and function calling."""


def main():
    sentence = "the quick brown fox jumps over the lazy dog the quick fox"
    print("Word Frequency:", word_frequency(sentence))
    print("Most Frequent Word:", most_frequent_word(sentence))
    print("Replace fox:", replace_word(sentence, "fox", "cat"))
    print("Replace cow:", replace_word(sentence, "cow", "cat"))

    paragraph = """
        Here is Edward Bear, coming downstairs now, bump, bump, bump, on the back of his head, behind Christopher Robin. It is, as far as he knows, the only way of coming downstairs, but sometimes he feels that there really is another way, if only he could stop bumping for a moment and think of it. And then he feels that perhaps there isn't. Anyhow, here he is at the bottom, and ready to be introduced to you. Winnie-the-Pooh.
    """
    paragraph_b = """
        Beatrice walked with determination, her senses alive to the magical pulses of the city that breathed around her. Lanterns glowing softly guided her through streets rich with secrets and untold stories, whispering to her of alliances to be forged in the heart of the night. It was a path laden with promises, each step bringing her closer to the unseen spirits eager to connect.
    """
    paragraph_c = "Why is the sky blue? It is a sunny day! I am going to the park."
    sentences = split_paragraph(paragraph_c)
    word_counts = word_count_by_sentence(paragraph_c)
    print(word_counts)
    print(sum_word_count(sentences[0], sentences[1]))


def word_frequency(sentence):
    # Takes a string sentence and returns a dictionary with each word as a key and its frequency as the value
    words = sentence.split()
    frequency = {}
    for word in words:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1
    return frequency


def most_frequent_word(sentence):
    # Return the word that appears the most in a sentence. Hint: RE-USE your word_frequency() function!
    frequency = word_frequency(sentence)
    most_frequent = ""
    highest_count = 0
    for word in frequency:
        if frequency[word] > highest_count:
            most_frequent = word
            highest_count = frequency[word]
    return most_frequent


def replace_word(sentence, word, new_word):
    # Return the sentence as a string with all examples of the specific word replaced with the new_word. If the word can't be found just return the original sentence.
    words = sentence.split()
    new_sentence = []
    for i in range(len(words)):
        if words[i] == word:  # we found our word
            new_sentence.append(new_word)
        else:  # the current word is just any other word
            new_sentence.append(words[i])
    return " ".join(new_sentence)


def split_paragraph(paragraph):
    # Return a LIST of all the sentences in the paragraph.
    # HINT: str.split() only takes 1 delimiter. Use str.replace(old, new) to replace the 3 different punctuation (., ?, !) with something else first, then split.
    # https://www.w3schools.com/python/ref_string_replace.asp
    paragraph = paragraph.replace("!", ".").replace("?", ".")
    sentences = paragraph.split(". ")
    return sentences


def word_count_by_sentence(paragraph):
    # Return a list of the word_frequency() for each sentence. Hint: reuse your word_frequency() function, and split_paragraph() function.
    # [{freq for first sentence}, {2nd sentence}, ...]
    sentences = split_paragraph(paragraph)
    x = []
    for sentence in sentences:
        x.append(word_frequency(sentence))
    return x


def sum_word_count(sentence1, sentence2):
    # Return the combined word_frequency for two sentences.
    combined_sentence = sentence1 + sentence2
    word_frequency(combined_sentence)

    combined_frequency = {}
    wfs1 = word_frequency(sentence1)
    wfs2 = word_frequency(sentence2)
    # loop through first dictionary and add everything to combined
    for k in wfs1:
        if k not in combined_frequency:  # new word
            combined_frequency[k] = 0
        combined_frequency[k] += 1

    for k in wfs2:
        if k not in combined_frequency:  # new word
            combined_frequency[k] = 0
        combined_frequency[k] += 1

    # for k in wfs1:
    #   print(k)

    # for v in wfs1.values():
    #   print(v)

    # for k, v in wfs1.items():
    #   print(k)
    #  print(v)


main()
