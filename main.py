from stats import *
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    list_dict = []
    for item in chars_dict:
        list_dict.append({'character': item,'count': chars_dict[item]})

    list_dict.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {sys.argv[1]} ---")
    # print(f"{num_words} words found in the document\n")
    print(f"Found {num_words} total words")
    for item in list_dict:
        # print(f"The '{item["character"]}' character was found {item["count"]} times")
        print(f"{item["character"]}: {item["count"]}")
    print("--- End Report ---")

def sort_on(dict):
    return dict['count']

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
