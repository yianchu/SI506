# START LAB EXERCISE 06
print('Lab Exercise 06 \n')

# SETUP
chinese_desserts = [
    ["Wheat Flour Cake", 190],
    ["Egg Yolk", 260],
    ["Green Bean Cake", 100],
    ["Taro Pastry", 227],
    ["Durian Cake", 360],
    ["Flower Pastry", 130],
    ["Sun Cake", 172]
]

# END SETUP

# PROBLEM 1 (3 points)

# TODO Implement function


def get_name(x):
    return x[0]


name = get_name(chinese_desserts[0])  # call function

print(f"\n1. First dessert item: {name}")


# PROBLEM 2 (3 points)

# TODO Implement function

def get_calories(x):
    return x[1]


calories = get_calories(chinese_desserts[1])  # call function

print(f"\n2A. Calories of the second dessert item: {calories}")


# PROBLEM 3 (5 points)

# TODO Implement function

# TODO call function

def remove_dessert(desserts, dessert):
    if dessert in desserts:
        desserts.remove(dessert)


sun_cake = chinese_desserts[6]
remove_dessert(chinese_desserts, sun_cake)

print(f"\n3. {chinese_desserts}")


# Problem 4 (6 points)

# TODO Create variable

# TODO call function

def add_dessert(desserts, dessert, idx=0):
    desserts.insert(idx, dessert)


sweetheart_cake = ["Sweetheart Cake", 170]
add_dessert(chinese_desserts, sweetheart_cake, 1)

print(f"\n4. {chinese_desserts}")


# Problem 5 (3 points)

# TODO Implement function

# TODO call function

egg_tarts = ["Egg Tarts", 376]
add_dessert(idx=2, dessert=egg_tarts, desserts=chinese_desserts)

print(f"\n5. {chinese_desserts}")
# END LAB EXERCISE
