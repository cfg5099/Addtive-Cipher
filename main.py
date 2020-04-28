LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
INDEX = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
Encrypted = ['-'] * 27;

def main():
	print("Enter the phrase to be encrypted: ")
	phrase = list(input())

	print("Enter the key to encode the phrase")
	key = input()

	newPhrase = encrypt(phrase, int(key))
	print("\n\nThe encrypted version has been made.")
	print("Finalt result: ", newPhrase)

def encrypt(phrase, key):
	result = phrase

	for x in range(0, len(phrase)):
		letter = phrase[x]

		pos = ord(letter) % 97
		if(letter == ' '):
			pos = 26
			result[x] = " "
			Encrypted[26] = " "
		if(Encrypted[pos] != '-'):
			result[x] = Encrypted[pos]

		else:
			cNumber = int(INDEX[pos]) + key
			print(cNumber)
			if(cNumber > 26):
				cNumber = cNumber % 26
			result[x] = cNumber
			Encrypted[pos] = cNumber
		pass

	return result
if __name__ == '__main__':
	main()