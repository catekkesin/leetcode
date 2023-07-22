s = "acb"
t = "ahbgdc"


def isSubsequence(s: str, t: str) -> bool:
    p1 = 0
    search = 0

    res = ""

    while p1 < len(s) and search < len(t):
        if s[p1] == t[search]:
            res += s[p1]
            p1 += 1
            search += 1

        else:
            search += 1

    return True if res == s else False


print(isSubsequence(s, t))
