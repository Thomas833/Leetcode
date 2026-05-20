# #71 Simplify Path - Explanation

create list of dirs by walking through string
if dir is not .. or ., append to stack
if .. and stack not empty, pop from stack
iterate through stack and append to output and return