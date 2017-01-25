from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Kerapu',

    version='0.9.10',

    description='Een implementatie van de grouper',
    long_description=long_description,

    url='https://github.com/SetBased/py-kerapu',

    author='Paul Water',
    author_email='p.r.water@setbased.nl',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',
        'Natural Language :: Dutch',
        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='DBC,Grouper',

    packages=find_packages(exclude=['build', 'test']),

    entry_points={
       'console_scripts': [
           'kerapu = kerapu.Shredder:main',
       ],
    },

    requires=['lxml', 'cleo==0.5.0']
)
