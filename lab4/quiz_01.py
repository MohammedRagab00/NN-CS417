# List comprehension
squares = [x ** 2 for x in range(1, 4)]
print("squares = ", squares)  # [1, 4, 9]

a = list(range(10, 21))
print("a = ", a)

even = [x for x in a if x % 2 == 0]  # even elements of a
print("even = ", even)

evenIndices = [x for i, x in enumerate(a) if i % 2 == 0]  # elements at even indices in a
print("even indices = ", evenIndices)
