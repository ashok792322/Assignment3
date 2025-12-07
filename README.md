# ASSIGNMENT 3:
# Module 4: Functions & Modules in Python 
# Task 1: Calculate Factorial Using a Function 

Recursion is a process in which a function call itself till a certain condition is not met.
Mathematically Factorial of a number n => n\*(n-1)\*(n-2)\*...............2\*1 and is represented by n!
Example:
5!=5\*4\*3\*2\*1 =120
It is achieved in code by recursive condition num*factorial(num-1)


### def factorial(num):
 User defined factorial() created using key word def with single argument num which will receive input  through calling function factorial(num) .

 ### fact=1
Variable fact with initial value 1  will receive  

 ### if num==1:                                
if statement contain Base condition num==1 

 ### return 1
once condition reached base condition num==1  value 1 return  to calling function 

 ### else:
if base condition mentioned in if statement False then enter else block

 ### fact=num\*factorial(num-1)
 else block start contain Recursive condition 
 Mathematical num*(num-1)!, this (num-1)! achieved by calling the same function again by factorial(num-1)

 ### return fact
part of else block  return evaluated value of fact to  previous calling function factorial(num-1)

## calling function
### num=int(input("Enter a number: "))
input()  typecast to integer for  interactively received integer value from user and assigned to variable num.

### print(f"Factorial of {num} is: {factorial(num)}")
calculated result is displayed by print() using fstring  for strings for understanding for respected value of input variable {num} and calling function {factorial(num)} . 


## Working:

### Starts from value num=5
when we call factorial(5)  . num=5   check  condition if num==1 i.e 5==1 becomes false ,So not go to if block or enter else block.

### Inside else block.
num\*factorial(num-1)  5\*factorial(5-1) call the same function again, that means factorial(5) calling factorial(4)
factorial(num) itself calling its own function again and  again.
factorial(5)  calling 5\*factorial(4)
factorial(4)  calling 4\*factorial(3)
factorial(3)  calling 3\*factorial(2)
factorial(2)  calling 2\*factorial(1) - when factorial(1) is called  num=1 check condition if num==1 i.e 1==1 becomes True.
 
So enter if block  and return 1 to calling function  factorial(1). 2\*factorial(1) replaced  by 2\*1 and stored in variable  fact.

 fact value 2 return to  factorial(2) as this calculation evaluation done by  3\*fact_rec(2) . So 3\*2=6 stored in fact

 fact value 6 return to  factorial(3) as this calculation evaluation done by  4\*fact_rec(3) . So 4\*6=24 stored in fact

 fact value 24 return to  factorial(4) as this calculation evaluation done by  5\*fact_rec(3) . So 5\*24=120 stored in fact

fact value 120 return  to first function call  i.e print(factorial(5)) that's why 120 gets printed.


None of these calculation happens until all the function are called and reached the base condition i.e. if block num==1.

First it call all the function one by one till base condition num==1 is reached. Then in reverse direction start returning all the values. <br><br><br><br>


# Assignment3 

## Task 2: Using the Math Module for Calculations
 
### Problem Statement: Write a Python program that:
### 1. Asks the user for a number as input.
### 2. Uses the math module to calculate the:

### \*   Square root of the number
### \*   Natural logarithm (log base e) of the number
### \*   Sine of the number (in radians)
### \*  Displays the calculated results.<br><br><br>


### import math
math module imported in order to utilize function for calculating square root, log, sine

### def cal(num) 
 User defined cal() created with single argument num which will receive input  through calling function cal(n) 

### square_root = math.sqrt(num)
under cal()   square root of number is calculated by sqrt() available in math module which is called by math.sqrt(num) and calculated value is assigned to variable square_root.

### logarithm =  math.log(num)
under cal()   log of number is calculated by log() available in math module which is called by math.log(num) and calculated value is assigned to variable logarithm.

### sin = math.sine(num)
under cal()   sine of number is calculated by sine() available in math module  which is called by math.sine(num) and calculated value is assigned to variable sine.

###  print(f"Square root: {square_root}")
  ### print(f"Logarithm: {logarithm}")
  ### print(f"sine:{sin}")
calculated result is displayed by print() using fstring  for strings for understanding for respected calculated  value  by calling variable inside {} . 

### n=int(input("Enter a number:"))
input() for  interactively received value from user and assigned to variable n.

cal(n)
 cal() called with value through variable  n which is assigned  value through input().
