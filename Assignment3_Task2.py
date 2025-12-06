#Assignment3
#Task 2: Using the Math Module for Calculations
#   Uses the math module to calculate the:
#   Square root of the number
#   Natural logarithm (log base e) of the n
#   Sine of the number (in radians)

import math

def cal(num):
  square_root = math.sqrt(num)
  logarithm =  math.log(num)
  sin = math.sin(num)
  print(f"Square root: {square_root}")
  print(f"Logarithm: {logarithm}")
  print(f"sine:{sin}")

#calling function
n=int(input("Enter a number:"))
cal(n)


