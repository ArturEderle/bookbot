from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    book_string = get_book_text(path_to_book)
    chars_dict = count_chars(book_string)
    sorted_chars_list = sorted_list_of_counted_chars(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_string)} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['amount']}")
    print("============= END ===============")

if __name__ == '__main__':
    main()
