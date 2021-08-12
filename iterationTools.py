from filteringComprehensions import is_prime
from itertools import islice, count
thousand_primes = islice(( x for x in count() if is_prime(x)), 1000)
print(list(thousand_primes)[-10:])

print(sum(islice((x for x in count() if is_prime(x)), 1000)))

print(any(is_prime(x) for x in range(1328, 1361)))

print(all(name == name.title() for name in ['London', 'Paris', 'Tokyo', 'New York']))

