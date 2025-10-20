from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements file and returns a list of packages.
    """
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='mlprojects',
    version='0.0.1',
    author='Saniatiku',
    author_email='saneeatiku14@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
