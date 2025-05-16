from stats import word_count, character_count,dict_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def output_print(path,total_words,char_list ):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path[2:]}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for entry in char_list:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")


def main():
        path = f"./{sys.argv[1]}" #/books/frankenstein.txt"
        contents = get_book_text(path)
        total_words = word_count(contents)
        total_chars = character_count(contents)
        sorted_dictionary = dict_sort(total_chars)
        output_print(path, total_words, sorted_dictionary)


try:
    main()
except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



