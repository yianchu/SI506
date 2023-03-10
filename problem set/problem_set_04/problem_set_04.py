# SI 506 Problem Set 04

# Part 1
menu = [
    ["name", "categories", "price (HKD)"],
    ["short ribs with xo source", "steamed", 28],
    ["pan-fried turnip cake", "Pan-fried/Baked", 22],
    ["Malay sponge cake", "sweet", 17],
    ["baked egg tart", "sweet", 18],
    ["custard bun", "steamed", 21],
    ["barbecued pork bun", "steamed", 17],
    ["lotus seed bun", "steamed", 18],
    ["shrimp dumpling", "steamed", 29],
    ["shumai", "steamed", 26],
    ["braised chicken feet", "steamed", 19],
    ["pineapple bun", "Pan-fried/Baked", 19],
    ["veggies", "steamed", 17],
    ["lo mai gai", "steamed", 24],
    ["curry beaf strip", "steamed", 26],
    ["honey stewed bbq pork rice roll", "rice roll", 23],
    ["shrimp rice roll", "rice roll", 29],
    ["chrysanthemum", "tea", 8],
    ["longjing", "tea", 20],
    ["tieguanyin", "tea", 12],
    ["dahongpao", "tea", 18],
    ["pu'er", "tea", 10],
]

print("Problem 01\n\n")

# Problem 01: Convert HKD to USD.

# TODO Implement

menu[0].append("price (USD)")

for i in menu[1:]:
    i.append(round(i[2]*0.128, 2))


print(menu)

print("\n\nProblem 02\n\n")

# Problem 02: Categorize items into superb, top, good, and tea (15 points).

# TODO Implement

menu[0].append("grade")
for i in menu[1:]:
    if (i[1] == "tea"):
        i.append("tea")
    else:
        if (i[2] > 25):
            i.append("superb")
        elif (i[2] > 20 and i[2] <= 25):
            i.append("top")
        elif (i[2] <= 20):
            i.append("good")

print(menu)

print("\n\nProblem 03\n\n")

# Problem 03: Find the max & min price of dim sums as well as their names (20 points).
max_price = 0
max_names = []
min_price = 100
min_names = []

# TODO Implement
for i in menu[1:]:
    if i[1] != "tea":
        if (i[2] > max_price):
            max_price = i[2]
        if (i[2] < min_price):
            min_price = i[2]

for i in menu[1:]:
    if i[1] != "tea":
        if (i[2] == max_price):
            max_names.append(i[0])
        if (i[2] == min_price):
            min_names.append(i[0])

print(f"max price: {max_price}")
print(f"max names: {max_names}")
print(f"min price: {min_price}")
print(f"min names: {min_names}")

print("\n\nProblem 04\n\n")

# Problem 04: Get the average price of steamed dim sums (10 points).
steamed_avg_price = 0
count = 0
price = 0
# TODO Implment

for i in menu[1:]:
    if(i[1] == "steamed"):
        count += 1
        price += i[2]

steamed_avg_price = price/count

print(f"average price of steamed dim sums: {steamed_avg_price}")


# Part 2

print("\n\nProblem 5.1\n\n")

# Problem 5.1: implement get_category_by_food (15 points).


def get_category_by_food(menu, food_name):  # pass  # TODO replace with code block
    for i in menu[1:]:
        if(i[0] == food_name):
            return i[1]
            break
    # Change None to your return value


print(
    f"E.g. the category of longjing: {get_category_by_food(menu, 'longjing')} (should be tea)")
print(
    f"E.g. the category of shumai: {get_category_by_food(menu, 'shumai')} (should be steamed)")

print("\n\nProblem 5.2\n\n")

# Problem 5.2: is_one_cup_two_pieces (10 points).
##### Helper function (DO NOT MODIFY) #####


def is_one_cup_two_pieces(menu, foods):
    condition1 = (
        get_category_by_food(menu, foods[0]) == "tea" and
        get_category_by_food(menu, foods[1]) != "tea" and
        get_category_by_food(menu, foods[2]) != "tea"
    )
    condition2 = (
        get_category_by_food(menu, foods[1]) == "tea" and
        get_category_by_food(menu, foods[0]) != "tea" and
        get_category_by_food(menu, foods[2]) != "tea"
    )
    condition3 = (
        get_category_by_food(menu, foods[2]) == "tea" and
        get_category_by_food(menu, foods[0]) != "tea" and
        get_category_by_food(menu, foods[1]) != "tea"
    )

    return condition1 or condition2 or condition3
##### Helper function (DO NOT MODIFY) #####


print(
    f"E.g. Testing with longjing, veggies, and shumai: {is_one_cup_two_pieces(menu, ['longjing', 'veggies', 'shumai'])} (should be True)")
print(
    f"E.g. Testing with longjing, dahongpao, and shumai: {is_one_cup_two_pieces(menu, ['longjing', 'dahongpao', 'shumai'])} (should be False)")

print("\n\nProblem 5.3\n\n")

# Problem 6.1: implement has_one_cup_two_pieces (15 points).


def has_one_cup_two_pieces(menu, order):
    count_tea = 0
    count_dish = 0
    for i in order:
        if get_category_by_food(menu, i) == "tea":
            count_tea += 1
        if get_category_by_food(menu, i) != "tea":
            count_dish += 1

    if count_tea >= 1 and count_dish >= 2:
        return True  # Change None to your return value
    else:
        return False


print(
    f"E.g. Testing with ['shumai', 'longjing']: {has_one_cup_two_pieces(menu, ['shumai', 'longjing'])} (should be False)")
print(
    f"E.g. Testing with ['shumai', 'longjing', 'veggies', 'custard bun']: {has_one_cup_two_pieces(menu, ['shumai', 'longjing', 'veggies', 'custard bun'])} (should be True)")

print("\n\nProblem 6.2\n\n")

# Problem 6.2: implement get_total_price (10 points).
##### Helper function (DO NOT MODIFY) #####


def get_price_by_food(menu, food_name):
    dim_sum_names = [item[0] for item in menu]
    idx = dim_sum_names.index(food_name)
    return menu[idx][2]
##### Helper function (DO NOT MODIFY) #####


def get_total_price(menu, order):
    price = 0
    for i in order:
        price += get_price_by_food(menu, i)
    if has_one_cup_two_pieces(menu, order):
        price = price*0.8
    return round(price, 2)  # Change None to your return value


print(
    f"E.g. Testing with ['shumai', 'longjing']: {get_total_price(menu, ['shumai', 'longjing'])} (should be 46)")
print(
    f"E.g. Testing with ['shumai', 'longjing', 'veggies']: {get_total_price(menu, ['shumai', 'longjing', 'veggies'])} (should be 50.4)")
