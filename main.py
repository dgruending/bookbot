from collections import Counter

def get_book_text(book_path):
    with open("books/frankenstein.txt", "r") as book:
        file_content = book.read()
        return file_content

def word_count(text):
    return len(text.split())

def character_count(text):
    return Counter(text.lower())

def make_char_occurence_list(occurrences):
    return [{"char": key, "count": value} for key, value in occurrences.items() if key.isalpha()]

def __sort_on(dict):
    return dict["count"]

def print_report(book_path):
    book_text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count(book_text)} words found in the document\n")

    character_occurences = make_char_occurence_list(character_count(book_text))
    character_occurences.sort(reverse=True, key=__sort_on)
    for entry in character_occurences:
        print(f"The '{entry['char']}' character was found {entry['count']} times")

    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)

main()
