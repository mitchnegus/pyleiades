#!/usr/bin/env python3
DOCLINES = (__doc__ or '').split("\n")

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pyleiades',
    version='0.0.dev',
    description='An API for examing the EIA Monthly Energy Review datasets.',
    author='Mitch Negus',
    author_email='mitchell.negus.17@gmail.com',
    license='FreeBSD',
    long_description='\n'.join(DOCLINES),
    url='https://github.com/mitchnegus/pyleiades',
    packages=['pyleiades', 'pyleiades.utils'],
    scripts=['scripts/update_eia_data.py'],
    include_package_data=True
)
