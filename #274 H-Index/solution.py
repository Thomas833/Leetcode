def hIndex(citations: list[int]) -> int:
    n = len(citations)
    bucket = [0] * (n + 1)

    for c in citations:
        if c >= n:
            bucket[n] += 1
        else:
            bucket[c] += 1

    count = 0
    print(bucket)
    for i in range(n, -1, -1):
        count += bucket[i]
        if count >= i:
            return i

    return 0
        
print(hIndex([1,4,1]))
# [4,4,2,1,0]
# # of papers with >= # of citations
# []