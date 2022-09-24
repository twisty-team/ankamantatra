from setuptools import setup

setup(
    entry_points = {
        'console_scripts': ['ankamantatra=ankamantatra.__main__:main' ],
    }
)