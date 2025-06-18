from stats import word_count
def main():
    file_path = "books/frankenstein.txt"
    file_contents = read_file(file_path)
    file_word_count = word_count(file_contents)
    file_letter_count = letter_count(file_contents)

    print(f"{file_word_count} words found in the document")
    list_chars = list_char_count(file_letter_count)
    


main()