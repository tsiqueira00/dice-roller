## I'm going to 'roll' a dice multiple times and then represent in a histogram how many times each side was chosen.

import random
import pygal

class Dice():
    def __init__(self, sides=6):
        self.sides = sides
        self.each_side = ['1', '2', '3', '4', '5', '6']
        self.random_sides = []
        self.side_frequency = []

    def rolling(self):
        while len(self.random_sides) < 50:
            rnd_numbers = str(random.randint(1, self.sides))
            self.random_sides.append(rnd_numbers)

dice = Dice()
dice.rolling()

for number in dice.each_side:
    if number in dice.random_sides:
        counting = dice.random_sides.count(number)
        dice.side_frequency.append(counting)

################ CREATING THE HISTOGRAM ###################

bar = pygal.Bar()

bar.title = 'Rolling a 6-side dice and representing each side frequency'
bar.x_labels = dice.each_side
bar.x_title = 'Sides'
bar.y_title = 'Frequencies'
bar.add('D6', dice.side_frequency)

bar.render_to_file('dice_roller.svg')







