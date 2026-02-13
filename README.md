# Lootbox Generator

## What the tool generates

This generator creates lootbox results based on customizable parameters. Given a lootbox tier, size, and luck value, the generator simulates how many items drop and what rarity tiers those items belong to. The output is returned as structured JSON data that can be used for loot systems in games.

**Some Example Usages:**
- Since the generator is a python function, you could integrate it directly in your own game to generate output for your own lootbox system.
- You could batch generate a bunch of lootboxes onto the JSON and have your in-game lootbox output one of those results from the data.

## How to run the tool

To get started on generating lootbox results, either clone or download the repository. Then, in lootbox.py, simply adjust the customizable knobs based on your needs. These knobs/parameters can be found at the bottom of the file under a section titled "USER INPUT." After that, just run the python file lootbox.py and that's it! Your output can be found in the JSON file and you may use that data however you like.

## Parameters

### Rarity

**Input:** Can be any positive integer (1 or greater).

**Surface Level Explanation:** This knob determines the base rarity of the lootbox. The base rarity controls the tiers of items that can potentially drop.

**Detailed Explanation:** The base rarity of the lootbox controls the range of tiers for the potential items. With the exception of tiers 1 and 2, the lootbox tier will always output items between the range of 1 tier above the base rarity and 2 tiers below it. For example, a Tier 5 lootbox can only output items of Tiers 6, 5, 4, and 3. It will never be able to drop a tier 7+ item or an item of tier 2 or below. This tier range system works similarly for base rarities 1 and 2, but since there aren't sufficient tiers below 1 and 2, the ranges are smaller. What this means is that a Tier 1 lootbox can only drop items of tiers 2 and 1, and a Tier 2 lootbox can only drop items of tiers 3, 2, and 1.

**Additional Note:** The reason why the lootbox and item rarities are represented with numeric tiers is so that the tool remains flexible and can be adapted to the user's own rarity system. For example, the user can simply treat "Tier 3" as Epic, "Tier 4" as Legendary and so on depending on their project's rarity system.

### Size

**Input:** Can be any positive integer (1 or greater).

**Surface Level Explanation:** This knob determines about how many total items to output. The higher the size, the more items that can potentially drop.

**Detailed Explanation:** The size of the lootbox controls minimum and maximum total items that can be dropped from the lootbox. The exact calculations goes as follows:
- Minimum: 2 * size
- Maximum (rounded to nearest int): 2 * size + 2 * sqrt(size)

One last important thing about the size parameter is that in addition to controlling the total items, it also guarantees a minimum number of items that match the lootbox's base rarity. What this means is that a Tier 5 box of size 8 will ALWAYS drop atleast 8 tier 5 items. A tier 3 box of size 1 will ALWAYS drop atleast 1 item that's tier 3, and so on. This is a safety rule that prevents potential players from opening a high tier box like a tier 7 just to find ZERO tier 7 items in it.

### Luck

**Input:** Any float between 0 and 1. (0 is default, 1 is maximum luck)

**Surface Level Explanation:** This knob skews the drop rates towards the highest tier. A luck of 0 results in the default drop rates while higher values will result in an increased drop rate for the highest item tier. A luck of 1 will result in a 100% drop rate for the highest tier.

**Detailed Explanation:** The default drop rates of items goes as follows:
- 1 Tier above base tier: 5%
- Base tier: 40%
- 1 Tier below base tier: 45%
- 2 Tiers below base tier: 10%

The Luck knob skews these probabilities towards the highest tier (1 Tier above base tier) meaning a high value like 0.8 will drastically increase the drop rate for the highest tier while lowering the drop rates for the others.

**Additional Note:** The purpose of this knob is to allow more flexibility over the drop rates, in case the user is not satisfied with the default rates. Finding the perfect luck value may take some time, so feel free to explore different values to find the drop rates that work best for you.

### Count / Batch size

**Input:** Can be any positive integer (1 or greater).

**Explanation:** Use this parameter for batch generation (i.e. how many lootboxes do you want to generate onto the JSON file?).

## Example Outputs
Here are 20 example outputs:

[

    {
        "box_tier": 4,
        "size": 3,
        "luck": 0.2,
        "total_items": 9,
        "loot": {
            "Tier 4": 5,
            "Tier 3": 4
        }
    },
    {
        "box_tier": 4,
        "size": 3,
        "luck": 0.2,
        "total_items": 6,
        "loot": {
            "Tier 4": 5,
            "Tier 2": 1
        }
    },
    {
        "box_tier": 4,
        "size": 3,
        "luck": 0.2,
        "total_items": 9,
        "loot": {
            "Tier 5": 2,
            "Tier 4": 5,
            "Tier 3": 2
        }
    }
]

