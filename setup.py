#!/usr/bin/env python

from setuptools import setup, find_packages

classifiers = [
# Get more strings from
# http://pypi.python.org/pypi?%3Aaction=list_classifiers
"License :: OSI Approved :: MIT License",
"Natural Language :: English",
"Operating System :: OS Independent",
"Programming Language :: Python",
"Programming Language :: Python :: 2",
"Programming Language :: Python :: 2.6",
"Programming Language :: Python :: 2.7",
"Programming Language :: Python :: 3",
"Programming Language :: Python :: 3.2",
"Programming Language :: Python :: 3.3",
"Programming Language :: Python :: 3.4",
]

setup(name="nanpy",
      version="0.9.4",
      description="Use your Arduino board with Python",
      license="MIT",
      author="Andrea Stagi",
      author_email="stagi.andrea@gmail.com",
      url="http://github.com/nanpy/nanpy",
      packages = find_packages(),
      keywords= "arduino library prototype",
      install_requires=[
        "pyserial",
      ],
      classifiers=classifiers,
      zip_safe = True)
