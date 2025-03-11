from stats import get_num_words, get_num_chars, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    number_of_words = get_num_words(text)
    number_of_characters = get_num_chars(text)
    sorted_characters = sort_chars(number_of_characters)
    print('============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...')
    print(f'----------- Word Count ----------\nFound {number_of_words} total words')
    print('--------- Character Count -------')
    for character in sorted_characters:
        if character["Letter"].isalpha():
            print(f'{character["Letter"]}: {character["Number"]}')
    print('============= END ===============')

main()
