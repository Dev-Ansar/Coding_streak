'''
Topic: Dictionaries
Problem:
Find the Most Frequent Element in a List

Write a function that finds the most frequent element in a list of integers. If there are multiple elements with the same highest frequency, return the smallest one.

Example:
Input: [4, 6, 2, 6, 2, 2, 5, 6]
Output: 2

Input: [1, 3, 1, 3, 1, 3, 4]
Output: 1

Constraints:
The list will contain only integers.
The list will have at least one element.


important questions to ask for clarity before starting the coding:

Input Constraints:
Is the list guaranteed to have at least one element?

Element Types:
Will the list contain only integers, or can there be other types of elements?

Multiple Most Frequent Elements:
If there are multiple elements with the same highest frequency, should we return the smallest one?

Performance Constraints:
Are there any specific performance constraints or limits on the size of the list?
'''

input_list = [4, 6, 2, 6, 2, 2, 5, 6]
freq_dict = {}
for i in input_list:
    if i in (freq_dict.keys()):
        freq_dict[i] = freq_dict[i] + 1

    else:
        freq_dict[i] = 1    

min_element = 0
current_max_freq = 0
for i,x in freq_dict.items():
    # print(i, ' -> ',x)
    if (x > current_max_freq):
        current_max_freq= x
        min_element = i
    elif (x == current_max_freq):
        if(min_element >= i):
            min_element = i
    


print(min_element, " -> ", current_max_freq)


'''
Feedback

1) Dictionary Key Check:
You can simplify the check for whether the key exists in the dictionary using in operator directly without .keys()
example:
if i in freq_dict:


2) Variable Initialization:

Initialize min_element with None and update its value accordingly. 
This avoids confusion with a default value like 0 which could be a valid list element.
example: 
min_element = None


'''

# Revised Code
# Here's an updated version of your solution with these improvements:

input_list = [4, 6, 2, 6, 2, 2, 5, 6]
freq_dict = {}

# Count frequencies
for i in input_list:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1

# Find the most frequent element
min_element = None
current_max_freq = 0
for i, x in freq_dict.items():
    if x > current_max_freq:
        current_max_freq = x
        min_element = i
    elif x == current_max_freq:
        if min_element is None or i < min_element:
            min_element = i

print(min_element)


'''
Key Takeaways:
Using in Operator: Directly check if the key exists in the dictionary.
Handling Ties: Ensure min_element is correctly updated if there’s a tie in frequency.
Initialization: Initialize variables to handle cases when the list might be empty or contain edge values.
'''