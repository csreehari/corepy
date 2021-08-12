print(len("oiuroiweurn983498kljkldfje"))
# use str.join() instead of concatenation as concatenation with + results in temporaries
# which results in consequent costs of memory, allocations and copies
colors = ';'.join(['#45ff23','#77ff23', '#1298a3'])
print(colors)
print(colors.split(';'))
print(''.join(['high', 'way', 'land']))
print("unforgetable".partition('forget'))
departure,separator,arrival = "London:Edinburgh".partition(':')
print(departure)
print(arrival)
origin, _, destination = "Seattle-Boston".partition('-')
print(origin)
print(destination)
print("{0}\xb0 north, {1}\xb0 east".format(59.7, 10.4))
print(('The age of {0} is {1}. {0}\'s birthday is on {2}').format('Fred', 24, 'October 31'))
print('Reticulating spline {} of {}.'.format(4, 23))
print('Current position {latitude} and {longitude}'.format(latitude ='60N', longitude = '5E'))
print('Galactic postion x={pos[0]}, y={pos[1]}, z={pos[2]}'.format(pos=(65.2, 23.1, 82.2)))

import math
print('Math constants: pi={m.pi}, e={m.e}'.format(m = math))
print('Math constants: pi={m.pi:.3f}, e={m.e:.3f}'.format(m = math))
value = 4*20
print(f'The value is {value}') # f-strings or string interpolation

import datetime
print(f'The current time is {datetime.datetime.now().isoformat()}')
print(f'Math constants: pi={math.pi}, e={math.e}')
print(f'Math constants: pi={math.pi:.3f}, e={math.e:.3f}')



