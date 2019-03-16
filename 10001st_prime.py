'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

counter = 0
primes = []
for i in range (2, 1000000):
    prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            prime = False
            break
    if prime:
        counter += 1
        primes.append(i)
    if counter == 10001: break
print(primes)
print(primes[-1])
