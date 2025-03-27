import sys
from stats import convert_to_dict, sort_char_dict, print_report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]

with open(file_path, 'r') as book:
    text = book.read().lower()
    char_dict = convert_to_dict(text)
    sorted_chars = sort_char_dict(char_dict)
    print_report(file_path, text, sorted_chars)
