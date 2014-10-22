#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


setup(
    name='Flask-HelloWorld',
    version='0.0.1',
    #url='http://github.com/rhyselsmore/flask-redis',
    author='Tang Chengliao',
    author_email='aliao0019@gmail.com',
    description='Hello-World Extension for Flask Applications',
    long_description=open('README').read(),
    py_modules=['flask_helloworld'],
    license=open('LICENSE').read(),
    package_data={'': ['LICENSE']},
    zip_safe=False,
    platforms='any',
    install_requires=[
        'setuptools',
        'Flask>=0.8',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
