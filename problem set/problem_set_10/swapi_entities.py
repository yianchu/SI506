# Problem 2.0
class Planet:
    """Representation of a planet.
    Attributes:
        url (str): identifier/locator
        name (str): planet name
        rotation_period (int): rotation period
        orbital_period (int): orbital period
        diameter (int): diameter of the planet
        climate (list): climate type(s) found on planet
        gravity (dict): gravity level
        terrain (list): terrain type(s) found on planet
        surface_water (float): surface water
        population (int): population size
    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    # Problem 2.1
    def __init__(self, url, name):
        """Initialize a Planet instance."""
        self.url = url
        self.name = name
        self.rotation_period = None
        self.orbital_period = None
        self.diameter = None
        self.climate = None
        self.gravity = None
        self.terrain = None
        self.surface_water = None
        self.population = None

    # Problem 2.2
    def __str__(self):
        """Return a string representation of the object."""
        return self.name

    # Problem 2.3
    def has_surface_water(self):
        """Return a boolean representation of whether the planet has surface water."""
        if self.surface_water > 0:
            return True
        else:
            return False


    # Problem 2.5
    def is_populated(self):
        """Return a boolean representation of whether the planet has population."""
        if self.population > 0:
            return True
        else:
            return False

    # Problem 2.6
    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use the order specified in the Docstring above.
        Use a dictionary literal rather than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.
        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        return {
            'url': self.url,
            'name': self.name,
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'diameter': self.diameter,
            'climate': self.climate,
            'gravity': self.gravity,
            'terrain': self.terrain,
            'surface_water': self.surface_water,
            'population': self.population,
        }

# Problem 3.0
def convert_data(planet):
    """Convert string values of a dictionary to the appropriate type whenever possible.
    Remember to set the value to None when the string is "unknown".

    Type conversions:
        rotation_period (str->int)
        orbital_period (str->int)
        diameter (str->int)
        climate (str->list) e.g. ["hot", "humid"]
        gravity (str->dict) e.g. {"measure": 0.75, "unit"; "standard"}
        terrain (str->list) e.g. ["fungus", "forests"]
        surface_water (str->float)
        population (str->int)

    Parameters:
        dict: dictionary of a planet
    Returns:
        dict: dictionary of a planet with its values converted
    """
    #print(planet['name'])
    if planet['rotation_period']:
        if 'unknown' not in planet['rotation_period']:
            planet['rotation_period'] = int(planet['rotation_period'])
        else : planet['rotation_period'] = None
        #print(planet['rotation_period'] )
    if planet['orbital_period']:
        if 'unknown' not in planet['orbital_period']:
            planet['orbital_period'] = int(planet['orbital_period'])
        else : planet['orbital_period'] = None
        #print(planet['orbital_period'])
    if planet['diameter']:
        if 'unknown' not in planet['diameter']:
            planet['diameter'] = int(planet['diameter'])
        else : planet['diameter']= None
        #print(planet['diameter'])
    if planet['climate']:
        if 'unknown' not in planet['climate']:
            planet['climate'] = planet['climate'].replace(', ',',').split(',')
        else : planet['climate'] = None
        #print(planet['climate'])
    if planet['gravity']:
        if 'unknown' not in planet['gravity']:
            a = planet['gravity'].split()
            planet['gravity'] = {"measure" : float(a[0]), "unit" : "standard"}
        else : planet['gravity'] = None
        #print(planet['gravity'])
    if planet['terrain']:
        if 'unknown' not in planet['terrain']:
            planet['terrain'] = planet['terrain'].replace(', ',',').split(',')
        else : planet['terrain'] = None
        #print(planet['terrain'])
    if planet['surface_water']:
        if 'unknown' not in planet['surface_water']:
            planet['surface_water'] = float(planet['surface_water'])
        else : planet['surface_water'] = None
        #print(planet['surface_water'])
    if planet['population']:
        if 'unknown' not in planet['population']:
            planet['population'] = int(planet['population'])
        else : planet['population'] = None
    #print(planet['population'])

    #print(planet)
    return planet


# Problem 4.0
def create_planet(planet):
    """Creates a < Planet > instance from dictionary data. You must call the convert_data() function
    to clean up the planet dictionary first, then assign the dictionary to the instance.

    Parameters:
        planet (dict): planet as a dictionary
    Returns:
        Planet: new < Planet > instance
    """
    #print(planet)
    #planet = Planet(planet['url'], planet['name'])
    #rint(planet.name)
    a = convert_data(planet)
    b = Planet(a['url'], a['name'])
    b.rotation_period = a['rotation_period']
    b.orbital_period = a['orbital_period']
    b.diameter = a['diameter']
    b.climate = a['climate']
    b.gravity = a['gravity']
    b.terrain = a['terrain']
    b.surface_water = a['surface_water']
    b.population = a['population']
    #print(b)
    return b
    #print(planet)
    
