from stats import no_words
from stats import generate_dict
from stats import sort_dict
import sys



def get_book_text(filepath):
    with open(filepath) as file:
        #return "Reading book from:" + filepath
        return file.read()

def main():

    #book_path = 'books/frankenstein.txt'
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    try:
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(no_words(get_book_text(book_path)))
        print("--------- Character Count -------")
        char_dict = sort_dict(generate_dict(get_book_text(book_path)))
        for key in char_dict:
          print(f"{key}: {char_dict[key]}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()