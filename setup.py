
from setuptools import setup, find_packages

setup(
    name='vwpylib',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/',
    author='',
    author_email='myemail@example.com'
)
