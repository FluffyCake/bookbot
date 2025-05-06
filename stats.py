def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def character_count(text):
    char_dict = {}

    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_dict:
            char_dict[lowered_char] += 1
        else:
            char_dict[lowered_char] = 1

    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(char_dict):
    list_of_dicts = []
    for char, count in char_dict.items():
        list_of_dicts.append({"char": char, "num": count})

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def print_dict(dict):   
    for item in dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

