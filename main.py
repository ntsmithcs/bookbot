from stats import get_num_words, get_char_count, get_sorted_char_counts
import sys

def main():
    """
    Main function that serves as the entry point for the application.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")

    book_text = get_book_text(filepath)
    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count = get_char_count(book_text)
    char_count_list = get_sorted_char_counts(char_count)
    for char in char_count_list:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

def get_book_text(filepath):
    """
    Reads the text of the book from the file.
    """
    with open(filepath, "r") as file:
        return file.read()

if __name__ == "__main__":
    main()
