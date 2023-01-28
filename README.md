# GitHub Search Using Regex

> Saikat Karmakar | 28 Jan:2023

---

This program allows you to search for a specific pattern within the files of a GitHub repository([Using PyGithub](https://pygithub.readthedocs.io/en/latest/)). The program utilizes regular expressions and multithreading to quickly search through the repository's contents and return all files that contain the specified pattern.

# Features
- Search for a specific pattern in the files of a GitHub repository
- Supports single repository or file containing multiple repository URLs
- Uses multithreading to improve search performance


# Installation
```bash
# using pip
pip install git-regex-search==0.2
```

To use this program, you will need to have Python 3 and the PyGithub library installed. You can install PyGithub using pip:
```bash
pip3 install -r requirements.txt
```

You will also need to have a GitHub personal access token. You can create one by going to the [GitHub Developer Settings](https://github.com/settings/tokens).

# Usage
To use the program, you will need to provide a GitHub access token. The token can be passed as an environment variable or in a config.toml file. The program will look for the token in the following order:

- `GITHUB_TOKEN` environment variable 
- `config.toml` file

```bash
python3 git_regex_search.py -h                                              
usage: git_regex_search.py [-h] [-u URL] [-r REGEX]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL of the repository (single or file
                        containing URLs)
  -r REGEX, --regex REGEX
                        Regex pattern to search for
```

For example, to search for the pattern `brownie` in the repository `Aviksaikat/RoadClosed-quillctf-brownie`, you would run the following command:

```bash
python3 git_regex_search.py -u https://github.com/Aviksaikat/RoadClosed-quillctf-brownie -r "brownie"
```

![](assets/img.png)


The program will then return a list of all files that contain the specified pattern, along with the line number where the pattern was found.

# Multithreading
The program utilizes multithreading to search through the repository's contents more quickly. Two threads are created and run simultaneously, each searching through the repository's contents. This allows the program to search through the repository's contents much faster than if it were only using a single thread.

# Regular Expressions
The program utilizes regular expressions to search for the specified pattern within the files of the repository. This allows for more powerful and flexible searches, as opposed to simple string matching.


# Docker
You can build the image by running the following command in the same directory where the Dockerfile is located:
```bash
docker build -t <image-name> .
```

You can then run the container using the following command:
```bash
docker run -e GITHUB_TOKEN=<access_token> <image-name>
```

# Limitations
This program only searches the contents of the files and not the name of the files. For my use I don't need it to search the names.

# Additional Features
The program also prints the whole file path where the pattern was found, which is helpful in identifying the location of the pattern.

# Conclusion
This program is a powerful tool for quickly searching through the contents of a GitHub repository and finding specific patterns. With the use of regular expressions and multithreading, it is able to search through large repositories quickly and efficiently.

# Version 0.2
Published as pip package
- https://pypi.org/project/git-regex-search/0.2/