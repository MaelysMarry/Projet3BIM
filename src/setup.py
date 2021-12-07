#!/usr/bin/env python

import setuptools
from distutils.core import setup

setup(name='Bacteria',
      version='1',
      description='See evolution bacteria population with antibioresistance',
      author='Maelys',
      author_email='maelys.marry@insa-lyon.fr',
      url='https://github.com/MaelysMarry/Projet3BIM',
      py_modules=['ourCode'],
      license_files = '../LICENSE',
      install_requires = ['numpy==1.17', 'matplotlib'])
