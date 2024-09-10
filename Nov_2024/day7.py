'''
Topic: Strings
Problem:
Check if Two Strings are Anagrams

Write a function to determine if two strings are anagrams of each other. 
An anagram is a word or phrase formed by rearranging the letters of another, typically using all the original letters exactly once.

Example:
Input: s1 = "listen", s2 = "silent"
Output: True

Input: s1 = "hello", s2 = "world"
Output: False

Constraints:
The strings s1 and s2 will only contain lowercase alphabets.
The strings must have the same length to be anagrams.

'''

s1 = "bad"
s2 = "dab"

if(len(s1) != len(s2)):
    print('input strings are not anagrams')
else:
    s11 = sorted(s1)
    s22 = sorted(s2)
    if(s11 == s22):
        print('yes they are anagrams')
    else:
        print('2. input strings are not anagrams')


'''
Feedback
Solution Explanation:
Length Check:
First, you check if the two strings are of equal length. If they aren’t, they can’t be anagrams.

Sorting Strings:
You then sort both strings, which arranges the characters in lexicographical order (alphabetical).
If the sorted strings are identical, the original strings are anagrams.

Comparison:
If the sorted versions of both strings are the same, they are anagrams.

Code review:
Efficiency: Sorting takes O(n log n) time, where n is the length of the string. 
This is good for small strings, but we can explore alternative methods to achieve better performance in certain scenarios.
'''

# Alternative Approach: Frequency Count
# Instead of sorting, you can count the frequency of each character in both strings and compare the frequency counts. 
# This approach runs in O(n) time.

from collections import Counter

def are_anagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    
    return Counter(s1) == Counter(s2)

s1 = "bad"
s2 = "dab"
if are_anagrams(s1, s2):
    print("Yes, they are anagrams")
else:
    print("No, they are not anagrams")


'''

Key Takeaways from Today's Problem:
Problem Understanding:
Task: Determine if two given strings are anagrams of each other.
Definition: An anagram is a rearrangement of letters from one string to form another string, using all the original letters exactly once.

Solution Approaches:
Sorting Approach:
Method: Sort both strings and compare them.
Time Complexity: O(n log n) due to sorting.
Space Complexity: O(n) for storing the sorted strings.

Frequency Count Approach:
Method: Use Counter from the collections module to count character frequencies and compare the counts.
Time Complexity: O(n), where n is the length of the strings.
Space Complexity: O(1) for fixed character sets, since the number of unique characters is bounded (e.g., 26 lowercase letters).

Clarifications:
Space Complexity:
Fixed Character Set (e.g., lowercase alphabets): O(1), since the number of unique characters is constant.
Alphanumeric Characters: O(n), where n is the number of unique characters.

Input Size:
Small Fixed Set: Space remains constant.
Variable Set: Space complexity can grow linearly with the number of unique elements.

Efficiency Considerations:
Sorting: Simple and easy but not the most efficient for large datasets.
Frequency Counting: More efficient and scalable, especially for larger inputs with a fixed character set.

Practical Tips:
Choose the Approach: Depending on the problem constraints, select the most efficient method for both time and space complexity.
Handling Different Character Sets: Consider the space complexity implications based on the variety of characters in the input.

'''