import json
import swapi_entities as ent

# Problem 1.0
def read_json(filepath, encoding='utf-8'):
    """
    Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.
    Parameters:
        filepath (string): path to file
        encoding (string): optional name of encoding used to decode the file. The default is 'utf-8'.
    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


# Problem 1.0
def write_json(filepath, data):
    """
    This function dumps the JSON object in the dictionary `data` into a file on
    `filepath`.
    Parameters:
        filepath (string): The location and filename of the file to store the JSON
        data (dict): The dictionary that contains the JSON representation of the objects.
    Returns:
        None
    """

    with open(filepath, 'w') as file_obj:
        json.dump(data, file_obj)


def main():
    # Problem 1.0
    planet_data = read_json('swapi_planets.json')
    #print(planet_data[0])
    #a = ent.create_planet(planet_data[9])
    #print(a)

    # Problem 2.0 - Problem 4.0
    # Complete in problem_set_10_utils.py

    # Problem 5.2
    global planets
    planets = {}
    for i in planet_data:
        # print(i['name'])
        # print(i['gravity'])
        #print(i)
        a = ent.create_planet(i)
        #print(a.jsonable())
        planets.update({a.name:a})
    #print(planets)

    # Problem 6.0
    planets_with_surface_water = []
    planets_inhabited = []
    planets_uninhabited = []
    planets_desert_only = []
    planets_biggest_smallest = {"biggest": [], "smallest": []}
    big = 0
    small = 100000
    #print(planets)
    for i in planets.items():
        val = i[1]
        if val.surface_water:
            if val.has_surface_water():
                planets_with_surface_water.append(i[1].jsonable())
        if val.population != None:
            #print(val.population)
            if val.is_populated():
                planets_inhabited.append(i[1].jsonable())
            else:
                planets_uninhabited.append(i[1].jsonable())
        if val.terrain:
            #print(val.terrain)
            if 'desert' in val.terrain and len(val.terrain) == 1:
                #print(val.terrain)
                planets_desert_only.append(i[1].jsonable())
        if val.diameter or val.diameter == 0:
            #print(val.name)
           # print(val.diameter)
            if val.diameter > big:
                big = val.diameter
            if val.diameter < small:
                small = val.diameter

    for i in planets.items():
        val = i[1]
        if val.diameter == big:
            planets_biggest_smallest['biggest'].append(i[1].jsonable())
        if val.diameter == small:
            planets_biggest_smallest['smallest'].append(i[1].jsonable())

    #print(planets_biggest_smallest)



    write_json('stu_planets_with_surface_water.json', planets_with_surface_water)
    write_json('stu_planets_inhabited.json', planets_inhabited)
    write_json('stu_planets_uninhabited.json', planets_uninhabited)
    write_json('stu_planets_desert_only.json', planets_desert_only)
    write_json('stu_planets_biggest_smallest.json', planets_biggest_smallest)


if __name__ == '__main__':
    main()
