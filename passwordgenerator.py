#Random password generator

import random

capital_let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_let = 'abcdefghijklmnopqrstuvwxyz'
number = '1234567890'
special_char = '~`!@#$%^&*()[]{}|'

upper,lower,digit,odd = True,True,True,True

finalpass = ''

if upper:
    finalpass += capital_let
if lower:
    finalpass += small_let
if digit:
    finalpass += number
if odd:
    finalpass += special_char

lenght = 20
howmuch = 10

for x in range(howmuch):
    password = ''.join(random.sample(finalpass,lenght))
    print(password)