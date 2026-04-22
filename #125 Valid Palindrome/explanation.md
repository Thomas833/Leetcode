using two pointers, i will walk from the beginning and the end of the string and meet in the middle, skipping over non-alphanumeric characters and when it is an alphanumeric character, making sure it's lowercase to do a proper comparison.

make two pointers, i and j. i will start at the beginning of the string and j will start at the end. they will walk towards each other and the loop will end when i >= j since this will mean that i and j are on the same space or they have compared every character.
