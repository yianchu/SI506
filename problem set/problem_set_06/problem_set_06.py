import csv
import copy

# Problem 01


def read_csv(filepath, encoding='utf-8'):
    """
    This function reads in a csv and returns its contents as a list

    Parameters:
        filepath (str): A str representing the filepath for the file to be read
        encoding (str): A str representing the character encoding of the file

    Returns:
        (list): A list with the content of the file
    """
    # TODO: Replace and Implement
    with open(filepath, 'r', encoding=encoding) as file_obj:
        reader = csv.reader(file_obj)
        data = []
        for line in reader:
            data.append(line)
        return data

# Problem 02


def add_ratings(shows, ratings):
    """
    This function makes a copy of a show list and adds the shows IMDb rating to it

    Parameters:
        shows (list): A list of shows
        ratings (list): A list of IMDb ratings for the shows

    Returns:
        (list): A list of shows with the ratings added
    """
    # TODO: Replace and Implement
    shows_copy = copy.deepcopy(shows)
    # print(shows_copy)
    shows_copy[0].append('IMDb Rating')
    for i in shows_copy[1:]:
        num = shows_copy.index(i)
        i.append(ratings[num][1])
        # print(num)
    return shows_copy


# Problem 03


def clean_show_data(shows):
    """
    This function cleans the data of a list of shows

    Parameters:
        shows (list): A list of shows

    Returns:
        (list): The list of shows with clean data
    """
    # TODO: Replace and Implement
    shows_copy = copy.deepcopy(shows)
    for i in shows_copy[1:]:
        # print(i)
        # a = i.split(',')
        i[1] = i[1].split('/')
        i[2] = i[2].split('/')
        i[3] = float(i[3])
        # print(i)
    return shows_copy


# Problem 04
def get_highest_rated_show(shows):
    highest = []
    high_rate = 0
    for i in shows[1:]:
        if i[3] > high_rate:
            a = []
            a.append(i[0])
            a.append(i[1])
            high_rate = i[3]
    highest = tuple(a)
    # print(highest)
    return highest

# Problem 05


def filter_by_genre(shows, genre):
    # print(shows)
    genre_list = []
    for item in shows:
        for i in item[2]:
            if genre.lower() == i.lower():
                # print(item)
                genre_list.append(item)
            # print(genre_list)
    # print(genre_list)
    return genre_list

# Problem 06


def stringify(shows):
    shows_copy = copy.deepcopy(shows)
    # print(shows_copy)
    for i in shows_copy[1:]:
        i[1] = '/'.join(i[1])
        i[2] = '/'.join(i[2])
    # print(shows_copy)
    return shows_copy


# Problem 07
def write_csv(filepath, data):
    with open(filepath, 'w', encoding='utf-8', newline='') as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(data)

# Main function


def main():
    """
    This function serves as the main point of entry point of the program
    """
    # Problem 01
    netflix_data = read_csv('netflix_data.csv')  # TODO: Replace
    disney_data = read_csv('disney_data.csv')  # TODO: Replace
    netflix_ratings = read_csv('netflix_ratings.csv')  # TODO: Replace
    disney_ratings = read_csv('disney_ratings.csv')  # TODO: Replace

    # Problem 02
    netflix_data_with_ratings = add_ratings(
        netflix_data, netflix_ratings)  # TODO: Replace
    disney_data_with_ratings = add_ratings(
        disney_data, disney_ratings)  # TODO: Replace
    # print(netflix_data_with_ratings)

    # Problem 03
    clean_netflix_data = clean_show_data(
        netflix_data_with_ratings)  # TODO: Replace
    clean_disney_data = clean_show_data(
        disney_data_with_ratings)  # TODO: Replace
    # print(clean_netflix_data)

    # Problem 04
    best_netflix_show = get_highest_rated_show(
        clean_netflix_data)  # TODO: Replace
    best_disney_show = get_highest_rated_show(
        clean_disney_data)  # TODO: Replace

    # Problem 05
    sci_fi_shows = []
    sci_fi_shows.append(clean_netflix_data[0])
    # print(sci_fi_shows)
    net_sci = filter_by_genre(clean_netflix_data, 'Science Fiction')
    dis_sci = filter_by_genre(clean_disney_data, 'Science Fiction')
    sci_fi_shows.extend(net_sci)
    sci_fi_shows.extend(dis_sci)
    print(sci_fi_shows)

    # Problem 06
    stringified_sci_fi_shows = stringify(sci_fi_shows)

    # Problem 07
    write_csv('sci_fi_shows.csv', stringified_sci_fi_shows)

    # WARN: if variables in the tuple below are not yet defined, initialize them to zero (0)
    return (netflix_data, disney_data, netflix_ratings, disney_ratings, netflix_data_with_ratings,
            disney_data_with_ratings, clean_netflix_data, clean_disney_data, best_netflix_show, best_disney_show
            )


# Do not delete
if __name__ == '__main__':
    main()
