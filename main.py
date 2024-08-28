def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    print(f"--- Begin report of books/frankenstein.txt ---\n{word_count} words found in the document\n")
    for i in range(0,len(character_count)):
        print(f"The '{character_count[i][0]}' character was found {character_count[i][1]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

from collections import defaultdict

def get_character_count(text):
    occurances_dict = defaultdict(int)
    lowered_text = text.lower()
    for character in lowered_text:
        if character.isalpha():
            occurances_dict[character] +=1
    sorted_occurances = sorted(occurances_dict.items(), reverse=True, key=lambda item: item[1])
    return sorted_occurances

main()
