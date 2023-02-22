import json, requests, copy


# Problem 01
def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """
    with open(filepath, 'r', encoding = encoding) as file_obj:
        ans = json.load(file_obj)
    return ans
     # TODO Implement


# Problem 02
def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more SWAPI entities to be found in ['results'] list; otherwise, response
    object body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """
    if params:
        reponse = requests.get(url, params, timeout=timeout)
    else:
        reponse = requests.get(url, timeout=timeout)
    #print(reponse.json())
    return reponse.json()
     # TODO Implement


# Problem 03
def delete_items(dictionary, key_list = None):
    # dict_copy = copy.deepcopy(dictionary)
    # for i in range(len(key_list)):
    #     if key_list[i] in dict_copy.keys():
    #         #print(key_list[i])
    #         del(dict_copy[key_list[i]])
    #print(dict_copy)
    dict_copy = copy.deepcopy(dictionary)
    for i in key_list:
        if i in dict_copy.keys():
            #print(key_list[i])
            del(dict_copy[i])
    return dict_copy

# Problem 04
def get_homeworld(person, key_list = None):
    #print(person)
    person_homeworld = get_swapi_resource(person['homeworld'])
    #copy_per_home = copy.deepcopy(person_homeworld)
    #print(person_homeworld)
    per_home = {}
    if key_list:
        for i in person_homeworld:
            if i in key_list:
                per_home.update({i:person_homeworld[i]})
    else:
        per_home = person_homeworld
    #print(per_home)
    return per_home
        #print(i)
def get_species(person, key_list = None):
    ans = {}
    if person['species']:
        val = person['species'][0]
        species = get_swapi_resource(val)
        if key_list:
            for i in key_list:
                if i in species.keys():
                    ans[i] = species[i]
        else:
            ans = species
    return ans


# Problem 05
def clean_person_dictionary(person, del_items, home_list=None, species_list=None):
    #print(del_items)
    a = delete_items(person, del_items)
    #print(a)
    b = get_homeworld(a, home_list)
    c = get_species(a, species_list)
    a['homeworld'] = b
    a['species'] = c
    return a

# Problem 06
def board_ship(ship, passengers):
    copy_ship = copy.deepcopy(ship)
    #print(copy_ship['passengers'])
    #order = passengers['boarding_order']
    print(passengers)
    # for i in range(len(order)):
    #     copy_ship = copy.deepcopy(ship)
    #print(ship['boarding_order'])
    #print(passengers['boarding_order'])
    ans = copy.deepcopy(passengers)
    for i in range(len(passengers)):
        order = 0
        order = passengers[i]['boarding_order']
        ans[order-1] = passengers[i]
        #copy_ship[order-1] = passengers[i]
    #print(ans)
    copy_ship['passengers'] = ans
    return copy_ship
    #print(copy_ship)
        #copy_ship[passengers[i]]







# Problem 07
def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent = 2):
    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)


def main():
    """Program entry point."""

    # Problem 01
    passengers = read_json('./passengers.json')['passengers']

    #print(f'\nProblem 01:\n{passengers}')

    # Problem 02
    base_url = 'https://swapi.py4e.com/api/'
    falcon_params = {'search': 'falcon'}
    #a = get_swapi_resource(base_url, falcon_params)['Millennium Falcon.']
    falcon = get_swapi_resource(base_url + '/starships/', falcon_params)['results'][0]
    #print(f'\nProblem 02:\n{falcon}')

    # Problem 03
    falcon_keys_delete = list(falcon.keys())[-5:]
    #print(falcon)
    falcon_updated = delete_items(falcon, falcon_keys_delete)
    #print(falcon_updated)


    # Problem 04
    #bail_home = get_homeworld(get_swapi_resource(base_url + '/people/'))
    a = get_swapi_resource(base_url + '/people/', {'search':'Bail Organa'})['results'][0]
    bail_home = get_homeworld(a)
    home_keys_keep = list(bail_home.keys())[0:9]
    bail_species = get_species(a)
    #print([bail_species])
    #print(bail_home)
    #print(b)


    # Problem 05
    del_items = ['films', 'vehicles', 'starships', 'created', 'edited', 'url']
    for i in passengers:
        name = i['name']
        inf = get_swapi_resource(base_url + '/people/', {'search':name})['results'][0]
        a = clean_person_dictionary(inf, list(del_items), home_keys_keep,list(['name']))

    # Problem 06
    all_aboard = board_ship(falcon_updated, passengers)


    # Problem 07
    leaving_tatooine = 'hyperspace_jump.json'
    write_json(data=all_aboard, filepath=leaving_tatooine)


if __name__ == '__main__':
    main()
