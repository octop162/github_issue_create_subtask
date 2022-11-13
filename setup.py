from setuptools import setup, find_packages

setup(
    name='gh-subtask',
    version='0.0.1',
    packages=find_packages(where='src'),
    install_requires=['fire'],
    entry_points={
        "console_scripts": [
            "gh-subtask=src.main:entry",
        ],
    },
)