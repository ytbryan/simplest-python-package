from setuptools import setup, find_packages

setup(
    name='suss_learning',
    version='0.1.0.alpha',
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        suss_learning=suss_learning.__main__:run
    ''', 
    license="BSD",  # TODO change the license
    classifiers=[
    ],
    install_requires=[
    ],
    tests_require=[
    ],
)
