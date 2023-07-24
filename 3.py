def lengthOfLongestSubstring(s: str) -> int:
    res = ""

    n = len(s)

    for i in range(n):
        curr = ""

        for j in range(i, n):
            if s[j] not in curr:
                curr = curr + s[j]
            elif s[j] in curr and len(curr) > len(res):
                res = curr

    print(res)


s = "pwwkew"
lengthOfLongestSubstring(s)
