# read this to learn  more about merge sort: https://www.w3schools.com/dsa/dsa_algo_mergesort.php

def merge(left: list, right: list)-> list:
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def mergeSort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    leftSorted = mergeSort(left)
    rightSorted = mergeSort(right)

    return merge(leftSorted, rightSorted)


unsorted = [1,6,3,7,8,4,2,0,9,7]
print(mergeSort(unsorted))