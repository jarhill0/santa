from distutils.core import setup

MAJOR = 0
MINOR = 1
PATCH = 3

setup(
    name='santa',
    packages=['santa'],
    version='{}.{}.{}'.format(MAJOR, MINOR, PATCH),
    description='Assign a secret santa over email',
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
