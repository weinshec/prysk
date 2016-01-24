#!/usr/bin/env python
"""Installs cram"""

import os
import sys
from distutils.core import setup

COMMANDS = {}
CRAM_DIR = os.path.abspath(os.path.dirname(__file__))

try:
    from wheel.bdist_wheel import bdist_wheel
except ImportError:
    pass
else:
    COMMANDS['bdist_wheel'] = bdist_wheel

def long_description():
    """Get the long description from the README"""
    return open(os.path.join(sys.path[0], 'README.rst')).read()

setup(
    author='Brodie Rao',
    author_email='brodie@bitheap.org',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Unix Shell',
        'Topic :: Software Development :: Testing',
    ],
    cmdclass=COMMANDS,
    description='A simple testing framework for command line applications',
    download_url='https://bitheap.org/cram/cram-0.6.tar.gz',
    keywords='automatic functional test framework',
    license='GNU GPL',
    long_description=long_description(),
    name='cram',
    packages=['cram'],
    scripts=['scripts/cram'],
    url='https://bitheap.org/cram/',
    version='0.6',
)
