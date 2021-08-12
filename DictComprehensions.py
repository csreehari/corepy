country_to_capital = {
    'United Kingdom': 'London',
    'Brazil': 'Brasilia',
    'Morocco': 'Rabat',
    'Sweden': 'Stockholm'
}
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
from pprint import pprint as pp
pp(capital_to_country)

# 
# {
#     key_expr(item): value_expr(item)
#     for item in iterable
# }

words = ['hi', 'hello', 'foxroot', 'hotel']
{ x[0]: x for x in words}

import os
import glob
file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
pp(file_sizes)