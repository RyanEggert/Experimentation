# Itertools Library Tests
"""Playing with the itertools library. Nested for-loop alternative? Sounds interesting"""

import itertools

output = itertools.product(range(1,100), range(1,10), range(1,10))

for comb in output:
	x,y,z = comb
	Sum = x + y + z 
	print Sum, ":", comb

