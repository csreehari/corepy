print(range(5))              # range(stop)
for i in range(5):
    print(i)
    
print(list(range(5, 10)))    # range(start, stop)
print(list(range(10, 15)))
print(list(range(0, 10, 2))) # range(start, stop, step)

s= [0, 1, 4, 6, 13]
for v in s:
    print(v)
 
# enumerate -  constructs an iterable of (index, value) tuples around another iterable object
t = [6, 372, 8862, 14880, 2096886]
for v in enumerate(t):
    print(v)
 
for i, v in enumerate(t):
     print(f'i = {i}, v = {v}')

  