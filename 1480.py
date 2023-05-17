def runningSum(nums):
    array = []

    for idx, val in enumerate(nums):
        array.append(sum(nums[: idx + 1]))

    return array


# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]

nums1 = [3, 1, 2, 10, 1]
nums2 = [1, 1, 1, 1, 1]
nums3 = [1, 2, 3, 4]
print(runningSum(nums1))
