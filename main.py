def main():
    path_to_book = "./books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    word_count = count_words(book_text)
    print(word_count)


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    words = text.split()
    text_length = len(words)
    return text_length


main()
