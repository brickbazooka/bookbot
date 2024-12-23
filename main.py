def get_file_contents(path):
	with open(path) as f:
		return f.read()

def get_num_words(txt):
	return len(txt.split())

def get_char_count(txt):
	result = {}
	for _char in txt:
		char = _char.lower()
		if(char not in result):
			result[char] = 0
		result[char] += 1
	return result

def print_book_report(book_path):
	text = get_file_contents(book_path)
	num_words = get_num_words(text)
	char_count = get_char_count(text)
	
	alpha_list = []
	for char in char_count:
		if char.isalpha():
			alpha_list.append({ "char": char, "count": char_count[char] })
	alpha_list.sort(reverse=True, key=lambda dict: dict["count"])

	print(f"--- Begin report of {book_path} ---")
	print(f"{num_words} words found in the document\n")
	for letter in alpha_list:
		char = letter["char"]
		count = letter["count"]
		print(f"The '{char}' character was found {count} times")
	print("--- End report ---")

def main():
	book_path = "books/frankenstein.txt"
	print_book_report(book_path)

main()