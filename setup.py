from distutils.core import setup
from os import path

MAJOR = 0
MINOR = 2
PATCH = 0

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.rst'), encoding='utf-8') as fp:
    README = fp.read()

setup(
    name='santa',
    packages=['santa'],
    version='{}.{}.{}'.format(MAJOR, MINOR, PATCH),
    description='Assign a secret santa over email',
    long_description=README,
    author='jarhill0',
    author_email='jarhill0@gmail.com',
    url='https://github.com/jarhill0/santa/',
    download_url='https://github.com/jarhill0/santa/archive/{}.{}.{}.tar.gz'.format(MAJOR, MINOR, PATCH),
    keywords=['secret', 'santa', 'email'],
    classifiers=[],
    install_requires=[
        'yagmail >=0.10.209',
    ]
)
