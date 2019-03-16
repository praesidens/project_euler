'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import time

a = time.clock()

sum_of_primes = 2

for i in range (3, 2000000, 2):
    #prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
         sum_of_primes += i

b = time.clock()
print(b - a)
print(sum_of_primes)

