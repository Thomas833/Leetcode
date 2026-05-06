# #290 Word Pattern - Explanation

will use two hashmaps to store the letter to the word and the word to the letter so i can perform checks if they are pointed to each other. iterate through string until you find space, perform checks on word in windowm, checking various states (letter not in map but word is, word not in map but letter is, word and letter in map but dont match). make sure to account for word at end of string that will not have space to account for to create word.
