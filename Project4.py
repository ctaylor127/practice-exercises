#Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
# Author: Christian Taylor
# Project 4
import math

list1 = []
list2 = []
m=1
n=3

""" User input """
iter = int(input("Enter the number of iterations: "))

""" Positive List """
for x in range(1, iter+1, 2):
    pattern1 = (1/m)
    list1.append(pattern1)
    m += 4

""" Negitive List """
for y in range(1, iter, 2):
    pattern2 = (1/n) * (-1)
    list2.append(pattern2) 
    n += 4

"""Combine both lists into one list"""
comb = list1.extend(list2)

"""Sum all values in list"""
sum = sum(list1)

""" Multiply result by 4 """ 
pi = sum*4

""" Print result """ 
print("The resulting value is equal to: %0.10f" % pi)
