p = {6,28,496,8128,33550336}
print(p)
print(type(p))
d={}
print(type(d))
e =set()
print(type(e))
s = set([2,4,16,64,4096,262144])
print(s)
s.add(24)
print(s)
k = {81, 108}
k.add(12)
k.update([37,128, 97])
print(k)
k.remove(97)
k.discard(98)
j = k.copy()
m = set(j)
print(m)

# set theory in algebra
blue_eyes= {'Olivia','Harry', 'Lily','Jack','Amelaia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry','Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood= {'Harry'}
ab_blood= {'Joshua', 'Lola'}
print(blue_eyes.union(blond_hair))
print(blond_hair.union(blue_eyes)) #all the elements that are in either or both
print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes)) # commutative
print(blue_eyes.intersection(blond_hair)) #only elements present in both sets
print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes)) # commutative
print(blond_hair.difference(blue_eyes)) # elements that are in first set and not in second set
print(blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair)) # non-commutative
print(blond_hair.symmetric_difference(blue_eyes)) #first set or the second set but not both
print(smell_hcn.issubset(blond_hair))
print(taste_ptc.issuperset(smell_hcn))
a_blood.isdisjoint(b_blood)