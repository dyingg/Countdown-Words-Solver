from collections import Counter

dictionary = None

with open("words.txt", 'r', encoding='utf-8') as words:
	read_words = words.readlines()
	dictionary = {}
	for word in read_words:
		if word.islower():
			dictionary[word.strip()] = 1
	print("Sucessfully Read Dictionary! Ready for Game!\n")

def check_pos(word, letters):
	if Counter(word) - Counter(letters):
		return False
	return True

def find_words(letters):
	found_words = {}
	for i in range(2, len(letters) + 1):
		found_words[str(i)] = []
	
	for word in dictionary:
		l = len(word)
		if l <= len(letters) and l > 2:
			if check_pos(word, letters):
				found_words[str(len(word))].append(word)
		
	return found_words


def print_words(found_words, letters):
	l = len(letters)

	for i in range(l, 2, -1):
		print('=========== Words with %d letters ==========' % (i))
		if str(i) in found_words:
			print('\n'.join(found_words[str(i)]))
	


while True:
	print("Enter the game letters:\n")
	game_letters = input().split()
	k = find_words(game_letters)
	print_words(k, game_letters)