from collections import defaultdict

def convert_to_dict(book_text):
    char_counts = defaultdict(int)
    for char in book_text:
        char_counts[char] += 1
    return dict(char_counts)

def sort_char_dict(char_dict):
    def get_count(item):
        return item["count"]
    
    sorted_list = [{"char": char, "count": count} for char, count in char_dict.items()]
    sorted_list.sort(key=get_count, reverse=True)
    return sorted_list

def print_report(file_path, text, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    
    print("----------- Word Count ----------")
    print(f"Found {len(text.split())} total words")

    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        if char.isalpha():  # Only show alphabetic characters
            print(f"{char}: {item['count']}")
    print("============= END ===============")



file_path = 'books/frankenstein.txt'

with open(file_path, 'r') as book:
    text = book.read().lower()
    char_dict = convert_to_dict(text)
    sorted_chars = sort_char_dict(char_dict)
    print_report(file_path, text, sorted_chars)
