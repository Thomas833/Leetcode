I created two pointers that start at the beginning of the array.
Since j iterates everytime, I use it in the conditional to ensure we are not at the end of the array. 
I check if the number is in the hashmap. If it is not, add it to the hashmap and add a value of 1 to indicate we have only seen the element once. I also put the nums[j] element into tne nums[i] space. This does not do anything when i==j, but will move the first unique element to the proper spot when they are not equal. 
If the number is in the hashmap but has a frequency less than 2. I do this because when checking the second frequency of the number, the hashmap has not been updated yet, so it will be show one less than what we are looking at at the conditional. I increment inside the conditional and move the number to the i index. 

Whenever I move a number forward, I iterate i since that number is where it is supposed to be. 