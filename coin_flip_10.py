# simple coin flip game: flip 10 times and report the results

import random

# 1- set up a data structure - here: tuple (for never-changing constants)
coin_possibles = ("heads", "tails")
heads_count = 0
tails_count = 0
range_obj = range(1, 11)

# print(type(coin_possibles)) # DS debug

for flip in range_obj:
    flip_result = random.choice(coin_possibles)
    if flip_result == 'heads':
        heads_count += 1
    else:
        tails_count += 1
    # print(f'the latest was: {flip_result}')
print(
    f'After {len(range_obj)} flips, there were {heads_count} heads and {tails_count} tails')
