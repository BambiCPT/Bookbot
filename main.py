def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    report(book_path, word_count, letter_count)

#self-explanatory
def get_book_text(path):
    with open(path) as f:
        return f.read()

#avoid loop by seperating words in text, then counting the num# of words with len
def count_words(text):
    words = text.split()
    return len(words)

#counts all chars in text.lower() (to avoid duplicates), alternatively if I wanted only alphabetical characters, I'd use char.isalpha()
def count_letters(text):
    letters = {}
    for char in text.lower():
        if char.isalpha() and char not in letters:
            letters[char] = 1
        elif char.isalpha():
            letters[char] += 1
    return letters

def sort_on(dict):
    return dict['count']

def report(book_path, word_count, letter_count):
    letter_list = [{'letter':key, 'count':value} for key, value in letter_count.items()]
    letter_list.sort(reverse=True, key=sort_on)
    #report print
    print(f'--- Begin report of {book_path} ---')
    print(f'{word_count} words found in this document')

    for letter in letter_list:
        print(f'The {letter['letter']} character was found {letter['count']} times')
    print('--- End Report ---')

main()