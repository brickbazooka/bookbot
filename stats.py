def get_num_words(text_content):
	return len(text_content.split())

def get_char_count_dict(text_content):
	result = {}
	for char in text_content.lower():
		result[char] = result.get(char, 0) + 1
	return result

def get_sorted_char_list(char_count_dict):
	result = []
	for char in char_count_dict:
		result.append({
			"char": char,
			"count": char_count_dict[char]
		})
	result.sort(reverse=True, key=lambda dict: dict["count"])

	return result