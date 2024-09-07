'''
Topic: Arrays
Problem:
Find the Maximum Product of Two Elements in an Array

Given an integer array nums, find the maximum product of two distinct elements in the array. 
Return the product of the two largest numbers, minus 1 for each of the numbers.

example:
Input: nums = [3, 4, 5, 2]
Output: 12
Explanation: The maximum product is (5 - 1) * (4 - 1) = 4 * 3 = 12.

Constraints:
The array will contain at least two elements.
The elements in the array will be non-negative integers.


'''

'''
Before jumping into coding during an interview, 
it's important to clarify certain aspects of the problem to ensure you fully understand the requirements and edge cases.

1. Clarify Input Constraints:
    What are the size constraints of the array?

    Can the array contain duplicates?

    Will the array always contain at least two elements?

2. What is the range of the elements in the array?
    Example: "Are the elements always non-negative integers?"

3. Are there any time complexity constraints?
Example: "Is there a preferred time complexity for this problem, or should I focus on the most optimal solution?"

"Should I focus on making the solution as efficient as possible, or is a correct brute-force solution acceptable?"



'''

#my approach
# nums = [4,6,1,20,30,7]

# nums.sort(reverse=True)

# product = (nums[0] - 1) * (nums[1] - 1)

# print(product)


'''
Feedback

Improvements:
Time Complexity:
Sorting the array takes O(nlogn), which is fine for small arrays, but for larger arrays, 
you can improve the efficiency by finding the two largest elements in linear time O(n) without sorting the entire array.

Space Complexity:
Sorting modifies the input array in place, which is acceptable. However, if you want to avoid modifying the original array, 
you could copy it first or use a more efficient algorithm.

Optimized Approach without Sorting:
To make your code more efficient, you can find the two largest elements in a single pass through the array without sorting.

'''

def max_product(nums):
    max1, max2 = 0, 0
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return (max1 - 1) * (max2 - 1)

nums = [4, 6, 1, 20, 30, 7, 30]
result = max_product(nums)
print(result)


'''
Time Complexity:
The optimized approach runs in O(n) time because it only requires a single pass through the array.
'''