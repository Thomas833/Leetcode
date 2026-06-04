def solution(s1: str, s2: str) -> bool:
    # check if lengths are 1 or less apart
    if (abs(len(s1) - len(s2)) > 1): 
        return False
    elif len(s1) + len(s2) <= 1:
        return True
    
    diff = 0
    i = 0
    j = 0
    while i != len(s1) and j != len(s2):
        if len(s1) != len(s2):
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                if len(s1) > len(s2) and s1[i+1] == s2[j]:
                    i += 1 
                elif len(s1) < len(s2) and s1[i] == s2[j+1]:
                    j += 1
                else:
                    i += 1
                    j += 1
                diff += 1
        else:
            if s1[i] != s2[i]:
                diff += 1
            i += 1
    return True if diff <= 1 else False

print(solution("ab", "ba"))            # False
print(solution("abc", "acb"))          # False
print(solution("abcdef", "abcfde"))    # False
print(solution("pale", "pael"))        # False
print(solution("abcde", "abXcYe"))     # False
print(solution("abc", "axbc"))         # True
print(solution("abc", "abXc"))         # False
print(solution("abcdef", "abcxyz"))    # False
print(solution("abcd", "abdc"))         # False
print(solution("abc", "a"))           # False
