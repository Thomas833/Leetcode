the biggest part of this problem that needs explaining is the math i did

- numLen tells me how many digits my number is. 
- mod tells me how much to mod my number to return the number minus the largest value
- romanNum is the largest digit in the number
- reducedNum is the single digit value from the romanNum

with this information, i use conditionals to ensure i am adding the roman numerals properly to the string. 

this solution is not efficient. i could have literally had 10 if statements covering all of the cases for a number, i.e. is it greater than 1000/900/400/100/90/40/10/9/4 and done the proper modulus and num calculation to have it go from top to bottom in one pass, updating the number has it goes through the various conditionals. but, this aint bad.