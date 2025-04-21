# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random 

for _ in range(3):
    print(random.randint(1,6),random.randint(1,6))


