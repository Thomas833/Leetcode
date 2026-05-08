def solution(n: int)->bool:
    hashmap = {}
    while True:
        total = 0
        while n > 0:
            rdigit = n % 10
            n = n // 10
            total += rdigit**2
        if total == 1:
            return True
        else:
            n = total
            if n in hashmap:
                return False
            else:
                hashmap[n] = 1


n = 11
print(solution(n))


# fast solution from leetcode uses fast slow pointer to track cycles
def isHappy(n: int) -> bool:
        def next(n) -> int:
            total = 0
            while n:
                digit = n%10
                total += digit*digit
                n //= 10
            
            return total
        
        fast = slow = n

        while True:
            slow = next(slow)
            fast = next(next(fast))

            if fast == 1:
                return True
            if slow == fast:
                return False
        return False
