# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

import re


def find(exp):
    parsed = re.sub(r"[\s\W_]+", "", exp).lower()
    rev_parsed = parsed[::-1]
    return True if parsed == rev_parsed else False


s = "A man, a plan, a canal: Panama"
print(find(s))
