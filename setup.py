# -*- coding: utf-8 -*-
# Author: Forrest Smith
from setuptools import setup


setup(name='rpi',
      version='0.1',
      description='A small collection of raspberrypi related modules',
      url='https://github.com/ephsmith/rpi',
      author='Forrest Smith',
      author_email='fasmith0229@gmail.com',
      license='MIT',
      packages=['rpi'],
      install_requires=[
          'pyserial',
          'guizero',
          ],
      zip_safe=False)
