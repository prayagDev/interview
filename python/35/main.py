nums = [1, 2, 3, 4, 5, 6]

evens = filter(lambda x: x%2 == 0, nums)

squares = map(lambda x: x**2, evens)

print(squares)

