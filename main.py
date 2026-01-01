def get_book_text(file):
    with open(file) as f: # f is a file object
        return f.read()
    
from stats import count_words
from stats import count_unique_char

def main():
    book_path = "books/frankenstein.txt"
    contents = get_book_text(book_path)
    total_words = count_words(contents)
    unique_char_dict = count_unique_char(contents)
    print(f"Found {total_words} total words")
    print(unique_char_dict)

main()