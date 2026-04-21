def solution(s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        
        charRow = [""]*numRows
        currRow = 0
        iterator = 1
        for char in s:
            charRow[currRow] += char
            if currRow == numRows - 1:
                iterator = -1
            if currRow == 0 and iterator == -1:
                iterator = 1
            currRow += iterator
        
        return ''.join(charRow)
print(solution("PAYPALISHIRING", 3))