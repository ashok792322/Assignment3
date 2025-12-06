#Assignment 3
#Task 1: Calculate Factorial Using a Function
# Using Recursion
def factorial(num):
    fact=1
    if num==1:                   #Base condition
        return 1
    else:
        fact=num*factorial(num-1)  # Recursive condition
        return fact

#calling function
num=int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")