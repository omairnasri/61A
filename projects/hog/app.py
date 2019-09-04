import hog
always_one = hog.make_test_dice(1)
always_two = hog.make_test_dice(2)
always_three = hog.make_test_dice(3)
always = hog.always_roll
# example 1
s0, s1 = hog.play(lambda score, other: (score + 3) // 4 * 2 + 3, 
				  lambda score, other: 4 - other // 4 * 2, score0=0, score1=0, goal=10, dice=always_one)

# Error: expected
#     9
# but got
#     8