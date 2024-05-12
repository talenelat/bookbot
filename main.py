def main():
    path_to_book = "./books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    count_words(book_text)


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    words = text.split()
    text_length = len(words)
    print(text_length)


main()
