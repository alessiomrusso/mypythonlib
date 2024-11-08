from setuptools import find_packages, setup

__version__ = "0.1.0"

setup(
    name='mypythonlib',
    packages=find_packages(include=['mypythonlib']),
    version=__version__,
    description='My first Python library',
    author='Me',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)