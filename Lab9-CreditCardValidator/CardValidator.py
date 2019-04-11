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


print(luhn(5555555555554444))
print(luhn(5305105105105100))
print(luhn(5555552555554444))
print(luhn(4111311111111111))
print(luhn(4012288888881881))
print(luhn(12345))