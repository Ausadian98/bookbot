from stats import *


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    list_dict = []
    for item in chars_dict:
        list_dict.append({'character': item,'count': chars_dict[item]})

    list_dict.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    # print(f"{num_words} words found in the document\n")
    print(f"Found {num_words} total words")
    for item in list_dict:
        # print(f"The '{item["character"]}' character was found {item["count"]} times")
        print(f"'{item["character"]}' {item["count"]}")
    print("--- End Report ---")

def sort_on(dict):
    return dict['count']

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
