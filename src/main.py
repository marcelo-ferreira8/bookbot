def main():
    with open("../books/frankenstein.txt") as f: 
        file_contents = f.read()
        print(len(count_words(file_contents)))


def count_words(book_text):
    words = book_text.split()
    return words


main()