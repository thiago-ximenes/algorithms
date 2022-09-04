def merge_sort(word, start=0, end=None):
    if end is None:
        end = len(word)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(word, start, mid)
        merge_sort(word, mid, end)
        merge(word, start, mid, end)
        print(word)

    return word


def merge(word, start, mid, end):
    left = word[start:mid]
    right = word[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            word[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            word[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            word[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            word[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_string_sorted = "".join(merge_sort(list(first_string.lower())))
    second_string_sorted = "".join(merge_sort(list(second_string.lower())))

    if first_string_sorted == second_string_sorted:
        return True
    else:
        return False
