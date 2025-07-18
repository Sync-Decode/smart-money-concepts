from setuptools import setup, find_packages
import codecs
import os

VERSION = "0.0.26"
DESCRIPTION = "Indicators based on Smart Money Concepts (ICT)"
README_FILE = "README.md"

# Read long description from README
here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, README_FILE), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="smartmoneyconcepts",
    version=VERSION,
    author="Joshua Attridge",
    author_email="joshua@example.com",  # optional, but good to have
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/joshyattridge/smartmoneyconcepts",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.2",
        "numpy>=1.24.3",
        "numba>=0.58.1"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    keywords="smart money concepts ict indicators trading forex stocks crypto",
    python_requires=">=3.8",
)
