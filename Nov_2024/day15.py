'''
Problem: Move Zeroes
Description: Given an array nums, write a function that moves all 0s to the end of it while maintaining the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.

Example:
Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

'''

def moveZeroes(nums):
    nonZeroIndex = 0  # Pointer to place the next non-zero element
    
    # Step 1: Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nonZeroIndex] = nums[i]
            nonZeroIndex += 1
    
    # Step 2: Fill the remaining array with 0s
    for i in range(nonZeroIndex, len(nums)):
        nums[i] = 0

# Example usage
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
