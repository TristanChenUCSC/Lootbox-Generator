import random

# PARAMETERS:
# Rarity - int representing the tier of the lootbox. Has to be atleast 1
# Size - int that determines total loot. Has to be atleast 1
def generate(rarity, size):
    output = f"Tier {rarity} Size {size} box: "
    items_dict = {}
    box_tier = rarity
    items_dict[box_tier + 1] = 0
    items_dict[box_tier] = 0
    if (box_tier - 1 > 0):
        items_dict[box_tier - 1] = 0
    if (box_tier - 2 > 0):
        items_dict[box_tier - 2] = 0

    total_items = random.randint(2 * size, 4 * size)
    guaranteed_num_of_matching_rarity = size

    # Tiers 1 and 2 are unique cases
    if box_tier == 1:
        items_dict[box_tier] += guaranteed_num_of_matching_rarity
        num_items = guaranteed_num_of_matching_rarity
        while num_items < total_items:
            if random.randint(1,100) <= 25:
                items_dict[box_tier + 1] += 1
                num_items += 1
            else:
                items_dict[box_tier] += 1
                num_items += 1

    elif box_tier == 2:
        items_dict[box_tier] += guaranteed_num_of_matching_rarity
        num_items = guaranteed_num_of_matching_rarity
        while num_items < total_items:
            random_num = random.randint(1,100)
            if random_num <= 10:
                items_dict[box_tier + 1] += 1
                num_items += 1
            elif random_num <= 50:
                items_dict[box_tier] += 1
                num_items += 1
            else:
                items_dict[box_tier - 1] += 1
                num_items += 1

    else:
        items_dict[box_tier] += guaranteed_num_of_matching_rarity
        num_items = guaranteed_num_of_matching_rarity
        while num_items < total_items:
            random_num = random.randint(1,100)
            if random_num <= 5:
                items_dict[box_tier + 1] += 1
                num_items += 1
            elif random_num <= 45:
                items_dict[box_tier] += 1
                num_items += 1
            elif random_num <= 90:
                items_dict[box_tier - 1] += 1
                num_items += 1
            else:
                items_dict[box_tier - 2] += 1
                num_items += 1

    for key, value in items_dict.items():
        if value > 0:
            output += f"\n{value} item(s) of 'Tier{key}' Rarity"

    return output

'''
for i in range(20): # generate 20 outputs
    rarity = random.randint(1, 20)
    size = random.randint(1, 20)
    print(generate(rarity, size))
    print("\n")
'''
YOUR_RARITY = 6 # Tier of the lootbox, can be any number that's 1 or higher
YOUR_SIZE = 15 # Size of the lootbox, can be any number that's 1 or higher
print(generate(YOUR_RARITY, YOUR_SIZE))