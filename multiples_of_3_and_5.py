'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''

# 1. generate the list
lst = list(range(1000))

# 2. find the sum (list comprehension)
sum_of_multiples = sum([el for el in lst if el % 3 == 0 or el % 5 == 0])

# 3. print
print(sum_of_multiples)
