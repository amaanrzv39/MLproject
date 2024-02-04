from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements = []
    with open(filepath) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    return requirements


setup(
    name = 'MLproject',
    version = '0.0.1',
    author = 'Amaan',
    author_email = 'amaan.rizvi39@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirement.txt')
)