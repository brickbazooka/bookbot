def _get_file_content(path):
	with open(path) as f:
		return f.read()


def _get_char_count_map(text_content):
	result = {}
	for char in text_content.lower():
		result[char] = result.get(char, 0) + 1
	return result


def _process_content(text_content):
	char_count_map = _get_char_count_map(text_content)

	result = []
	for char in char_count_map:
		if char.isalpha():
			result.append({ "char": char, "count": char_count_map[char] })
	result.sort(reverse=True, key=lambda dict: dict["count"])

	return result


def print_book_report(book_path):
	text_content = _get_file_content(book_path)
	num_words = len(text_content.split())
	
	processed_data = _process_content(text_content)

	print("\n")
	print(f"--- Begin report of {book_path} ---")
	print(f"{num_words} words found in the document\n")
	for datum in processed_data:
		char = datum["char"]
		count = datum["count"]
		print(f"The '{char}' character was found {count} times")
	print("--- End report ---")
	print("\n")


print_book_report("./books/frankenstein.txt")