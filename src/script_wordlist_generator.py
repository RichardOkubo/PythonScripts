from itertools import permutations

text = input("Word: ")

wordlist = permutations(text, len(text))

for word in wordlist:
    print("".join(word))
