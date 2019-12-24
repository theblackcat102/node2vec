import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.md').read()

requirements = [
    'wheel>=0.23.0',
    'Cython>=0.20.2',
    'argparse>=1.2.1',
    'six>=1.7.3',
    'numpy>=1.11.2',
    'gensim>=1.0.0',
    'scipy>=0.15.0',
    'psutil>=2.1.1',
    'networkx>=2.0',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='node2vec',
    version='1.0.0',
    description='The *node2vec* algorithm learns continuous representations for nodes in any (un)directed, (un)weighted graph',
    long_description=readme + '\n\n',
    author='Aditya Grover',
    url='https://github.com/aditya-grover/node2vec',
    packages=[
        'node2vec',
    ],
    entry_points={'console_scripts': ['node2vec = node2vec.__main__:main']},
    package_dir={'node2vec':
                 'node2vec'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='node2vec',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)