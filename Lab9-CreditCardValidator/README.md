Lab 9 - Credit card validator

First thing is to explain what a card number is. Every credit card has one PAN (Primary Account Number), or card number associated with it. The card number is the identifier for the card. Is made of digits which represents the issuing entity and the issuer of the card. These digits are created following the ISO/IEC 7812 standard.
The first 6 digits of the card number are the issuer identification number (IIN) (Nowadays it has been expanded to 8) and the remaining, except for the last digit, are the individual account identification number. The last digit is the Luhn Check Digit. The payment card numbers are composed of 8 to 19 digits.
So then, the Luhn Check Digit algorithm is a simple checksum formula which is used to validate card numbers and other identifiers, such as IMEI, etc.
This algorithm verifies a number against its included check digit (the last digit of the credit number). This number must follow these points:
1-	From the check digit (last one), and moving left, double the value of every second digit. The check digit is not doubled. The fist digit doubled is immediately to the left of the check digit. If the result of doubling is greater than 9, then add the digits of the result (e.g. 16 = 1 + 6 = 7).
2-	Take the sum of all the digits.
3-	If the total modulo is equal to 0, then the number is valid according to the Luhn formula, else it is not valid.
To calculate the vendor of a credit card, I have created a txt file (called iin.txt) where there is a list of vendors with its length of the credit card and their range of IIN numbers.
The calculate the last digit(checksum), the process is like the Luhn algorithm but not the same.
The process is:
1-	From the first digit, and moving right, double the value of every first digit.
2-	Take the sum of all digits
3-	The checksum digit is the total sum * 9 and then modulo 10

To generate a valid card number given a vendor, I follow these steps:
1-	Open the iin.txt file where vendor details are
2-	If the vendor does not exist, return error
If vendor exist, take the length of the number. If length is a range, generate a random number between that range. Same process for the IIN number.
Then, generate the remaining digits (length – 1(checknumber) – IIN number) randomly.
3-	Given the digits of the generated card, calculate the checksum number and add it
4-	Return the card number
