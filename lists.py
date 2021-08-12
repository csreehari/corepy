r = [1, -4, 10, -16, 15]
print(r[-1])
print(r[-2])
print(f'{r[0]} {r[-0]}')

t = [6, 372, 8862, 14880, 2096886]
print(t[1:3]) # slice first and second
print(t[1:-1]) # slice skipping first and last
print(t[2:]) # slice from 2 onwards
print(t[:2]) # slice upto 2 but not including 2
print(t[:])
s=t
print(s is t)
r=t[:]
print(r is s) # reference equality vs 
print(r == s) # value equality
u = s.copy()
print(u is s)
v = list(s)
print(v) # these create shallow copies
a = [[1,2], [8,9]]
b=a[:]
print(a is b)
print(a[0])
print(b[0])
print(a[0] is b[0])
a[0] = [3,4]
print(a[0])
print(b[0])
a[1].append(5)
print(a[1])
print(b[1])
print(a)
print(b)

c = [21, 37]
d = c * 4
print(d)
print([0]*9)
print(37 in [4, 56, 37, 98])
print(78 not in [6, 78, 65, 23])