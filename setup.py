#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
]

setup(
    author="Daniel Leuenberger",
    author_email='daniel.leuenberger@meteoswiss.ch',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Parses Fortran Namelists",
    entry_points={
        'console_scripts': [
            'f90nmlparse=f90nmlparse.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='f90nmlparse',
    name='f90nmlparse',
    packages=find_packages('src'),  # collect names of packages in ``src/``
    package_dir={'': 'src'},  # location of packages: ``src/<package>``
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/DanielLeuenberger/f90nmlparse',
    version='0.1.0',
    zip_safe=False,
)
