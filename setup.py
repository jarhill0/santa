from distutils.core import setup

setup(
    name='santa',
    packages=['santa'],
    version='0.1.1',
    description='Assign a secret santa over email',
    author='jarhill0',
    author_email='jarhill0@gmail.com',
    url='https://github.com/jarhill0/santa/',
    download_url='https://github.com/jarhill0/santa/archive/0.1.1.tar.gz',
    keywords=['secret', 'santa', 'email'],
    classifiers=[],
    install_requires=[
        'yagmail >=0.10.209',
    ]
)
