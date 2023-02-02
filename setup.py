from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION = "\n" + fh.read()

CLASSIFIERS=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]

DESCRIPTION = "This program allows you to search for a specific pattern within the files of a GitHub repository(using PyGithub)."
# LONG_DESCRIPTION = "This program allows you to search for a specific pattern within the files of a GitHub repository(using PyGithub). The program utilizes regular expressions and multithreading to quickly search through the repository's contents and return all files that contain the specified pattern."

setup(
    name="git_regex_search",
    version="1",
    author="Aviksaikat (Saikat Karmakar)",
    author_email="<aviksaikat@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "toml",
        "re",
        "PyGithub",
        "termcolor"
    ],
    classifiers=CLASSIFIERS,
)
