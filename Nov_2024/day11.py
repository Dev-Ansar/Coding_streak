'''
Longest Substring Without Repeating Characters
Problem: Given a string s, find the length of the longest substring without repeating characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.


Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols, and spaces.



Question for Clarification:
Does the input string contain spaces or special characters, or should we only consider alphanumeric characters?



'''
#my solution
def find_longest_Substring(input_str):
    output_str = ""
    curr_str = ""
    seen = set()

    for s in input_str:
        
        if s in seen:
            if (len(curr_str)>len(output_str)):
                output_str = curr_str
                curr_str = s
            
            
        else:
            seen.add(s)
            curr_str = curr_str + s


    return output_str

# Example usage
input_str = "pwwkew"

result = find_longest_Substring(input_str)
print(result)

'''
Feedback:
Your solution is on the right track, but there are a couple of issues:

Handling repeated characters: When encountering a repeated character, you reset the current substring (curr_str) to just that character. This can lead to missed substrings. You need to slide the window forward from the point of repetition instead of starting over.

Maintaining the set: You're adding characters to the seen set but never removing them when moving past a repeated character.


'''

#Here's an updated approach using a sliding window technique that fixes these issues:

def find_longest_Substring(input_str):
    seen = set()  # To track characters in the current window
    left = 0  # Left pointer of the sliding window
    max_len = 0  # Max length of substring
    output_str = ""  # Longest substring without repeating characters

    for right in range(len(input_str)):
        while input_str[right] in seen:  # If the character is already in the set, move the left pointer
            seen.remove(input_str[left])
            left += 1

        seen.add(input_str[right])

        # Check if current substring is longer than previous ones
        if right - left + 1 > max_len:
            max_len = right - left + 1
            output_str = input_str[left:right + 1]

    return output_str

# Example usage
input_str = "pwwkew"
result = find_longest_Substring(input_str)
print(result)  # Expected Output: "wke"


'''
Key Changes:
Sliding Window: We move the left pointer to skip characters until the repeated character is excluded from the current window.
Update the longest substring: We continuously check and update the longest substring whenever we find a longer one.
Efficiency: This method runs in O(n) time due to sliding window and set operations.
'''



'''
Key Takeaways:

Problem: Find the longest substring without repeating characters.
Sliding Window: Two pointers (left, right) dynamically adjust the window size to exclude repeated characters.
Set Usage: Track unique characters in the current window with a set.
Efficiency: Time complexity is O(n), as we make only one pass through the string.
Window Adjustment: Move the left pointer when a repeated character is found, ensuring valid substrings only.

'''