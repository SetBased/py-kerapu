from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as handle:
    long_description = handle.read()

setup(
    name='Kerapu',

    version='2.0.3',

    description='Een implementatie van de grouper',
    long_description=long_description,

    url='https://github.com/SetBased/py-kerapu',

    author='Paul Water',
    author_email='p.r.water@setbased.nl',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',
        'Natural Language :: Dutch',
        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    keywords='DBC Grouper',

    packages=find_packages(exclude=['build', 'test']),

    entry_points={
       'console_scripts': [
           'kerapu = kerapu.application.kerapu:main',
       ],
    },

    install_requires=['cleo==0.6.8',
                      'lxml<5, >=4.6.1']
)
