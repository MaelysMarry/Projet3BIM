#!/usr/bin/env python

import setuptools
from distutils.core import setup

setup(name='HandsOnDeployAPackage',
      version='1.7',
      description='Hands-on: deploy a Python package',
      author='Maelys',
      author_email='maelys.marry@insa-lyon.fr'
      url='https://github.com/MaelysMarry/Projet3BIM',
      py_modules=['ourCode'],
      license_files = '../LICENSE',
      install_requires = ['matplotlib>=3.5.0', 'numpy', 'math'])
