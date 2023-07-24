def romanToInt(s: str) -> int:
    hmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    p = 0

    while p < len(s):
        if(p + 1) > len(s) -1:
            res = res + hmap[s[p]]
            break

        if  hmap[s[p]] >= hmap[s[p+1]]:
            res = res + hmap[s[p]]
        else:
            res = res - hmap[s[p]]

        p +=1

    return res

s = "LVIII"
romanToInt(s)