[

    {
        "box_tier": 2,
        "size": 1,
        "luck": 0,
        "total_items": 3,
        "loot": {
            "Tier 3": 1,
            "Tier 2": 1,
            "Tier 1": 1
        }
    },
    {
        "box_tier": 2,
        "size": 1,
        "luck": 0,
        "total_items": 2,
        "loot": {
            "Tier 2": 1,
            "Tier 1": 1
        }
    }
]

[

    {
        "box_tier": 6,
        "size": 10,
        "luck": 0.5,
        "total_items": 23,
        "loot": {
            "Tier 7": 6,
            "Tier 6": 13,
            "Tier 5": 3,
            "Tier 4": 1
        }
    },
    {
        "box_tier": 6,
        "size": 10,
        "luck": 0.5,
        "total_items": 26,
        "loot": {
            "Tier 7": 10,
            "Tier 6": 13,
            "Tier 5": 2,
            "Tier 4": 1
        }
    },
    {
        "box_tier": 6,
        "size": 10,
        "luck": 0.5,
        "total_items": 21,
        "loot": {
            "Tier 7": 4,
            "Tier 6": 13,
            "Tier 5": 2,
            "Tier 4": 2
        }
    }
]

[

    {
        "box_tier": 67,
        "size": 6767,
        "luck": 1,
        "total_items": 13593,
        "loot": {
            "Tier 68": 6826,
            "Tier 67": 6767
        }
    }
]

[

    {
        "box_tier": 7,
        "size": 20,
        "luck": 1,
        "total_items": 46,
        "loot": {
            "Tier 8": 26,
            "Tier 7": 20
        }
    },
    {
        "box_tier": 7,
        "size": 20,
        "luck": 1,
        "total_items": 44,
        "loot": {
            "Tier 8": 24,
            "Tier 7": 20
        }
    },
    {
        "box_tier": 7,
        "size": 20,
        "luck": 1,
        "total_items": 40,
        "loot": {
            "Tier 8": 20,
            "Tier 7": 20
        }
    },
    {
        "box_tier": 7,
        "size": 20,
        "luck": 1,
        "total_items": 46,
        "loot": {
            "Tier 8": 26,
            "Tier 7": 20
        }
    }
]

[

    {
        "box_tier": 15,
        "size": 100,
        "luck": 0.1,
        "total_items": 203,
        "loot": {
            "Tier 16": 18,
            "Tier 15": 128,
            "Tier 14": 42,
            "Tier 13": 15
        }
    },
    {
        "box_tier": 15,
        "size": 100,
        "luck": 0.1,
        "total_items": 213,
        "loot": {
            "Tier 16": 13,
            "Tier 15": 142,
            "Tier 14": 43,
            "Tier 13": 15
        }
    },
    {
        "box_tier": 15,
        "size": 100,
        "luck": 0.1,
        "total_items": 217,
        "loot": {
            "Tier 16": 19,
            "Tier 15": 142,
            "Tier 14": 40,
            "Tier 13": 16
        }
    }
]

[

    {
        "box_tier": 10,
        "size": 200,
        "luck": 0.8,
        "total_items": 408,
        "loot": {
            "Tier 11": 164,
            "Tier 10": 219,
            "Tier 9": 23,
            "Tier 8": 2
        }
    },
    {
        "box_tier": 10,
        "size": 200,
        "luck": 0.8,
        "total_items": 407,
        "loot": {
            "Tier 11": 173,
            "Tier 10": 215,
            "Tier 9": 18,
            "Tier 8": 1
        }
    },
    {
        "box_tier": 10,
        "size": 200,
        "luck": 0.8,
        "total_items": 428,
        "loot": {
            "Tier 11": 179,
            "Tier 10": 220,
            "Tier 9": 26,
            "Tier 8": 3
        }
    }
]

[

    {
        "box_tier": 123456,
        "size": 123456,
        "luck": 0.123456,
        "total_items": 247502,
        "loot": {
            "Tier 123457": 20731,
            "Tier 123456": 166712,
            "Tier 123455": 49185,
            "Tier 123454": 10874
        }
    }
]

## Known Limitations

The tool breaks when the parameters are given unsuitable values. For example, the generator will fail if the rarity is 0 or a negative number. Also avoid using sizes that are too high (like 1 billion) because the generator might take too long to run and fail.

## Notes from Playtesting/Feedback
1. Tester: Stanley Hung
- Suggested a new parameter to change the range of tiers, allow users to change the stuff that can be obtained more freely
Confused about the size at first, thinks the range is a bit awkward

2. Tester: Anish
- Redocument generator to be more clear to new users

3. Tester: Edison Chan
- The mechanics are incredibly interesting, but I think the fact that they’re all abstracted by only two knobs means that there's a lot of potential versatility it's missing out upon.
- What’s already present in the generator is already solid.
- Turn many of the pre-baked probabilities into knobs

4. Tester: Michael Tang 
- Like the idea of creating a tier system
- It is nice that the system limits the outputs of both higher and lower tier items
- It makes sense that a tier 4 shouldn’t give tier 1 loot 
