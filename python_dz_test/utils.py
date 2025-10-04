def common_numbers(list1, list2):

    set2 = set(list2)
    seen = set()
    result = []
    for num in list1:
        if num in set2 and num not in seen:
            result.append(num)
            seen.add(num)
    return result


def words_starting_with_vowel(text):

    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = text.split()
    result = []
    for word in words:
        clean_word = word.strip(".,!?;:\"'()[]{}")
        if clean_word and clean_word[0].lower() in vowels:
            result.append(clean_word)
    return result