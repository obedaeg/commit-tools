from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.3.0"

setup(
    name='etl',
    version=__version__,
    python_requires='>=3.6.5',
    description="test",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Obed Espinoza",
    author_email="obedaeg@gmail.com",
    classifiers=[
        'Programming Language :: Python :: 3.7'
    ],

    packages=find_packages(),

    setup_requires=[],
    install_requires=[

    ],
    include_package_data=True,
    package_data={

    },
    entry_points={
        'console_scripts': [
            'etl=etl.main:main',
        ]
    }
)

