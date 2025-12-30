from stats import wordcount, charcount, sorting
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        fileContent = f.read()
    return fileContent

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
        print(f"Found " + str(wordcount(get_book_text(sys.argv[1]))) + " total words")
        print("--------- Character Count -------")
        for i in sorting(charcount(get_book_text(sys.argv[1]))):
            print(i['char'] + ": " + str(i['num']))    
main()



