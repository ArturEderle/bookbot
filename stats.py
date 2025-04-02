def get_book_text(book):
    with open(book, 'r', encoding='utf-8') as f:
        file_content = f.read()
        return file_content

def count_words(book_string):
    num_words = len(book_string.split())
    return num_words

def count_chars(book_string):
    char_count_dict = {}
    for char in book_string:
        lowered_char = char.lower()
        if lowered_char in char_count_dict:
            char_count_dict[lowered_char] += 1
        else:
            char_count_dict[lowered_char] = 1
    return char_count_dict

def sort_on(dictionary):
    return dictionary["amount"]

def sorted_list_of_counted_chars(char_count_dict):
    chars_list = []
    for char, count in char_count_dict.items():
        char_result_dict = {"char": char, "amount": count}
        chars_list.append(char_result_dict)
    return sorted(chars_list, key=sort_on, reverse=True)
