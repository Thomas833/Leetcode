def solution(nums1: list, m: int, nums2: list, n: int)->list:
    if m == 0:
        nums1 = nums2
        return nums1

    j = n-1
    i = m-1
    k = n+m-1

    while j > -1:
        if i < 0:
            nums1[k] = nums2[j]
            k-=1
            j-=1
            continue

        if not (i == 0 and j == 0):
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1 
        else:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                nums1[i] = nums2[j]
                j-=1
            else:
                nums1[k] = nums2[j]
                j-=1
    return nums1
    

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [4,5,6]
n = 3
print(solution(nums1, m, nums2, n))