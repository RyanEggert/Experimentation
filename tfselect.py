from __future__ import print_function

from random import randint
from collections import Counter
from decimal import *

getcontext().prec = 8
print ("Preparing to select class")

NumSim = 500000

ClassSelectorScreen = {1: 'Scout', 2: 'Soldier', 3:'Pyro', 4:'Demoman', 5:'Heavy', 6:'Engineer', 7:'Medic', 8: 'Sniper', 9: 'Spy'}
pass
d = []
for x in xrange(1,NumSim):
    number = randint(1,9)
    d.append(number)

Data = Counter(d)
Mode, Number = Data.most_common()[0]

print(Data.most_common())
YourClass = ClassSelectorScreen[Mode]
Advantage = Decimal(Number) - (Decimal(NumSim)/ Decimal(9))
AdvantagePercent = Advantage/(Decimal(NumSim)/Decimal(100))

print()
print("You should be a " + YourClass)
print("Your class has an extra " + str(AdvantagePercent) + "% advantage over the other classes")