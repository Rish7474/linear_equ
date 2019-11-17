#System of Linear Equation Solver
import math    

str_f1 = input("Enter the first linear function in terms of variable 'x' -> ")
str_f2 = input("Enter the second linear function in terms of variable 'x' -> ")

f1 = lambda x: eval(str_f1)
f2 = lambda x: eval(str_f2)

f1_yint = f1(0)
f2_yint = f2(0)
f1_slope = f1(1)-f1_yint
f2_slope = f2(1)-f2_yint

print(f1_yint)
