# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


def logest_sub_string(string):
    left = 0
    max_len = 0
    seen ={}
    for right , ch in enumerate(string):
        if ch in seen and left <= seen[ch]:
            left = seen[ch]  + 1
        seen[ch]=right
        max_len = max(max_len,right - left + 1)
    print(max_len)
    return max_len
s = "abcabcbb"
logest_sub_string(s)
    