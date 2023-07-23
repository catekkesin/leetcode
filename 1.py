def twoSum(nums, target: int):
    h_map = {}
    n = len(nums)

    for i in range(n):
        h_map[nums[i]] = i

    for i in range(n):
        comp = target - nums[i]
        if comp in h_map and h_map[comp] != i:
            return (i, h_map[comp])

    return []


nums = [3, 2, 4]
target = 6

twoSum(nums, target)
