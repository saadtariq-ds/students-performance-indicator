from typing import List
from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file=file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [requirement.replace("\n", "") for requirement in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="students_performance_indicator",
    version="0.0.1",
    author="Saad",
    author_email="tariqsaad1997@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)