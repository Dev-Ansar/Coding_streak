'''
Problem: Move Zeroes
Description: Given an array nums, write a function that moves all 0s to the end of it while maintaining the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.

Example:
Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

'''

input_arr = [0, 1, 0, 3, 12] 

curr_ptr = 0
zero_ptr = 0
non_zero_ptr = 0
while (curr_ptr < len(input_arr)):
    if(input_arr[zero_ptr] != 0 and input_arr[curr_ptr] == 0):
        #print('it came here zero')
        zero_ptr = curr_ptr
    elif(input_arr[non_zero_ptr] == 0 and input_arr[curr_ptr]!= 0):
        #print('it came here non zero')
        non_zero_ptr = curr_ptr

    if (input_arr[zero_ptr] == 0 and input_arr[non_zero_ptr] != 0):
        print('it came here')
        input_arr[zero_ptr], input_arr[non_zero_ptr] = input_arr[non_zero_ptr], input_arr[zero_ptr]
        
    else:
        print('increment')
        curr_ptr +=1
print(input_arr)

