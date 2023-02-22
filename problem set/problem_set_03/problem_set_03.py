# SI 506 Problem Set 03

# PART 1
print('\nPART 1')

day_1 = [
    'Kennedy & Company Education Strategies, LLC',
    'Congressional Research Service',
    'M&T Bank',
    'MassMutual Michigan Metro',
    'Alliance for Catholic Eduation (ACE Teaching Fellows)',
    'enFocus',
    'Buckle',
    'Defense Finance and Accounting Services (DFAS)',
    'AllianceBernstein',
    "Domino's",
    'Epic',
    'Fisher Investments',
    'goPuff dba GoBrands Inc.',
    'Govern For America',
    'Guidehouse',
    'Maxim Integrated Now Part of Analog Devices',
    'Equitable Advisors',
    'Exelon Corporation'
]


# PROBLEM 1
print('\nPROBLEM 1')

# 1.1

day_1.sort()
print(f'\nSorted Day 1 List: {day_1}.')

# 1.2
a_companies = []
a_companies = day_1[slice(2)]
a_companies = day_1[:2]

print(f"\nThe companies that start with 'A' are {a_companies}.")

# 1.3
num_a_companies = len(a_companies)
print(
    f"\nThere are {num_a_companies} companies that start with the letter 'A'.")


# PROBLEM 2
print('\nPROBLEM 2')

# 2.1
e_companies = []

for day in day_1:
    if day.lower().startswith('e'):
        e_companies.append(day)
print(f"\nThe companies that start with 'e' are {e_companies}.")

# 2.2
num_e_lower = 0
for day in e_companies:
    if day.startswith('e'):
        num_e_lower += 1

# PART 2

salaries = """Domino's|Graphic Designer|39000
Fisher Investments|Analyst|95916
Department of Health & Human Services|Technical Writing Specialist|76703
Splunk|Front-End Engineer|139554
Domino's|Senior Technical Writer|98000
Department of Health & Human Services|Analyst|71754
Domino's|Digital Specialist|93000
Splunk|Product Manager|134633
Dimensional Insight|Consultant|69359
Splunk|Customer Success Manager|125720
Edgeworth Economics|Consultant|80190
Edgeworth Economics|Economic Consultant|80645
Edgeworth Economics|Computer Systems Engineer|98495
Domino's|Analyst|77937
Fisher Investments|Research Associate|79141
Splunk|Data Analyst|117652
"""


# PROBLEM 3
print('\nPROBLEM 3')
sal_strings = []
sal_strings = salaries.splitlines()
#sal_strings = sal_strings[:len(sal_strings)-1]
print(sal_strings)

sal_lists = []
for s in sal_strings:
    sal_lists.append(s.split('|'))
print(sal_lists)

# PROBLEM 4
print('\nPROBLEM 4')

dom_sals = []
dom_idx = []
i = 0
while i < len(sal_lists):
    s = sal_lists[i]
    if "Domino's" in s[0]:
        dom_sals.append(s)
        dom_idx.append(i)
    i += 1
print(dom_sals)
print(dom_idx)


# PROBLEM 5
print('\nPROBLEM 5')
consultant_sals = []
analyst_sals = []
for s in sal_lists:
    if 'consultant' in s[1].lower():
        consultant_sals.append(s)
    elif s[1].lower() == 'analyst':
        analyst_sals.append(s)
print(consultant_sals)
print(analyst_sals)


# PROBLEM 6
print('\nPROBLEM 6')
analyst_sals = []
for s in sal_lists:
    if s[1].lower() != 'analyst':
        continue
    else:
        analyst_sals.append(s)

max_analyst_sal = 0
max_analyst_company = ""
for s in analyst_sals:
    sal = int(s[2])
    if sal > max_analyst_sal:
        max_analyst_sal = sal
        max_analyst_company = s[0]
print(max_analyst_sal)
print(max_analyst_company)


# PROBLEM 7
print('\nPROBLEM 7')
sal_great = []
sal_too_low = []
for index in range(10):
    s = sal_lists[index]
    sal = int(s[2])
    if sal > 50000:
        sal_great.append(s)
    else:
        sal_too_low.append(s)

print(sal_great)
print(sal_too_low)


for s in analyst_sals:
    sal = int(s[2])
    if sal > max_analyst_sal:
        max_analyst_company = s[0]
        max_analyst_sal = sal
