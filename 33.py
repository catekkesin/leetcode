# 7 8 9 1 2 3 4 5 6
# Save the first element for reference: a0 = 7.
# Take the middle element of the numsay (2).
# If it’s smaller than a0, then your pivot element is to the left.
# Else, it’s to the right. Repeat,
# and you will find the index of your pivot element in O(log n) time.

# Then, if the value you’re searching for is larger than a0,
# use binary search in the left part of the list (from 0 to pivot index).
#  Otherwise, the right side (from pivot index to end).


def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[mid] >= nums[l]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        # right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1


nums = [7, 8, 9, 1, 2, 3, 4, 5, 6]
print(binary_search(nums, 8))
