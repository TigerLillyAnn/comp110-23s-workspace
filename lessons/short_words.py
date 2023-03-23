"""Practice for Quiz 2"""

def short_words(words: list[str], max_length: int) -> list[str]:
    short_words_list = []
    for word in words:
        if len(word) <= max_length:
            short_words_list.append(word)
        else:
            print(word + " is too long!")
    return short_words_list