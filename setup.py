# Copyright (C) 2010 Florian Ledermann ledermann@ims.tuwien.ac.at

from setuptools import setup, find_packages 
 
setup(
    name='django-content-feedback',
    version='0.1',
    description='A simple Django app providing feedback form to send feedback for any object in the database.',
    author='Flo Ledermann',
    author_email='ledermann@ims.tuwien.ac.at',
    url='http://bitbucket.org/floledermann/django-content-feedback/',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    # Make setuptools include all data files under version control,
    # svn and CVS by default
    # include_package_data=True,
    # zip_safe=False,
    # Tells setuptools to download setuptools_hg before running setup.py so
    # it can find the data files under Hg version control.
    # setup_requires=['setuptools_hg'],
)

