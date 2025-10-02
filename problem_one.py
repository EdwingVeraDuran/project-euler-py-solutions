numbers: list[int] = []

for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        numbers.append(n)

        print(f"Numero: {n} - Suma: {sum(numbers)}")
