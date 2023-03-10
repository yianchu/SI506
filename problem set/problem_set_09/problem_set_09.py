""" start setup """

import json
import requests
PEOPLE_URL = 'http://swapi.py4e.com/api/people/'

""" end setup """

# Problem 1.0
class Droid():

    # Problem 1.1
    def __init__(self, name, height, mass):
        """
        The constructor of the `Droid` class. This method takes in the given parameters
        and assigns them to the attributes (instance variables) of the class. It then creates
        additional attributes and assigns them with the specified values.
        Parameters:
            name (string): name of the Droid we are looking for
            height (string): height of the Droid we are looking for
            mass (string): mass of the Droid we are looking for
        Additional Attribute:
            languages (None): this is not a parameter, but should be created as an attribute of the class
                              and assigned the value None. We will load a language database into this
                              attribute later.
        Returns:
            None
        """
        self.name = name
        self.height = height
        self.mass = mass
        self.languages = None

    # Problem 1.2
    def __str__(self):
        """
        This method provides a readable string representation of the object.
        Parameters:
            None
        Returns:
            string: If languages != None, returns an f-string with the following syntax:
                    '< name > is a droid with height < height > and mass < mass >. Status: operational.'
            string: If languages == None, returns an f-string with the following syntax:
                '   < name > is a droid with height < height > and mass < mass >. Status: not operational.'
        """
        if self.languages:
            #a = print(f'< {self.name} > is a droid with height < {self.height} > and mass < {self.mass} >. Status: operational.')
            return f'{self.name} is a droid with height {self.height} and mass {self.mass}. Status: operational.'
        else:
            #b = print(f'< {self.name} > is a droid with height < {self.height} > and mass < {self.mass} >. Status: not operational.')
            return f'{self.name} is a droid with height {self.height} and mass {self.mass}. Status: not operational.'

    # Problem 1.3
    def load_languages(self, languages):
        """
        Assigns the parameter languages to the instance variable languages.
        Parameters:
            languages (Languages object): an object of the Languages class
        Returns:
            None
        """
        self.languages = languages

    # Problem 1.4
    def jsonable(self):
        """
        This method returns a JSON-friendly representation of the `Droid` object.
        The key should be the name of instance variable and value should be the corresponding value.
        For example, self.title should be converted in this way:
        {"title": self.title}
        If languages != None, make sure to call the `jsonable` method on languages.
        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        languages = None
        if self.languages: #if self.homeworld != None
            languages = self.languages.jsonable()

        return{
            'name' : self.name,
            'height' : self.height,
            'mass' : self.mass,
            'languages': languages
        }


# Problem 2.0
class Languages():

    # Problem 2.1
    def __init__(self):
        """
        The constructor of the `Languages` class. This method creates
        attributes and assigns them with the specified values.
        Parameters:
            This method takes no parameters
        Additional Attributes:
            language_database (dict): a dictionary of language information (set to an empty dictionary)
            language_count (int): number of languages in the dictionary (set to 0)
        Returns:
            None
        """
        self.language_database = {}
        self.language_count = 0

    # Problem 2.2
    def __str__(self):
        """
        This method provides a readable string representation of the object.
        Parameters:
            None
        Returns:
            string: An f-string with the following syntax:
                    'This language database currently contains < language_count > language entries.'
        """
        return f'This language database currently contains {self.language_count} language entries.'

    # Problem 2.3
    def add_language(self, species):
        """
        This method takes a dictionary representing a species. If the species' language is not in the
        `language_database` dictionary, this method should createa new dictionary entry with the language
        as the key and a list containing a tuple in which the species' name is at index 0 and the species'
        homeworld is at index 1. If the species' language is already in the `language_database` dictionary,
        this method should append a tuple in which the species' name is at index 0 and the species'
        homeworld is at index 1 to the language's associated value, a list.
        Paramters:
            species (dict): a dict representing a species
        Returns:
            None
        """

        if species['language'] not in self.language_database:
            a = {species['language'] : [(species['name'], species['homeworld'])]}
            self.language_database.update(a)

        else:
            self.language_database[species['language']].append((species['name'], species['homeworld']))
            #b = (species['name'], species['homeworld'])
            #self.language_database[species['language']].append((species['name'], species['homeworld']))
            #self.language_database[species['language']][0].append(species['name'])
            #self.language_database[species['language']][1].append(species['homeworld'])

            #print(species['name'])
            #print(self.language_database[species['language']][0][0])



    # Problem 2.4
    def update_language_count(self):
        """
        This method takes the length of `language_database` and stores it in the lanugage_count variable
        Parameters:
            None
        Returns:
            None
        """
        #length = len(self.language_database)
        self.language_count = len(self.language_database)

    # Problem 2.5
    def get_speakers(self, language):
        """
        This method returns a list of tuples from the `language_database` dictionary representing
        the speakers of a language.
        Parameters:
            language (string): a string representing a language
        Returns:
            list: a list from the `language_database` dictionary representing the speakers of a language
        """
        for i in self.language_database.keys():
            if language == i:
                return [self.language_database[i][0]]

    # Problem 2.6
    def jsonable(self):
        """
        This method returns a JSON-friendly representation of the `Languages` object.
        The key should be the name of instance variable and value should be the corresponding value.
        For example, self.title should be converted in this way:
        {"title": self.title}
        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        return{
           'language_database' : self.language_database,
           'language_count' : self.language_count
        }



