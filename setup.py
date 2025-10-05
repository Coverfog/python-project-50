from setuptools import find_packages, setup

setup(
    name='gendiff',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'gendiff=gendiff.scripts.gendiff:main',
        ],
    },
)
