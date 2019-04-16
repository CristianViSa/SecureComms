Lab 5 - RSA

Flag 1 -
For this exercise, i just used the python example from moodle.
Encrypt the message and then decrypt.

Flag 2-
Same as flag 1 but only decrypt the message using the RSA formula and the int2string() given method.

Flag 3 -
For this exercise we are given a privatekey file so i open it, i read it and then, using the library Cripto.PublicKey RSA i create a RSA object and then extract the values.

Flag 4 -
Using the same process as flag3, i create a RSA object, extract the values and then i used them to decrypt the message.

Flag 5 -
In this case we are given p, q, dp, dq, qinv and pinv. There is a way of calculating the message using dq and dp. The first step is calculate m1 and m2 (using dp and dq respectively). With that, we calculate h, which is h = (qinv * (m1-m2))%p.
Finally, the message is m = m2 + h*q. Last step is decrypt it and there it is.
Formulas extracted from https://en.wikipedia.org/wiki/RSA_(cryptosystem)

Flag 6 -
This time we have p, q, and e. We can calculate n (p x q).
We need to use the Extended Euclidean Algorithm for this exercise in order to calculate d which is the modular inverse of e modulus phi. We can calculate phi = (p-1)(q-1).
Once we have d, we use it to decrypt the ciphertext  --> decrypted = pow(ciphertext, d, n)

Flag 7 -
Is the same process as flag6, however, we only have n, no p and no q. We need to factorise n, for that, i used http://factordb.com/
Now we have p and q and we can calculate phi and so, d (modular inverse of e mod phi).
Then decrypt the message.

Flag 8 -
We only have n, e and ciphertext. Notice that e = 3, this gives us a hint that maybe M^e < n. If this, the message will be just the e-root of ciphertext.
Lets try this. I create a function that returns the nth-root of X and then use it to calculate e-root of ciphertext. Finaly i tried to decrpyt that value and it works.

Flag 9 -
We have 3 different encrypted text for the same message. Notice the e is the same and low value(3). This gives us a hint that may be the Low Public Exponent Attack. Lets try it. For this, we have to calculate the chinese remainder algorithm, so first of all, i create a function for that. Then, i calculate the CRT for [n1,n2,n3] and [c1,c2,c3]. That will result as the ciphertext, so then, to calculate the message, just calculate the e-root of that value(ciphertext) and you have the decrypted message.

Flag 10-
We have 2 different encrypted text for the same message,  but this time e is not the same, so its not as flag 9. I was searching for several attacks and trying them with no result, until i finally realize that e2 = 3, so maybe i could try the same as flag 8. Calculating the e2-root of c2 gave me the message, so i decrypted it and got the flag.

Flag 11 -

TBD

