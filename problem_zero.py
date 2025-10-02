sum: int = 0

for n in range(1, 661001):
    square_number = n**2

    if square_number % 2 != 0:
        sum += square_number

    print(f"Number: {n} - Square number: {square_number} - Total sum: {sum}")
