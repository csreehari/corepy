url = {
    'Google': 'https://www.google.com',
    'Pluralsight': 'https://www.pluralsight.com',
    'Sixty North': 'https://sixty-north.com',
    'Microsoft': 'https://microsoft.com'
}
print(url['Pluralsight'])
names_and_ages= [('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Sathyvardha', 21)]
d = dict(names_and_ages)
print(d)
phonetics = dict(a='alfa', b='bravo',c='charlie',d='delta')
print(phonetics)

d = dict(goldenrod=0xDAA520,indigo=0x4B0082,seashell=0xFFF5EE)
e = d.copy()
print(e)
f = dict(e)
print(f)
g = dict(wheat=0xF5DEB3, khaki=0xF0E68C, crimson = 0xDC143C)
f.update(g)
print(f)
stocks={'GOOG':891, 'AAPL': 416, 'IBM':194}
stocks.update({'GOOG':894, 'YHOO':25})
print(stocks)
print('GOOG' in stocks)
del stocks['IBM']
m = {'H': [1,2,3],
     'He': [3,4],
     'Li': [6,7],
     'Be': [7,9,10],
     'B': [10,11],
     'C': [11,12,13,14]}
m['H'] += [4,5,6,7]
print(m)
from pprint import pprint as pp
pp(m)
