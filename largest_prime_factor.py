'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

def find_lpf(number):
    # the minimal pf is 2
    i = 2
    while number > 1:
        if number % i == 0:
            number /= i
            i -= 1
        i += 1
    return i


number = 600851475143
print(find_lpf(number))
