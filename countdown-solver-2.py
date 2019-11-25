from itertools import permutations, combinations

dictionary = None

with open("words.txt", 'r', encoding='utf-8') as words:
	read_words = words.readlines()
	dictionary = {}
	for word in read_words:
		if word.islower():
			dictionary[word.strip()] = 1
	print("Sucessfully Read Dictionary! Ready for Game!\n")

def find_words(letters):
	found_words = {}
	words = []
	for i in range(2, len(game_letters) + 1):
		found_words[str(i)] = []
		cmbs = combinations(letters, i)
		for combination in cmbs:
			perm = permutations(combination)
			for word in perm:
				c_word = "".join(word)
				words.append(c_word)

	for c_word in set(words):
		if c_word in dictionary:
			found_words[str(len(c_word))].append(c_word)

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



		