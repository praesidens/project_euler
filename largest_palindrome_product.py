# coding=utf-8
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import time
a = time.clock()

minimum_product = 100 * 100
maximum_product = 999 * 999
largest_p = -1
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        # the product of two numbers
        p = i * j
        if largest_p < p and str(p) == str(p)[::-1]:
                largest_p = p
b = time.clock()
print(b - a)
print(largest_p)
