from hog import *
dice = make_test_dice(3, 1, 5, 6)
averaged_roll_dice = make_averaged(roll_dice, 1000)
# Average of calling roll_dice 1000 times
# Enter a float (e.g. 1.0) instead of an integer
print(averaged_roll_dice(2, dice))