# START PROBLEM SET 02
print('Problem Set 02')

# PROBLEM 1 (10 points)
print('\nProblem 1')

gme_prices = [15.84, 35.50, 65.01, 325.00, 63.77]

price_max = max(gme_prices) #TODO: Replace

price_max_index = gme_prices.index(price_max) #TODO: Replace

gme_prices.append(52.40)#TODO: Problem 1.3

gme_prices[0] = 17.69#TODO: Problem 1.4

print(gme_prices)

# PROBLEM 2 (10 points)
print('\nProblem 2')

amc_prices = [33.47, 34.41, 40.84, 44.02, 50.16] #TODO: Replace

amc_prices_latest = amc_prices[5-1] #TODO: Replace


amc_prices_last_three = amc_prices[2:] #TODO: Replace
print(amc_prices_last_three)


# PROBLEM 3 (10 points)
print('\nProblem 3')

pltr_prices = ' 21.82-24.90-24.01-25.71-26.64-26.28 '
pltr_prices = pltr_prices.strip()

pltr_prices_list = pltr_prices.split("-") #TODO: Replace
print(pltr_prices_list)


# PROBLEM 4 (20 points)
print('\nProblem 4')

dates = ['September 10th', 'September 3rd', 'August 27th', 'August 20th', 'August 13th', 'August 6th']
dates.reverse()
dates_str = '|'.join(dates)
#dates_str = dates.join("|")
print(dates_str)

# PROBLEM 5 (20 points)
print('\nProblem 5')
a = pltr_prices_list.index(max(pltr_prices_list))
print(a)
pltr_highest = f"In the week ending on {dates[a]}, Palantir closed with a price of ${pltr_prices_list[a]} and AMC closed with a price of ${amc_prices[a-1]}."
#Uncomment once you've defined pltr_highest
print(pltr_highest)

b = amc_prices.index(max(amc_prices))+1
#print(b)
amc_highest = f"In the week ending on {dates[b]}, Palantir closed with a price of ${pltr_prices_list[b]} and AMC closed with a price of ${amc_prices[b-1]}."
#Uncomment once you've defined amc_highest
print(amc_highest)

# PROBLEM 6 (20 points)
print('\nProblem 6')
dates_reversed = dates[::-1]
print(dates_reversed)

# PROBLEM 7 (10 points) 
print('\nProblem 7')

every_other_date = dates_reversed[::2]
print(every_other_date)