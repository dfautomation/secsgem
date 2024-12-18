from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='secsgem',

    version='0.2.2',

    description='Python SECS/GEM implementation',

    url='https://github.com/bparzella/secsgem',
    download_url='https://github.com/bparzella/secsgem/tarball/v0.0.6',

    author='Benjamin Parzella',
    author_email='bparzella@gmail.com',

    license='LGPL',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='development hsms secs gem',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=[
        "python-dateutil",
        "transitions",
    ],
)
