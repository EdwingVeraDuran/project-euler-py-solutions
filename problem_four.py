def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


max_palindrome: int = 0
a, b = 0, 0

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product: int = i * j
        if is_palindrome(product) and product > max_palindrome:
            max_palindrome = product
            a, b = i, j

print(
    f"Max palindromic number is: {max_palindrome} - The product numbers are: {a} - {b}"
)
