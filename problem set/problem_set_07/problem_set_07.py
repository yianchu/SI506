import csv


def read_csv_to_dicts(filepath, encoding='utf-8-sig', newline='', delimiter=','):
    """
    NOTE: This is a helper function - please do NOT edit or delete it.

    Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line)  # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data


def write_dicts_to_csv(filepath, data, fieldnames, encoding='utf-8', newline=''):
    """
    NOTE: This is a helper function - please do NOT edit or delete it.

    Writes dictionary data to a target CSV file as row data using the csv.DictWriter().
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): dictionary content to be written to the target file
        fieldnames (seq): sequence specifing order in which key-value pairs are written to each row
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames)
        writer.writeheader()
        writer.writerows(data)

# PROBLEM 2


def clean_data(data):
    """
    This function takes in data and returns a mutated version that converts string versions of numbers
    to their integer or float form depending on the type of value.

    Parameters:
        data (list): A list of dictionaries.

    Returns:
        (list): A list of dictionaries with the numerical values appropriately converted.
    """
    for i in data:
        if 'points' in i.keys():
            i['points'] = float(i['points'])
        if 'position' in i.keys():
            i['position'] = int(i['position'])
    return data
    # print(i)
    # TODO: Implement

# PROBLEM 3


def convert_time_to_ms(driver_dict):
    # for i in driver_dict:
    a, b, c = driver_dict['fastest_lap'].split(":")
    time = int(a)*60000+int(b)*1000+int(c)
    # print(driver_dict)
    return time


# PROBLEM 4
def add_fastest_lap_point(race_result):
    # a = {}
    #nam = ''
    current_fastest_lap_time = 100000
    for i in race_result:
        lap_time = convert_time_to_ms(i)
        if i['position'] <= 10 and lap_time < current_fastest_lap_time:
            # print(i)
            current_fastest_lap_time = lap_time
            driver = i['name']
            #a = i
    # print(nam)
    # print(a)
    #a['points'] = a['points']+1
    # print(a)
    for j in race_result:
        # print(j.value())
        # if driver in j['name']:
        if driver in j.get('name'):
            # print(nam)
            j['points'] += 1  # j['points']+1
            # print(j)
    return race_result


# PROBLEM 5
def update_driver_standings(standings, race_result):
    for i in standings:
        for j in race_result:
            if i['driver'] == j['name']:
                i['points'] = i['points']+j['points']
    # print(standings)
    return standings

# PROBLEM 6


def compare_points_by_nation(standings, nationality1, nationality2):
    """
    This function calculates the average points for all drivers for two nations and returns
    a tuple with the name and average points for the nation with the higher average points.

    Parameters:
        standings (list): A list of dictionaries that contains the drivers' standings.
        nationality1 (str): A string signifying the first nationality to be checked for.
        nationality2 (str): A string signifying the second nationality to be checked for.

    Returns:
        (tuple): A tuple with the nationality and average points for the nation with
        the higher average points.
    """
    num1 = num2 = 0
    count1 = count2 = 0
    new = []
    # print(standings)
    for i in standings:
        if nationality1 in i['nationality']:
            num1 += i['points']
            count1 += 1
        if nationality2 in i['nationality']:
            num2 += i['points']
            count2 += 1
    if round(num1/count1, 1) > round(num2/count2, 1):
        # new.append(tuple(nationality1, round(num1/count1, 1)))
        return (nationality1, round(num1/count1, 1))
    else:
        # new.append(tuple(nationality2, round(num1/count2, 1)))
        return (nationality2, round(num2/count2, 1))
      # TODO: Implement

# Main function


def main():
    """
    This function serves as the main point of entry point of the program
    """

    # PROBLEM 1
    standings = read_csv_to_dicts(
        'driver_standings_pre_USGP.csv', encoding='utf-8-sig', newline='', delimiter=',')
    race_result = read_csv_to_dicts(
        'usgp_results.csv', encoding='utf-8-sig', newline='', delimiter=',')

    # print(f'\n{standings}')
    # print(f'\n{race_result}')

    last_standing_keys = standings[-1].keys()
    # print(f'\n{last_standing_keys}')  # Uncomment to test

    third_standing_values = standings[2].values()
    # print(f'\n{third_standing_values}')  # Uncomment to test

    tenth_race_result_kv = race_result[9].items()
    # print(f'\n{tenth_race_result_kv}')  # Uncomment to test

    # PROBLEM 2
    cleaned_standings = clean_data(standings)
    # print(f'\nCleaned standings:\n{cleaned_standings}')

    cleaned_race_result = clean_data(race_result)
    # print(f'\nCleaned race results:\n{cleaned_race_result}')

    # PROBLEM 3 (Optional Check)
    # print(cleaned_race_result[0])
    convert_time_to_ms(cleaned_race_result[0])
    # print(convert_time_to_ms(cleaned_race_result[0]))

    # PROBLEM 4
    updated_race_result = add_fastest_lap_point(cleaned_race_result)

    # PROBLEM 5
    updated_standings = update_driver_standings(cleaned_standings, updated_race_result)
    # print(updated_standings)

    # PROBLEM 6
    ger_vs_gbr = compare_points_by_nation(
        updated_standings, 'German', 'British')
    fra_vs_spa = compare_points_by_nation(
        updated_standings, 'French', 'Spanish')
    # print(ger_vs_gbr)

    # PROBLEM 7
    # print(updated_standings)
    write_filepath = 'driver_standings_post_USGP.csv'
    write_fieldnames = ['driver', 'team', 'nationality', 'points']
    # write_fieldnames = list(updated_standings[0].keys())
    # print(list(write_fieldnames))
    write_dicts_to_csv(filepath=write_filepath, data=updated_standings, fieldnames=write_fieldnames)


# DO NOT EDIT
if __name__ == '__main__':
    main()
