# #49 Group Anagrams - Explanation

create an empty list and a hashmap
iterate through strs
    for each string, check if the sorted string is a key in the hashmap. 
    if not, add it as the key and the value will be the index in the output list that you add it to and append to output with a list containing your string.
    if it is in hashmap, append the string to the index, which is also a list, in output.
