import os
from setuptools import setup, find_packages

constants = open('lib/evernote/edam/userstore/constants.py').read().split("\n")
for x in [x for x in constants if x.startswith('EDAM_VERSION')]:
    exec(x)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='evernote',
    version="{major}.{minor}.1".format(major=EDAM_VERSION_MAJOR,
                                       minor=EDAM_VERSION_MINOR),
    author='Evernote Corporation',
    author_email='api@evernote.com',
    url='http://dev.evernote.com',
    description='Evernote SDK for Python',
    long_description=read('README.md'),
    packages=find_packages('lib'),
    package_dir={'': 'lib'},
    classifiers=[
        'Development Status :: 4 - Production/Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3'
    ],
    license='BSD',
    install_requires=[
        'oauthlib',
        'requests_oauthlib'
    ],
)
