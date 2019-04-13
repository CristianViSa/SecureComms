def luhn(card_number):
	sum = 0
	str_card_number = str(card_number)
	digits = list(str_card_number)
	double = 0
	num_digits = len(str_card_number) - 1
	while num_digits >= 0:
		digit = int(digits[num_digits])
		if double:
			digit = digit * 2
			if digit > 9:
				digit = (digit % 10) + 1
		sum = sum + digit
		double = not double
		num_digits = num_digits - 1

	return (sum % 10) == 0

def return_vendor(card_number):
	import csv
	card_number = str(card_number)
	with open('iin.txt', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter = ",")
		digitsMatch = 0
		vendor = ""
				
		for line in reader:
			bank = line[0]
			lenght = line[1]
			isRange = lenght.find("-")
			if isRange != -1:
				minLength = lenght[:isRange]
				maxLength = lenght[isRange+1:]
				if not(len(card_number)>=int(minLength) and len(card_number)<= int(maxLength)):
					continue
			else:
				if len(card_number) != int(lenght):
					continue
			for x in range(2,len(line)):
				rangeCard = line[x]
				isRange = rangeCard.find("-")
				if isRange != -1:
					minRange = rangeCard[:isRange]
					maxRange = rangeCard[isRange+1:]
					card_numbers = card_number[:len(minRange)]
					if(int(card_numbers) >= int(minRange) and int(card_numbers) <= int(maxRange)):
						if digitsMatch < len(card_numbers):
							digitsMatch = len(card_numbers)
							vendor = bank
						else:
							break
				else:
					match = 0
					for position in range (0, len(rangeCard)):
						digit = card_number[position]
						if int(digit) == int(rangeCard[position]):
							match = match + 1
						else:
							break
					if match == len(rangeCard) and match > digitsMatch:
						digitsMatch = match
						vendor = bank
	return vendor
def calculate_checksum(card_number):
	card_number = int(card_number)
	sum = 0
	str_card_number = str(card_number)
	digits = list(str_card_number)
	double = 1
	num_digits = len(str_card_number) - 1
	iterations = 0
	while num_digits >= iterations:
		digit = int(digits[iterations])
		if double:
			digit = digit * 2
			if digit > 9:
				digit = (digit % 10) + 1
		sum = sum + digit
		double = not double
		iterations = iterations + 1

	return (sum *9) % 10
	

def generate_vendor_card(vendor):
	import csv
	import random
	with open('iin.txt', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter = ",")
		card_digits_to_generate = 0
		card_number = ""
		for line in reader:
			bank = line[0]
			if bank == vendor:
				lenght = line[1]
				isRange = lenght.find("-")
				if isRange != -1:
					minLength = lenght[:isRange]
					maxLength = lenght[isRange+1:]
					lenght = random.randint(int(minLength),int(maxLength))
				else:
					lenght = int(lenght)
				rangeCard = line[2]
				isRange = rangeCard.find("-")
				if isRange != -1:
					minRange = rangeCard[:isRange]
					maxRange = rangeCard[isRange+1:]
					rangeCard = str(random.randint(int(minRange),int(maxRange)))
				else:
					rangeCard = int(rangeCard)
				card_digits_to_generate = lenght - len(str(rangeCard)) - 1
				card_number = card_number + str(rangeCard)
				for number in range (0, card_digits_to_generate):
					card_number = card_number + str(random.randint(int(0),int(9)))
				checksum = calculate_checksum(card_number)
				card_number = card_number + str(checksum)
				return card_number
		return card_number

if __name__ == "__main__":
	noStop = 1
	while noStop:
		print ("--- Credit Card Generator and Validator")
		print("1 - Verify a credit card number")
		print("2 - Determine vendor")
		print("3 - Calculate checksum")
		print("4 - Generate a valid credit card number")
		print("5 - Exit")
		option = input("Select an option ")
		if option == "1":
			card = int(input("Enter a card number : "))
			if luhn(card):
				print("The card number is valid")
			else:
				print("The card number is not valid")
		elif option == "2":
			card = int(input("Enter a card number : "))
			vendor = return_vendor(card)
			if vendor != "":
				print ("The vendor is " + vendor)
			else:
				if luhn(card):
					print("Vendor not found")
				else:
					print("Not a valid card")
		elif option == "3":
			card = int(input("Enter a card number : "))
			checksum = calculate_checksum(card)
			print("The checksum is "+ str(checksum))
		elif option == "4":
			vendor = input("Enter a vendor for the card : ")
			card = generate_vendor_card(vendor)
			if (card != ""):
				print("Your credit card number is " + card)
			else:
				print("You entered a not valid vendor")
		if (option == "5"):
			noStop = 0	