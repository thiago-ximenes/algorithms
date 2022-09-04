def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    word_length = len(word)

    if word_length <= 1:
        return True

    if word[low_index] == word[high_index]:
        return (
            True
            if word[1: word_length - 1] == ""
            else is_palindrome_recursive(
                word[1: word_length - 1], 0, high_index - 2
            )
        )
    else:
        return False
