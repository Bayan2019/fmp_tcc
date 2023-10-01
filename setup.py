#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Alexandre Courtois Auberger, Bayan Saparbayeva, and Vish Patel",
    author_email='saparbayevabt@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A package for aggregating data from FMP.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='fmp_tcc',
    name='fmp_tcc',
    packages=find_packages(include=['fmp_tcc', 'fmp_tcc.*']),
    install_requires=[
        'numpy>=1.10',
        'pandas',
        'datetime',
        'python-dateutil',
        'statsmodels',
        'urllib3',
        'certifi',
        'plotly',
        'json5'
    ],
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Bayan2019/fmp_tcc',
    version='0.1.0',
    zip_safe=False,
)