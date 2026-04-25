from collections import defaultdict, Counter

def findSubstr(s: str, words: list) -> list:
    if not s or not words:
        return []

    k = len(words[0])
    m = len(words)
    target = Counter(words)
    res = []

    # try every offset
    for offset in range(k):
        window = defaultdict(int)
        start = offset
        count = 0

        # step through in word-sized jumps
        for j in range(offset, len(s) - k + 1, k):
            word = s[j:j + k]

            if word in target:
                window[word] += 1
                count += 1

                # shrink if too many of this word
                while window[word] > target[word]:
                    left_word = s[start:start + k]
                    window[left_word] -= 1
                    start += k
                    count -= 1

                # valid match found
                if count == m:
                    res.append(start)

            else:
                # reset everything
                window.clear()
                count = 0
                start = j + k

    return res


print(findSubstr("xbarfoofoobarthefoobarman", ["bar","foo","the"]))