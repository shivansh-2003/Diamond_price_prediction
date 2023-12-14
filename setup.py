from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        file_obj.readlines()
        requirement=[req.replace("\n","")for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

        return requirement

setup(
    name='Diamond price prediction',
    version='0.0.1',
    author='ShivanshMahajan',
    author_email='shivansh.m2003@gmail.com',
    install_requirement=get_requirements('requirement.txt'),
    packages=find_packages()
)