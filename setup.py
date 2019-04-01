#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as history_file:
    history = history_file.read()

requirements = [
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
]

setup(
    name='fightfor_alembic',
    version='0.10.0',
    description="Alembic migrations for the fightfor project.",
    long_description=readme + '\n\n' + history,
    author="Adamos Kyriakou",
    author_email='adam@bearnd.io',
    url='https://github.com/somada141/fightfor_alembic',
    packages=find_packages(include=['ffalembic']),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='fightfor_alembic',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
