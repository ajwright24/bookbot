import sys

def get_book_text(file):
    with open(file) as f: # f is a file object
        return f.read()
    
from stats import count_words
from stats import count_unique_char
from stats import sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    contents = get_book_text(book_path)
    total_words = count_words(contents)
    unique_char_dict = count_unique_char(contents)
    sorted_output = sorted_list(unique_char_dict)
    
    print("========BOOKBOT========")
    print(f"Analyzing book found at {book_path}")
    print ("--------Word Count--------")
    print(f"Found {total_words} total words")
    print("--------Character Count--------")
    for d in sorted_output:
        if d["name"].isalpha():
            print(f"{d["name"]}: {d["num"]}")

main()