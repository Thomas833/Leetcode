# #128 Longest Consecutive Sequence - Explanation

ASSUMING DUPLICATE INTS COUNT AS ONE IN THE SEQUENCE

brute force:
    - sort list
    - iterate through list. i = 0,j=1,prevNum = nums[i]
        - if prevNum + 1 != nums[j]
            - i=j
        - prevNum = nums[j]
        - j++
    return j-i

[-10,5,-2,1,4,-9,3,2]
sorted:
[-10,-9,-2,1,2,3,4,5]

Time complexity O(nlogn) due to sorting list. wont work for problem since it has to be O(n)

efficient method:
- iterate through list and store each number in hashmap
- iterate through hashmap, :
    - curNum = key
    - if curNum + 1 in hashmap, curNum = key+1, count ++
    - else, count = 0
-return count


Is if n-1 not in numSet: needed in my loop to keep O(n)? Can I have duplicatous checks?
Yes — the if n-1 not in numSet check is necessary to guarantee O(n).

Your old solution is not O(n) in the worst case.

Consider this input:

[1,2,3,4,5]

Your old solution does:

From 1:

2? yes
3? yes
4? yes
5? yes

4 checks.

From 2:

3? yes
4? yes
5? yes

3 checks.

From 3:

4? yes
5? yes

2 checks.

From 4:

5? yes

1 check.

Total:

4 + 3 + 2 + 1 = O(n²)

More generally:

(n-1) + (n-2) + ... + 1

which equals:

n(n-1)/2

and that simplifies to:

O(n²)

The check:

if n-1 not in numSet:

fixes this because you ONLY start counting from the beginning of a sequence.

So for:

1,2,3,4,5

only 1 starts the walk.

2, 3, 4, and 5 get skipped.

Now each number is effectively visited a constant number of times overall, making the algorithm O(n).