import stats
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_file = sys.argv[1]

contents = stats.get_book_text(path_to_file)
total_words = stats.count_words(contents)
list_dictionary = stats.sort_dictionary(stats.count_characters(contents))

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {total_words} total words")
print("--------- Character Count -------")
for dictionary in list_dictionary:
    if dictionary["char"].isalpha():
        print(f"{dictionary["char"]}: {dictionary["num"]}")
print("============= END ===============")

