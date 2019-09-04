import hog
always_three = hog.make_test_dice(3)
always_seven = hog.make_test_dice(7)
#
# Use strategies
# We recommend working this out turn-by-turn on a piece of paper.
# Error: expected
#     108
# but got
#     81

strat0 = lambda score, opponent: opponent % 10
strat1 = lambda score, opponent: max((score // 10) - 4, 0)
s0, s1 = hog.play(strat0, strat1, score0=71, score1=80, dice=always_seven, feral_hogs=False)

