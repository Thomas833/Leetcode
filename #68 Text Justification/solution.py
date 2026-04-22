def textJustification(words: list[str], maxWidth: int) -> list[str]:
    output = []
    charCount = 0
    rowArr = []
    i = 0

    while i < len(words):
        if charCount + len(rowArr) + len(words[i]) <= maxWidth:
            rowArr.append(words[i])
            charCount += len(words[i])
        else:
            if len(rowArr) == 1:
                output.append(rowArr[0] + ((maxWidth - len(rowArr[0])) * " "))
            else:
                spw, ros = divmod(maxWidth - charCount, len(rowArr) - 1)
                for j in range(ros):
                    rowArr[j] += " "
                output.append((spw * " ").join(rowArr))
            
            rowArr = [words[i]]
            charCount = len(words[i])

        i += 1

    if rowArr:
        last_line = " ".join(rowArr)
        last_line += " " * (maxWidth - len(last_line))
        output.append(last_line)

    return output

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(textJustification(words, maxWidth))