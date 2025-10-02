a, b = 1, 2
sum: int = 0

while a <= 4000000:
    if a % 2 == 0:
        sum += a
        print(f"Number: {a} - Sum: {sum}")

    a, b = b, a + b

    print(f"Suma: {sum}")
