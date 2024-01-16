"""
Write a Python function named case_counter that counts the number of uppercase and lowercase letters in a given string.

The function should calculate and return two numbers: the count of uppercase letters and the count of lowercase letters in the string.
If there are no letters of a particular case (uppercase or lowercase) in the string, the function should return 0 for that case.
Non-alphabetic characters in the string should be ignored and not counted.
"""

def case_counter(text):
   uppercase_letter = 0
   lowercase_letter = 0
   for letter in text:
     if letter.isupper():
       uppercase_letter += 1
     elif letter.islower():
       lowercase_letter += 1
   return uppercase_letter,lowercase_letter
pass
print(case_counter("Hello World"))
print(case_counter("PYTHON")) 
print(case_counter("python")) 
print(case_counter("1234!@#$"))



  













