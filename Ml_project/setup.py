from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Machine Learning Project"
VERSION = '0.0.1'
AUTHOR = 'Naveed Ansari'
DESCRIPTION = 'This is our Machine Learning project'
REQUIREMETNS_FILE_NAME = 'requirements.txt'
Hyphen_e_dot = '-e .'
def get_requirements_list() -> List[str]:
    with open (REQUIREMETNS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace('\n','') for requirement_name in requirement_list]
        if Hyphen_e_dot in requirement_list:
            requirement_list.remove(Hyphen_e_dot)
        return requirement_list

setup(
    name= PROJECT_NAME,
    version= VERSION,
    author= AUTHOR,
    description=DESCRIPTION,
    packages= find_packages(),
    install_requires = get_requirements_list()

)