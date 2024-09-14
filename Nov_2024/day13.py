'''
Topic: Arrays

Problem: Merge Two Sorted Arrays

You are given two sorted arrays arr1 and arr2 of sizes m and n, respectively. 
Write a function to merge these two arrays into one sorted array. The resulting array should also be sorted.

example:
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

output: [1, 2, 3, 4, 5, 6, 7, 8]

'''

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
final_arr = [0] * (len(arr1) + len(arr2))  # Final array initialized with the correct size

arr1_ptr = 0
arr2_ptr = 0
i = 0

# Merging both arrays until one is fully traversed
while arr1_ptr < len(arr1) and arr2_ptr < len(arr2):
    if arr1[arr1_ptr] <= arr2[arr2_ptr]:
        final_arr[i] = arr1[arr1_ptr]
        arr1_ptr += 1
    else:
        final_arr[i] = arr2[arr2_ptr]
        arr2_ptr += 1
    i += 1

# Add remaining elements of arr1 if any
while arr1_ptr < len(arr1):
    final_arr[i] = arr1[arr1_ptr]
    arr1_ptr += 1
    i += 1

# Add remaining elements of arr2 if any
while arr2_ptr < len(arr2):
    final_arr[i] = arr2[arr2_ptr]
    arr2_ptr += 1
    i += 1

print(final_arr)


#You could also use an empty list and append elements as you go, which simplifies things a bit:

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
final_arr = []  # Start with an empty list

arr1_ptr = 0
arr2_ptr = 0

# Merging both arrays until one is fully traversed
while arr1_ptr < len(arr1) and arr2_ptr < len(arr2):
    if arr1[arr1_ptr] <= arr2[arr2_ptr]:
        final_arr.append(arr1[arr1_ptr])
        arr1_ptr += 1
    else:
        final_arr.append(arr2[arr2_ptr])
        arr2_ptr += 1

# Add remaining elements of arr1 if any
while arr1_ptr < len(arr1):
    final_arr.append(arr1[arr1_ptr])
    arr1_ptr += 1

# Add remaining elements of arr2 if any
while arr2_ptr < len(arr2):
    final_arr.append(arr2[arr2_ptr])
    arr2_ptr += 1

print(final_arr)


'''
Key takeaways


Here are today's key takeaways:

Merging two sorted arrays: You can use a two-pointer approach to efficiently merge two sorted arrays into one without extra sorting.

Handling list size: Pre-allocating a list with a known size using [0] * size allows you to assign values via indexing, 
while using an empty list with .append() dynamically grows the list.

Pre-allocation vs. append: Pre-allocation can improve performance slightly by avoiding the overhead of dynamic list resizing, 
but .append() is simpler and works well when the final size is unknown or if you prefer flexibility.

Indexing vs. append: Indexing into a pre-allocated list requires the list to already have the needed size, 
while .append() is useful when you're building a list dynamically, as it adjusts the size automatically.

Question about duplicates: Always clarify if duplicates are allowed in the arrays before starting your solution, 
as it can impact your approach or result.
'''
