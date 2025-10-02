sum_of_squares: int = 0
square_of_sum: int = 0

for i in range(1, 101):
    sum_of_squares += i**2
    square_of_sum += i

square_of_sum = square_of_sum**2

difference: int = square_of_sum - sum_of_squares

print(f"Difference: {square_of_sum} - {sum_of_squares}: {difference}")
