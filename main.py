from stats import get_num_words, get_num_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
    print(f'{get_num_words(text)} words found in the document')
    print(get_num_chars(text))

main()
