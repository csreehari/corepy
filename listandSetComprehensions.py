words = "Why sometimes I have believed as many as six impossible things beforoe breakfast".split()
print([len(word) for word in words])
# [expr(item) for item in iterable]

lengths = []
for word in words:
    lengths.append(len(word))
    
from math import factorial
f = [len(str(factorial(x))) for x in range(20)]
print(f)

s = {len(str(factorial(x))) for x in range(20)}
print(s)