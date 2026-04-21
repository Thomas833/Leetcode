the key to this is to use a counter that increases until you reach numRows, at which point it will decrease to 0 and switch back to incrementing.

create a string array of length numRows. as you walk along the string, the char will go in the index that corresponds to the counter. after this loop, join all the strings. this takes n time as well. 