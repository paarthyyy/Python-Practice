<<<<<<< HEAD
def swap_first_last_chars(sentence: str) -> str:
    words = sentence.split(" ")
    swapped_words = []

    for word in words:
        if len(word) <= 1:
            swapped_words.append(word)
        else:
            new_word = word[-1] + word[1:-1] + word[0]
            swapped_words.append(new_word)
    return " ".join(swapped_words)

text = "hello world dojo"
result = swap_first_last_chars(text)
=======
def swap_first_last_chars(sentence: str) -> str:
    words = sentence.split(" ")
    swapped_words = []

    for word in words:
        if len(word) <= 1:
            swapped_words.append(word)
        else:
            new_word = word[-1] + word[1:-1] + word[0]
            swapped_words.append(new_word)
    return " ".join(swapped_words)

text = "hello world dojo"
result = swap_first_last_chars(text)
>>>>>>> 0981ad8685c870ca7bf0ce4be72d496e180f8ead
print(result)