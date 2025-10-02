import math

number = 600851475143
n = number
max_prime = -1

while number % 2 == 0:
    max_prime = 2
    n //= 2

for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        max_prime = i
        n //= i

if n > 2:
    max_prime = n

print(max_prime)
