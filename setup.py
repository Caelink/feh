from setuptools import setup
from setuptools import find_packages

setup(
    name='feh',
    version='0.0',
    description='Fire Emblem Heroes Python Board module',
    author='Caelin Jackson-King',
    author_email='caelink+feh@gmail.com',
    url='https://github.com/Caelink/feh',
    packages=find_packages(exclude=('tests*',)),
    install_requires=[
        'six',
    ],
)