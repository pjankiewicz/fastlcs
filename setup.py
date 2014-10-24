#!/usr/bin/env python

# Set this to True to enable building extensions using Cython.
# Set it to False to build extensions from the C file (that
# was previously created using Cython).
# Set it to 'auto' to build with Cython if available, otherwise
# from the C file.
USE_CYTHON = True


import sys

from distutils.core import setup
from distutils.extension import Extension

if USE_CYTHON:
    try:
        from Cython.Distutils import build_ext
    except ImportError:
        if USE_CYTHON=='auto':
            USE_CYTHON=False
        else:
            raise

cmdclass = { }
ext_modules = [ ]
base_dir = 'python'

if USE_CYTHON:
    ext_modules += [
        Extension("fastlcs._cython", [ "cython/fastlcs.pyx" ])
    ]
    cmdclass.update({ 'build_ext': build_ext })
else:
    ext_modules += [
        Extension("fastlcs._cython", [ "cython/fastlcs.c" ])
    ]

setup(
    name='fastlcs',
    version="0.1",
    description='Fast Longest Common Substring',
    author='Pawel Jankiewicz',
    author_email='p.jankiewicz',
    url='https://github.com/pjankiewicz/fastlcs',
    packages=[ 'fastlcs' ],
    package_dir={
        'fastlcs' : base_dir,
    },
    cmdclass = cmdclass,
    ext_modules = ext_modules,

    long_description=open('README.md').read(),

    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
    keywords='lcs longest common substring',
)