# Problem 3.1
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

# Problem 4.0
def get_swapi_resource(resource, params=None, timeout=20):
    """
    This function initiates an HTTP GET request to the SWAPI service in order to return a
    representation of a resource. `params` is not included in the request if no params is passed to this
    function during the function call. Once a response is received, it is converted to a python dict.
    Parameters:
        resource (string): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments. The default value is None.
        timeout (int): timeout value in seconds. The default value is 20.
    Returns:
        dict: dictionary representation of the decoded JSON.
    """
    if params:
        return requests.get(resource, params, timeout=timeout).json()
    else:
        return requests.get(resource, timeout=timeout).json()

# Problem 5.1
def fill_language_database(species_data, language_database):
    """
    This function takes a list of dictionaries representing species and uses the information therin to fill
    a language database. This function should skip the 'Droid' species. For all other species, it should
    replace the url string at the 'homeworld' key with the name of the homeworld planet. It should then pass
    the updated dictionary to the `language_database`'s `add_language` method.
    Parameters:
        species_data (list): a list of dicts, with each dict representing a single species
        language_database (Languages object): an instance of the Languages class
    Returns:
        language_database (Languages object): an instance of the Languages class loaded with language data
    """
    #language_database = Languages()
    for i in species_data:
         if 'Droid' not in i['name']:
              a = get_swapi_resource(i['homeworld'])
              i['homeworld'] = a['name']
              #print(i)
              language_database.add_language(i)
              #print(language_database.language_database)
    #print(language_database.language_database)
    return language_database

# Problem 6.2
def create_droid(data):
    """
    This function takes one parameter, a dictionary, represnting a person and returns
    an instance of the Droid class.
    Parameters:
        data (dict): a dictionary representing a person
    Returns:
        Droid object: an instance of the Droid class
    """
    #print(Droid(data['name'], data['height'], data['mass']))
    return Droid(data['name'], data['height'], data['mass'])


# Problem 7.1
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
    # Problem 3.2
    species_data = read_json('swapi_species.json')
    #print(species_data)
    # Problem 5.2
    language_database = fill_language_database(species_data, Languages())
    language_database = Languages()
    language_database.update_language_count()
    galactic_basic_speakers = language_database.get_speakers('Galactic Basic')
    # galactic_basic_speakers = Languages.get_speakers('Galactic Basic')

    #print(f'Testing language_database: {language_database}')

    # Problem 6.1
    c3po_data = get_swapi_resource(PEOPLE_URL, {'search' : 'C-3PO'})['results'][0]
    # Problem 6.3
    #print(c3po_data)
    #c3po = create_droid(c3po_data)
    #print(c3po)
    c3po = create_droid(c3po_data)
    Droid.load_languages(c3po, language_database)

    print(f'Testing c3po: {c3po}')

    # Problem 7.2
    #a = Droid.jsonable(c3po)

    write_json('c3po.json', c3po.jsonable())

if __name__ == '__main__':
    main()
