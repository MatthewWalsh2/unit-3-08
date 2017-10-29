#created by Matthew Walsh
#created on oct 2017
#created for IcS3U
#this program prints the alphabet lower and upper case with its unicode number

BEGINNING_NUMBER_UPPERCASE = 64
BEGINNING_NUMBER_LOWERCASE = 96
ALPHABET_SIZE = 26

def print_letters():
	
	for counter in range(1, ALPHABET_SIZE + 1):
		letter_number = BEGINNING_NUMBER_UPPERCASE + counter
		print(str(letter_number) + ' ' + unichr(letter_number))
		
	for counter in range(1, ALPHABET_SIZE + 1):
		letter_number = BEGINNING_NUMBER_LOWERCASE + counter
		print(str(letter_number) + ' ' + unichr(letter_number))
	
print_letters()

