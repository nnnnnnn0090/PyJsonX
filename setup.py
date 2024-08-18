from setuptools import setup, find_packages

DESCRIPTION = "PyJsonX data visualization of regression, classification and distribution"
NAME = 'PyJsonX'
AUTHOR = 'nnnnnnn0090'
AUTHOR_EMAIL = 'nnnnnnn0090@gmail.com'
URL = 'https://github.com/nnnnnnn0090/PyJsonX'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/nnnnnnn0090/PyJsonX'
VERSION = '0.0.1'
PYTHON_REQUIRES = ">=3.0"

def read_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

PACKAGES = find_packages()

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
]

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    long_description=read_readme(),
    long_description_content_type='text/markdown',
)
