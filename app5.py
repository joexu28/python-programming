import converters
from converters import lbs_to_kg
from converters import kg_to_lbs
import utils
import ecommerce.shipping
from ecommerce.shipping import calc_shipping
import random

print(lbs_to_kg(180))
print(kg_to_lbs(100))
print(converters.kg_to_lbs(70))
print(converters.lbs_to_kg(160))

numbers = [2, 5, 1, 10, 30, 2]
print(utils.find_max(numbers))

ecommerce.shipping.calc_shipping()

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

members = ['john', 'jay', 'guy', 'someone']
print(random.choice(members))


class Dice:
    def roll(self):
        result = (random.randint(1, 6), random.randint(1, 6))
        return result


dice = Dice()
print(dice.roll())