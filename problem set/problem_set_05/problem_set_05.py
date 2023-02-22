# SI 506 Problem Set 05

import csv
import copy

print("Problem 01\n\n")

# Problem 01: Implement read_csv and load the election data.

# TODO Implement


def read_csv(filepath):
    a = []
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        for line in f.readlines():
            # print(line)
            line = line.strip('\n')
            s = line.split(",")
            #s1 = s.strip("\n")
            # for i in range(3):
            #s[i] = s[i].strip()
            # print(i)
            #s1 = s.strip()
            # print(s)
            a.append(s)
    return a


raw_election_data_2021 = read_csv('election_data_2021.csv')
raw_election_data_2017 = read_csv('election_data_2017.csv')
# print(raw_election_data_2021)
# print(raw_election_data_2017)


print("\n\nProblem 02\n\n")

# Problem 02: Implement clean and clean the election data.

# TODO Implement


def clean(data):
    data_copy = copy.deepcopy(data)
    b = []
    b.append(data_copy[0])
    for i in data_copy[1:]:
        #a = i.split(',')
        # print(a)
        i[0] = i[0].strip()
        i[1] = i[1].strip()
        i[1] = int(i[1])
        i[2] = i[2].strip().lower()
        # print(i[2])
        #i[2] = ss.lowercase()
        b.append(i)
    return b
    # pass


clean_election_data_2017 = clean(raw_election_data_2017)
clean_election_data_2021 = clean(raw_election_data_2021)

print(clean_election_data_2017)
print(clean_election_data_2021)

print("\n\nProblem 03\n\n")

# Problem 03: Implement get_party_seat_differences and get the party seat differences for the 2021 election.

# TODO Implement


def get_seat_differences(current_election, previous_election):
    diff = []
    for i in current_election[1:]:
        for j in previous_election[1:]:
            b = []
            if i[0] == j[0]:
                c = i[1]-j[1]
                b.append(i[0])
                b.append(c)
                diff.append(tuple(b))
    return diff


party_seat_differences = []
party_seat_differences = get_seat_differences(
    clean_election_data_2021, clean_election_data_2017)
print(party_seat_differences)
print("\n\nProblem 04\n\n")

# Problem 04: Implement get_leaders and get the leaders for the 2021 election data.
party_leaders_2021 = [
    ('AfD', 'Joerg Meuthen and Tino Chrupalla'),
    ('FDP', 'Christian Lindner'),
    ('CDU/CSU', 'Armin Laschet'),
    ('SPD', 'Olaf Scholz'),
    ('Greens', 'Annalena Baerbock and Robert Habeck'),
    ('Left', 'Janine Wissler and Susanne Hennig-Wellsow')
]
election_data_2021_with_leaders = []


def get_leaders(election_data, party_leaders):
    data_copy = copy.deepcopy(election_data)
    data_copy[0].append("Party Leader(s)")
    for i in data_copy[1:]:
        for party_tuple in party_leaders:
            a, b = party_tuple
            if i[0] == a:
                party_tuple = b
                # print(party_tuple)
                i.append(party_tuple)
    return data_copy


election_data_2021_with_leaders = get_leaders(
    clean_election_data_2021, party_leaders_2021)
print(election_data_2021_with_leaders)
# TODO Implement


print("\n\nProblem 05\n\n")

# Problem 05: Implement get_affiliation_percents and get affiliation percents for the 2021 election data.


def get_seats_percent(election_data):
    total = 0
    left = right = no_far = far = 0
    b = []
    for j in election_data[1:]:
        total += j[1]
    print(total)
    for i in election_data[1:]:
        if "left" in i[2]:
            left += i[1]
        if "right" in i[2]:
            right += i[1]
        if "far" not in i[2]:
            no_far += i[1]
        if "far" in i[2]:
            far += i[1]
    b.append(round(left/total*100, 2))
    b.append(round(right/total*100, 2))
    b.append(round(far/total*100, 2))
    b.append(round(no_far/total*100, 2))

    return tuple(b)


affiliation_percents = get_seats_percent(clean_election_data_2021)
print(affiliation_percents)

# TODO Implement
print("\n\nProblem 06\n\n")


# Problem 06: Implement write_csv and write election_data_2021_with_leaders to a file called revised_election_data_2021.csv.

def write_csv(filepath, data):
    with open(filepath, "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


write_csv("revised_election_data_2021.csv", election_data_2021_with_leaders)
# TODO Implement
