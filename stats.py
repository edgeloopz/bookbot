def word_count(book_string):
    word_list = book_string.split()
    total_words = len(word_list)
    return total_words

def character_count(book_string):
    #take string and lowercase all char
    lower_string = book_string.lower()
    #initialize character dictionary
    char_dict = {}
    #iterate to count the characters in book_string
    for char in lower_string:
    #logic to add to dictionary
        if char in char_dict:
        # Character exists in dict: increment
            char_dict[char] += 1
        else:
        # Character doesn't exist in dict: initialize
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def dict_sort(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_dictionary = {}
        char_dictionary = { "char": char, "num": count }
        char_list.append(char_dictionary)
    char_list.sort(reverse=True, key=sort_on)
    return char_list



