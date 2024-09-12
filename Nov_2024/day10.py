'''
Topic: Arrays
Problem:
Find All Pairs with a Given Sum

Write a function that finds all unique pairs in a list of integers that add up to a given target sum. 
Each pair should be returned as a tuple (a, b) such that a <= b. The output should not contain duplicate pairs.

Example:
Input: nums = [2, 4, 3, 5, 7, 8, 9], target = 10
Output: [(2, 8), (3, 7)]

Constraints:
The list will contain only integers.
The list can have both positive and negative integers.
The function should return unique pairs only.

'''

input_arr = [2, 4, 3, 5, 7, 8, 9]
target = 10
output_arr = []

target_pair_dict = {}
input_arr.sort()

for i in input_arr:
    current_complement = target - i 
    if(current_complement !=i and current_complement in input_arr):
        if(current_complement not in target_pair_dict):
            target_pair_dict[i] = current_complement
            target_pair_dict[current_complement] = 0


    
    
for i,x in target_pair_dict.items():
    if (x !=0 ):
        op_tuple = (i,x)
        output_arr.append(op_tuple)

print(target_pair_dict)
print("\nresult\n")
print(output_arr)


'''
Feedback on Your Code:
Duplicate Pair Handling:
- You're using a dictionary to track the pairs, which works, but the logic could be simplified. 
Also, storing both i and current_complement as keys in the dictionary adds some redundancy.
- Since you're using a sorted list, you can avoid having to check target_pair_dict this way.

Efficiency:
Sorting the input list increases the time complexity to O(n log n). 
While sorting helps in avoiding duplicate pairs, there’s a more efficient way using a set that would allow you 
to maintain O(n) time complexity without sorting.

'''
# Revised Solution:
def find_pairs(nums, target):
    output_arr = []
    seen = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            # Ensure (a, b) is always (smaller, larger)
            output_arr.append((min(num, complement), max(num, complement)))
        seen.add(num)

    return output_arr

# Example usage
input_arr = [2, 4, 3, 5, 7, 8, 9]
target = 10
result = find_pairs(input_arr, target)
print(result)



'''
Explanation:
Set for Tracking: We use a set called seen to keep track of the numbers we've already encountered.

Unique Pairs: As we traverse the list, for each number num, we calculate its complement (target - num). 
If this complement has already been seen, we know they form a valid pair.

Ordered Pair: We ensure each pair is returned as (smaller, larger) using min() and max() 
to avoid duplicate pairs like (3, 7) and (7, 3).
'''

# Key Points:
# Efficiency: The revised solution runs in O(n) time because sets have constant-time lookups.
# Simplicity: We avoid needing to sort the list, and there's no need to check both directions of a pair, thanks to the set-based lookup.

#bonus point
'''
In Python, both sets and dictionaries provide constant-time lookups on average, meaning the time it takes to find or check for an element in a set or dictionary is O(1).

Why Constant-Time Lookups?
Hashing: Both sets and dictionaries in Python use a data structure called a hash table. 
Each element in a set (or key in a dictionary) is assigned a unique "hash" (a number computed from the element's value). 
Using this hash, Python can directly jump to the correct location in memory without having to search through all the elements. 
This results in a lookup time of O(1) on average.
'''