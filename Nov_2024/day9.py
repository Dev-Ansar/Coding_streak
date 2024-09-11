'''
Topic: Arrays
Problem:
Find the First Unique Element in a List

Write a function to find the first unique element in a list of integers 
(i.e., the first element that appears exactly once). If there is no unique element, return '-1'.

Example:
Input: [9, 2, 3, 2, 6, 6]
Output: 9

Input: [1, 1, 1, 2, 2, 2]
Output: -1

Constraints:
The list will contain only integers.
The list will have at least one element.
'''


input_arr = [1, 1, 1, 2, 2, 2]

freq_dict = {}

for i in input_arr:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1

if (1 not in freq_dict.values()):
    print('-1')
else:
    for i,x in freq_dict.items():
        if (x == 1):
            print(i, " is the first unique element.")
            break



'''
Checking for Uniqueness:

Your approach correctly counts frequencies, but checking if 1 exists in freq_dict.values() is unnecessary. 
You could just traverse the list to find the first unique element in one go.

The check if (1 not in freq_dict.values()) could miss certain cases. For instance, even if there's a unique element, 
this check might not ensure it's the first.

'''

# Revised Code
# Here's an updated version of your code:

input_arr = [1, 1, 1, 2, 2, 2]
freq_dict = {}

# Count the frequencies
for i in input_arr:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1

# Find the first unique element
found = False
for i in input_arr:
    if freq_dict[i] == 1:
        print(i, "is the first unique element.")
        found = True
        break

if not found:
    print('-1')


# Key Improvements:
# Frequency Check in Original Order: Instead of checking freq_dict.values(), you directly traverse 
# the original list (input_arr) to ensure you find the first unique element.

# Handling No Unique Element: Added a flag (found) to handle cases where no unique element exists and print -1 at the 
# end if none is found.

'''
Key Takeaways:
Efficient Frequency Counting: Using a dictionary to count frequencies is optimal for this kind of problem.

Order Matters: To find the first unique element, always iterate the original array after building the frequency dictionary
[Note: i was iterating over the dictionary which is not wrong as even the dic maintains the input order but its much straight forward to se the list itself.].
'''