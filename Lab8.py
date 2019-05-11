# Course Name: CS2302
# Author: Olugbenga Iyiola ID:80638542
# Assignment 8
# Instructor: Olac Fuentes
# T.A.: Nath Anindita / Maliheh Zargaran
# Date of last modification: 05/10/2019
# Purpose of program: Binary Search Trees

# importing all modules needed to run the program
import random
from mpmath import *
import numpy as np
from math import *
import math

# This method compares if 2 functions are equal
def equal(f1, f2,tries=1000,tolerance=0.0001):
    for i in range(tries):
        t = random.uniform(-math.pi, math.pi) # randomly generating numbers between -pi and +pi
        y1 = eval(f1)  # evaluates the passed string as a Python expression and returns the result
        y2 = eval(f2)  # evaluates the passed string as a Python expression and returns the result
        if np.abs(y1-y2)>tolerance:
            return False
    return True

# This method checks if there is partition of a list i.e S1 and S2 are a partition of S if and only
# if S1∪S2 = S and S1∩S2 = {}
def SubsetSum(S, leftList, rightList, checkList):
    leftSum = sum(leftList) # summation of left list
    rightSum = sum(rightList) # summation of right list
    concatenateList = leftList + rightList  # joining left and right list

    if leftSum == rightSum:  # checking if summation of left list = summation of right list
        print('Goal: ', leftSum)
        return True, leftList, rightList  # returning result

    if leftSum > rightSum and concatenateList not in checkList:
        removing = min(leftList) # minimum element of the bigger list
        leftList.remove(removing) # arbitrarily removing the minimum element of the bigger list
        rightList.append(removing) # appending the minimum element of the bigger list to the smaller list
        checkList.append(concatenateList)
        result, leftList, rightList = SubsetSum(S,leftList,rightList, checkList) # Backtracking
        return result, leftList, rightList

    if rightSum > leftSum and concatenateList not in checkList:
        removing = min(rightList) # minimum element of the bigger list
        rightList.remove(removing) # arbitrarily removing the minimum element of the bigger list
        leftList.append(removing) # appending the minimum element of the bigger list to the smaller list
        checkList.append(concatenateList)
        result, leftList, rightList = SubsetSum(S, leftList, rightList, checkList) # Backtracking
        return result, leftList, rightList

    return False, leftList, rightList



functions= ['sin(t)','cos(t)','tan(t)','mp.sec(t)','-sin(t)','-cos(t)','-tan(t)','sin(-t)','cos(-t)','tan(-t)','sin(t)/cos(t)','2*sin(t/2)*cos(t/2)','sin(t)*sin(t)','1-(cos(t)*(cos)(t))','(cos(2*t))/2','1/(cos(t))']
for i in range(len(functions)):
    for j in range(len(functions)):
        print(functions[i],' is equals to ',functions[j], ': ',equal(functions[i],functions[j]))

print()
print('******************************************')
print('******************************************')
S = [1,2,5,4,11,8,9,6]
boolResult,left, right = SubsetSum(S,S[0:len(S)//2],S[len(S)//2 : len(S)],[])
print('Original List: ', S)
if boolResult:
    print('Partition/Solution:',left, right)
else:
    print('There is no solution')