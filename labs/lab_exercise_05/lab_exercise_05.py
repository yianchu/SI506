# START LAB EXERCISE 05
import os
print('Lab Exercise 05 \n')


# PROBLEM 01


def read_file(filepath):
    """Reads text file and returns each line as a list element.
    Parameters:
        filepath (str): path to file
    Returns
        list: list of all lines in the file
    """
    f_name = 'project_data.txt'
    a = []
    with open(f_name, 'r', encoding='utf-8') as f:
        # print(f.readlines()).
        # print(type(f.readlines()))
        for line in f.readlines():
            a.append(line.strip('\n'))
        return a


filepath = 'project_data.txt'  # Gradescope
# read_file(filepath)
# Create filepath using the os module (COMMENT OUT BEFORE SUBMITTING TO GRADESCOPE)
#abs_path = os.path.dirname(os.path.abspath(__file__))
#filepath = os.path.join(abs_path, 'project_data.txt')

projects = read_file(filepath)
print(f"\n1.0 {projects}")
print(type(projects))

# PROBLEM 02


def get_filtered_projects(projects, categories):
    """
    This function returns a filtered list of projects based on one or more passed in categories.

    Parameters:
        projects (list): a list of strings that represent project information.
        categories (list): list of categories used as filters

    Returns:
        list: A filtered list of tuples. Each tuple contains both project name and project goal
    """
    filtered_projects = []
    for i in projects[1:]:
        a = i.split(",")
        if categories[0].lower() in a[0].lower():
            #print(categories[0] + categories[1])
            # print(a[0])
            filtered_projects.append(tuple(a[1:]))
        elif categories[1].lower() in a[0].lower():
            # print(a[0])
            filtered_projects.append(tuple(a[1:]))
    return filtered_projects
    # print(filtered_projects)

    # pass
#get_filtered_projects(projects, 'data')


categories = ['data', 'UI/UX']
#get_filtered_projects(projects, categories)
data_ux_projects = get_filtered_projects(projects, categories)

print(f"\n2.0 {data_ux_projects}")

# PROBLEM 03

# #write


def write_file(name, data):
    with open(name, 'w', encoding='utf-8') as s:
        for line in data:
            s.write(f"{line}\n")


name = 'data_ux_projects.txt'
write_file(name, data_ux_projects)
