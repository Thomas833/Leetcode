will use 3 pointers and walk backwards on both arrays. 

j = last value in nums2
i = last value in nums1 before 0s
k = last value in nums1 (len(i)-1)

iterate until j < 0

need to account for when i < 0 before j and when j < 0 before i