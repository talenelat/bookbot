def main():
    path_to_book = "./books/frankenstein.txt"
    book_text = get_book_text(path_to_book)

    word_count = count_words(book_text)
    letter_count = count_letter(book_text)

    letter_count_arr = []
    for letter in letter_count:
        letter_count_arr.append({"letter": letter, "num": letter_count[letter]})
    letter_count_arr.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path_to_book} ---")
    print(f"{word_count} words found in the document\n")

    for letter in letter_count_arr:
        print(f"The '{letter['letter']}' character was found {letter['num']} times")

    print("--- End report ---")


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    words = text.split()
    text_length = len(words)
    return text_length


def count_letter(text):
    letter_count = {}
    text_lowered = text.lower()
    for char in text_lowered:
        if char.isalpha():
            if char not in letter_count:
                letter_count[char] = 1
            else:
                letter_count[char] += 1
    return letter_count


def sort_on(dict):
    return dict["num"]


main()
