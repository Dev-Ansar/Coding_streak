'''
Topic: Strings - Palindrome Check

Problem:
Write a function to check if a given string is a palindrome. 
A string is considered a palindrome if it reads the same forwards and backwards, ignoring spaces, punctuation, and capitalization.

Example:
Input: "A man, a plan, a canal: Panama"  
Output: True  

Input: "race a car"  
Output: False

'''

input_str = "A man, a plan, a canal: Panama"
input_str = input_str.replace(" ","")
input_str = input_str.replace(",","")
input_str = input_str.replace(":","").lower()
print(input_str)


if (input_str == input_str[::-1]):
    print("yes they are palindrome")


'''
Feedback
Points to Consider:
Efficiency: Instead of calling .replace() multiple times, a more efficient way is to filter out all 
non-alphanumeric characters in one pass using a list comprehension or filter().
Clarification: Your current solution correctly checks if the string is a palindrome by comparing it to its reverse ([::-1]).
'''

#Suggested Improvement:

def is_palindrome(input_str):
    # Filter only alphanumeric characters and convert to lowercase
    filtered_str = ''.join(char.lower() for char in input_str if char.isalnum())
    
    # Check if the filtered string is a palindrome
    return filtered_str == filtered_str[::-1]

# Example usage
input_str = "A man, a plan, a canal: Panama"
if is_palindrome(input_str):
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")


'''
Performance Consideration:

Time Complexity: O(n), since we traverse the string twice (once to filter, once to check).
Space Complexity: O(n), for storing the filtered string.
'''

#Asked question: is it the most optimized approach to find palindrome and whats filtered_str[::-1] approach called?

'''
Answer:
1) The approach you've used is quite efficient for checking whether a string is a palindrome. Here's why:

Time Complexity: The solution traverses the string twice—once to filter out non-alphanumeric characters, and once 
to check the palindrome condition by comparing it with its reverse ([::-1]). This makes the time complexity O(n), 
where n is the length of the string.

Space Complexity: You're creating a filtered version of the string, so the space complexity is O(n) due to storing the filtered string.

While this is efficient, you can avoid reversing the string to slightly improve space complexity. Instead of creating a reversed copy, 
you can compare characters from the start and end of the string, which gives you O(1) space complexity if you use 
two pointers (one at the beginning and one at the end).


2) What is [::-1] called?
The [::-1] notation is a slice operation in Python and is called string reversal. The general syntax for slicing is:
[start:end:step]

Default behavior in slicing:
Start (first value): If omitted, it defaults to the beginning of the sequence (index 0).
End (second value): If omitted, it defaults to the end of the sequence (last index + 1).
Step (third value): If the step is negative (-1), it means Python moves from right to left.

In [::-1], the -1 step tells Python to move backward, starting from the end (last character) 
and going back to the first character. The default values for start and stop cover the whole string.

'''

#Two Pointer approach
def is_palindrome(input_str):
    left, right = 0, len(input_str) - 1
    
    while left < right:
        # Ignore non-alphanumeric characters
        while left < right and not input_str[left].isalnum():
            left += 1
        while left < right and not input_str[right].isalnum():
            right -= 1
        
        # Check if characters at left and right are the same (ignoring case)
        if input_str[left].lower() != input_str[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# Example usage
input_str = "A man, a plan, a canal: Panama"
if is_palindrome(input_str):
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")


'''
Key takeaway for today
Here are today's key takeaways:
Handling Non-Alphanumerics: Use isalnum() to ignore spaces, punctuation, and special characters efficiently.

Palindrome Definition: A string that reads the same backward as forward, ignoring spaces and special characters.

String slicing with [::-1] creates a new reversed sequence, leading to O(n) space complexity.

The two-pointer approach operates directly on the original sequence, requiring only constant space (O(1)), as no new sequence is created.

Slicing logic: Slicing creates a new sequence by iterating over the original in a specified range. When using [::-1], 
it iterates from the end of the sequence to the beginning, creating a reversed copy.

The two-pointer method is more space-efficient compared to slicing, especially when space is a concern in palindrome checking or similar problems
'''