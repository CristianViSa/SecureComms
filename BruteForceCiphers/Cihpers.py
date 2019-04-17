def caesar(text, shift):
   if shift > 26 or shift < 0:
      return "Shift must be a number between 0 and 26 included"
   else:
      message = ""
      # transverse the plain text
      for i in range(len(text)):
         char = text[i]
         # Decrypt uppercase characters in plain text
         if (char.isupper()):
            message = message + chr((ord(char) - shift - 65) % 26 + 65)
         # Decrypt lowercase characters in plain text
         elif(char.islower()):
            message = message + chr((ord(char) - shift - 97) % 26 + 97)
         # If it is not a letter, put the char
         else:
            message = message + char
      return message
def rot47(text):
   message = ""
   for i in range(len(text)):
      charnum = ord(text[i])
      #If the char is on the correct range of characters (Letter upper or lower, puntuation sign or number)
      if charnum >= 33 and charnum <= 126:
         message = message + chr(33 + ((charnum + 14) % 94))
      else:
         message = message + text[i]
   return message


  
def atbash(text): 
   #The substitution table for every letter, upper and lower case
   substitution_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V', 
                        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q', 
                        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 
                        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 
                        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A',
                        'a' : 'z', 'b' : 'y', 'c' : 'x', 'd' : 'w', 'e' : 'v', 
                        'f' : 'u', 'g' : 't', 'h' : 's', 'i' : 'r', 'j' : 'q', 
                        'k' : 'p', 'l' : 'o', 'm' : 'n', 'n' : 'm', 'o' : 'l', 
                        'p' : 'k', 'q' : 'j', 'r' : 'i', 's' : 'h', 't' : 'g', 
                        'u' : 'f', 'v' : 'e', 'w' : 'd', 'x' : 'c', 'y' : 'b', 'z' : 'a'
                        } 
   message = '' 
   for char in text: 
      #If the char is a letter, put its corresponding substitution letter
      if(char != ' '):
         message = message + substitution_table[char] 
      else: 
         #If not, put the char without substitution(has to be a space)
         message = message + char
   return message 
def kamasutra(text, alphabet):
   #Alphabet has to be an even number in order to make translations, if not, error
   if((len(alphabet) %2) == 0):
      message = ""
      #Everything to upper to avoid confusion between upper and lowercases during translation
      text = text.upper()
      alphabet = alphabet.upper()
      #Separate the alphabet in 2 parts, to create the translation table
      first_half = list(alphabet[:len(alphabet)//2])
      second_half = list(alphabet[(len(alphabet)//2):])
      #Create the substitution table, the first with format {first_half:second_half} and the second {second_half:first_half} 
      substitution_table1 = dict(zip(first_half, second_half))
      substitution_table2 = dict(zip(second_half, first_half))
      
      message = ""
      for char in text:
         #If char is on substitution_table1, tranlsate
         if substitution_table1.get(char):
            message = message + substitution_table1.get(char)

         #If char is on substitution_table2, tranlsate
         elif substitution_table2.get(char):
            message = message + substitution_table2.get(char)

         #If char is not on any table (a space), put the char
         else:
            message = message + char
      return message  
   else:
      return "Wrong substitution table entered"

if __name__ == "__main__":
   noStop = 1
   while noStop:
      print ("--- Brute Force Decipher")
      print("1 - Caesar Cipher")
      print("2 - Rot47 Cipher")
      print("3 - Atbash Cipher")
      print("4 - Kamasutra Cipher")
      print("5 - Exit")
      option = input("Select an option ")
      if option == "1":
         cipher = input("Enter the cipher text : ")
         shift = int(input("Enter the shift : "))
         print(caesar(cipher, shift))
      elif option == "2":
         cipher = input("Enter the cipher text : ")
         print(rot47(cipher))
      elif option == "3":
         cipher = input("Enter the cipher text : ")
         print(atbash(cipher))
      elif option == "4":
         cipher = input("Enter the cipher text : ")
         alphabet = input("Enter the alphabet : ")
         print(kamasutra(cipher, alphabet))
      if (option == "5"):
         noStop = 0  