def maxProfit(prices) -> int:
    max_p = 0
    l, r = 0, 1

    while r < len(prices):
        if prices[l] > prices[r]:
            l = r
        else:
            curr_p = prices[r] - prices[l]
            max_p = max(curr_p, max_p)

        r += 1

    return max_p


prices = [2, 1, 2, 1, 0, 1, 2]
# prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
