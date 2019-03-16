'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import time
a = time.clock()

for i in range(2520, 100000000000, 20):
    if i % 19 == 0 and i % 17 == 0 \
    and i % 18 == 0 and i % 14 == 0 \
    and i % 16 == 0 and i % 11 == 0 \
    and i % 13 == 0:
        print(i)
        break;
b = time.clock()
print(b-a)
