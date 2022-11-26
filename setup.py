from setuptools import setup, find_packages

setup(
    name='santa',
    version='0.2.0',
    packages=find_packages(include=['santa', 'santa.*'])
)
