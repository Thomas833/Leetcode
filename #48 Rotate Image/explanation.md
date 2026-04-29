A simple trick to rotating matrices 90 degrees is by reversing the order of the elements (the lists) in the greater list and then swapping values at i,j with j,i

dont forget to do i+1 in the inner loop when determing what j will start at to prevent doing nothing. if you just swap i,j with j,i, then youll not change anything. 
(no reverse method)
[5, 1, 9, 11]      [5, 1, 9, 11]
[2, 4, 8, 10]      [2, 4, 8, 10]
[13, 3, 6, 7]      [13, 3, 6, 7]
[15, 14, 12, 16]   [15, 14, 12, 16]

(with reverse method. you redo the reverse method)
[1, 2, 3]   [7, 8, 9]
[4, 5, 6]   [4, 5, 6]
[7, 8, 9]   [1, 2, 3]

