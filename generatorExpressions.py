from filteringComprehensions import is_prime

million_Squares = (x*x for x in range(1, 1000001))
print(million_Squares)
print(list(million_Squares)[-10:])
print(sum(x*x for x in range(1, 1000001)))

print(sum(x for x in range(1001) if is_prime(x)))