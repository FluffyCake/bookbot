import sys
from stats import count_words, character_count, sort_dict, print_dict

def get_book_text(filepath):
    file_contents = ""

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book = get_book_text(filepath)
    word_count = count_words(book)
    print("============ BOOKBOT ============")
    character_dict = character_count(book)
    sorted_character_list = sort_dict(character_dict)    
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_dict(sorted_character_list)
    print("============= END ===============")
main()
