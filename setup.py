from setuptools import setup

setup(
    name='authority',  
    version='1.0',
    py_modules=['authority'],  
    install_requires=[
        'pyfiglet',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'authority = authority:main',
        ],
    },
)

