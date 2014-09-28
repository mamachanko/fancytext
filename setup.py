#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='fancytext',
    version='0.1.0',
    description='Fancifies text.',
    long_description=readme + '\n\n' + history,
    author='Max Brauer',
    author_email='max@rootswiseyouths.com',
    url='https://github.com/mamachanko/fancytext',
    packages=[
        'fancytext',
    ],
    package_dir={'fancytext':
                 'fancytext'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='fancytext',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)