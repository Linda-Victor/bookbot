from stats import get_num_words, get_num_chars, sort_chars
import sys

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    number_of_words = get_num_words(text)
    number_of_characters = get_num_chars(text)
    sorted_characters = sort_chars(number_of_characters)
    print(f'============ BOOKBOT ============\nAnalyzing book found at {path}...')
    print(f'----------- Word Count ----------\nFound {number_of_words} total words')
    print('--------- Character Count -------')
    for character in sorted_characters:
        if character["Letter"].isalpha():
            print(f'{character["Letter"]}: {character["Number"]}')
    print('============= END ===============')

main()
