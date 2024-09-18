# Recursion - Factorial Calculation (September 6, 2024)

'''
Problem:
Write a function to calculate the factorial of a number using recursion.

Details:
The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
It is denoted as n!.
For example, the factorial of 5 (5!) is 5 * 4 * 3 * 2 * 1 = 120.

'''

#Iterative approach

# def factorial_iterative(n: int) -> int:
#     # Check for invalid input
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
    
#     fact = 1
#     for i in range(n, 1, -1):
#         fact *= i
    
#     return fact

# # Input and validation
# try:
#     n = int(input('Please enter a non-negative integer to find its factorial: \n'))
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     result = factorial_iterative(n)
#     print(f"The factorial of {n} is {result}.")
# except ValueError as e:
#     print(e)


# Recursive approach

# def factorial_recursive(n: int) -> int:
#     # Check for invalid input
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     # Base case
#     if n <= 1:
#         return 1
#     # Recursive case
#     return n * factorial_recursive(n - 1)

# # Input and validation
# try:
#     n = int(input('Please enter a non-negative integer to find its factorial: \n'))
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     result = factorial_recursive(n)
#     print(f"The factorial of {n} is {result}.")
# except ValueError as e:
#     print(e)





'''
Key Takeaways from Today's Discussion:
Recursion Overview:
We started with the concept of recursion and tackled a problem to calculate the factorial of a 
number using both recursive and iterative approaches.

Factorial Problem Implementation:
You implemented the iterative approach for calculating the factorial.
We discussed adding input validation and handling edge cases (like factorial of 0) for both iterative and recursive solutions.

Clarification on the range() Function with n = 0:
You asked how the for loop in the iterative approach behaves when n = 0.
Explanation: The range(0, 1, -1) produces an empty sequence, so the loop doesn’t execute, 
and the function correctly returns 1 because the initial value of fact is 1.

Type Hints Explanation:
You inquired about the difference between defining functions with type hints (def factorial_iterative(n: int) -> int:) vs. without them.
Clarification: Type hints make your code more readable and easier to maintain by indicating the expected parameter types and return type. 
They also help with static analysis but are not enforced at runtime in Python.

Iterative vs. Recursive Approaches:
You asked which approach is more resource-intensive.
Clarification: The recursive approach is typically more resource-intensive due to higher memory usage (stack space) 
and function call overhead, while the iterative approach uses constant space and is generally more efficient.
'''



#Practice:
#Iterative:

def iterative_factorial(num):
    if num < 0:
        print('negative num not allowed')
        return
    else:
        fact = 1
        for i in range(num,1,-1):
            fact *= i
    return fact
        


input_num = int(input('Please enter a non neative number. \n'))

try:

    if input_num < 0:
        print('negative num not allowed')
    else:
        result = iterative_factorial(input_num)
        print(f"the factorial of the number: {input_num} is {result}")


except:
    print('eroror') 

