


'''
Problem Statement:
The Fibonacci numbers, commonly denoted F(n) form a sequence,
called the Fibonacci sequence, such that each number is the
sum of the two preceding ones, starting from 0 and 1. That is,


1   1   2   3   5   8   13  21  34  : Fibonacci series
1   2   3   4   5   6   7   8   9   : Fibonacci number correspoind to the fib series
'''


#Approach one: Using Recursion
#Time complexity: Omega(2^[n/2]). Big-oh(2^n)
#Space complexity: O(n) : Heigh of stack at max can be n bcoz
                 # it goes like this 5->4->3->2->1
def fibonacci_number(num):
    if num == 1 or num == 2:
        return 1
    
    #Recursively call fibonacci_number function
    return fibonacci_number(num - 1) + fibonacci_number(num - 2)

print(fibonacci_number(8))




#Approach one: Using Iteration
#Time complexity: O(n)
#Space complexity: O(1)
def fib_number(num):

    #First and second number of fib series
    first_num, second_num = 1, 1

    #Running loop from 2, bcoz we want nth number of fib series but we already
    #have first 2 numbers as 1 and 1
    for _ in range(2, num):
        third_num = first_num + second_num

        first_num = second_num #Now second number becomes first
        second_num = third_num #And third number becomes second number

    return third_num #Return required number



print(fib_number(10))

