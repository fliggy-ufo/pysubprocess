import os
import runpy
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

VERSION = runpy.run_path(
    os.path.join(here, "pysubprocess", "version.py")
)["VERSION"]

def read_requirements(name):
    with open(os.path.join(here, name), encoding='utf-8') as f:
        require_str = f.read()
        return require_str.split()

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pysubprocess',
    version=VERSION,
    packages=['pysubprocess'],
    url='https://github.com/fliggy-ufo/pysubprocess.git',
    author='youngfreeFJS',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts': [
            'psp = pysubprocess.manager:main'
        ]
    },
    install_requires=read_requirements('requirements.txt'),
    extras_require={
        'dev': read_requirements('requirements.dev.txt')
    }
)