Brute Force Ciphers -

This python script can decode in 4 different ciphers:

1 - Caesar cipher

Given a cipher text, and a shift, this algorithm moves every letter of the cipher text the number of shift positions in the ASCII code. For example, if shift is 3, a character with code 29 would be now 26.
This algorithm distinguise between upper and lowercase.

2- Rot47

Is the same procedure as caesar cipher, but in this case, the charset includes puntuation symbols and numbers, not only letters as the caesar cipher. The shift in this one is 47.

3 - Atbash

This cipher is a substitution cipher. So, first of all, i create a substitution table, for every letter(lower and upper) create its substitution character. This cipher inverts the alphabet.

4 - Kamasutra
Given a cipher text and an alphabet,  substitute every letter of the first half of the alphabet for its corresponding letter in the second half. The alphabet has to be even lenghted, so it contains pairs of letters only.
