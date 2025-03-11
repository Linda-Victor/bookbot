def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_number_of_words(text):
    print (f'{len(text.split())} words found in the document')

def main():
    print(get_book_text("books/frankenstein.txt"))
    get_number_of_words(get_book_text("books/frankenstein.txt"))

main()
