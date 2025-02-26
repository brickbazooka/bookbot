import sys
from stats import get_num_words, get_char_count_dict, get_sorted_char_list


def get_file_content(path):
	with open(path) as f:
		return f.read()


def print_book_report(book_path):
	text_content = get_file_content(book_path)
	
	num_words = get_num_words(text_content)
	char_count_dict = get_char_count_dict(text_content)
	
	sorted_char_list = get_sorted_char_list(char_count_dict)

	print("============ BOOKBOT ============")
	print(f"Analyzing the book found at {book_path}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("----------- Char Count ----------")
	for datum in sorted_char_list:
		char, count = datum["char"], datum["count"]
		if char.isalpha():
			print(f"'{char}': {count}")
	print("============= END ===============")


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python main.py <path_to_book>")
		sys.exit(1)
	
	book_path = sys.argv[1]
	print_book_report(book_path)