from setuptools import find_namespace_packages,setup
from typing import List
def get_requirements(file_path:str) ->List[str]:
    '''
        This function will return the list of requirements
    '''
    reruirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements 
setup(
name='mlproject',
version='0.0.1',
author='Soumyajit',
author_email='das.samjit1999@gmail.com',
packages=find_namespace_packages(),
install_requires=get_requirements('requirements.txt')
)