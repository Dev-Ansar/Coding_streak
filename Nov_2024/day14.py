'''
Given an array of integers, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.


Example:
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

Can you find a solution with a time complexity of O(n)?


'''


'''
Optimized Approach: Kadane's Algorithm
Kadane’s Algorithm works by iterating through the array and, at each step, keeping track of the maximum 
subarray sum that ends at the current index. If the current subarray sum becomes negative, 
it’s better to start a new subarray from the next index.
'''


# Here’s an optimized version of your solution using Kadane’s Algorithm:

def max_subarray_sum(arr):
    max_sum = curr_sum = arr[0]
    
    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)  # Decide whether to start a new subarray or continue with the existing one
        max_sum = max(max_sum, curr_sum)     # Update max_sum if the current subarray is larger
    
    return max_sum


# Example usage
input_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(input_arr)
print(result)


'''
Here are the key takeaways for today:

Kadane's Algorithm: It efficiently finds the maximum sum of a contiguous subarray in O(n) time, 
adjusting the start and end of the window dynamically based on the cumulative sum.

Window Functions: Typically used with fixed-size windows in tasks like calculating running totals or averages. 
Kadane’s algorithm doesn't use a fixed window size, so it's not a window function.

Sliding Window Technique: Useful for problems with fixed window sizes, 
where you slide the window across the array and compute results like sums, averages, or maximum values for each window.

Space Complexity in Kadane’s Algorithm: It operates in O(1) space, as it only tracks the 
current sum and maximum sum without creating new subarrays or structures.

These concepts help distinguish when to use dynamic windowing (like Kadane's) vs. fixed-size sliding windows 
in different problem scenarios.

'''
