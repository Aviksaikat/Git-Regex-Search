import argparse
import threading
import os
import toml
import re
from github import Github
from termcolor import colored

# https://pygithub.readthedocs.io/en/latest/examples/Repository.html
def process_env():
    # Initialize the Github instance using your access token
    
    # Fetch the access token
    access_token = os.environ.get("GITHUB_TOKEN")
    #print(access_token)
    
    #* if not in env then fetch from config.toml file
    if access_token is None:
        try:
            with open("config.toml") as config_file:
                config = toml.load(config_file)
                access_token = config["github"]["access_token"]
        except (FileNotFoundError, KeyError):
            print("Error: Could not find access token in environment variable or config.toml file.")
            exit(1)
    g = Github(access_token)
    return g
    

def search_repo(repository, pattern) -> tuple:
    g = process_env()
    org = repository.split('/')[-2]
    repo_name = repository.split('/')[-1]
    repo = g.get_repo(org + '/' + repo_name)
    results = []

    def search_contents(contents):
        for item in contents:
            if item.type == "dir":
                search_contents(repo.get_contents(item.path))
            elif item.type == "file":
                file_contents = repo.get_contents(item.path).decoded_content
                for i, line in enumerate(file_contents.splitlines(), 1):
                    if re.search(pattern.encode(), line):
                        results.append((item, i))

    thread1 = threading.Thread(target=search_contents, args=(repo.get_contents(""),))
    thread2 = threading.Thread(target=search_contents, args=(repo.get_contents(""),))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    #print(results)
    return results


def git_regex_search(url, pattern):
    # print(type(args))
    # print(args)
    if url:
        if url.endswith(".txt"):
            # The URL is a file containing multiple URLs
            with open(url, "r") as file:
                urls = file.readlines()
                for url in urls:
                    try:
                        # repo = g.get_repo(url.strip())
                        # results = repo.search_code(pattern)
                        results = search_repo(url.strip(), pattern)
                        for result in results:
                            print(f"{url.strip()}/tree/master/{result[0].path}#L{result[1]}")
                    except Exception as e:
                        print(f"Error: {e}")
        else:
            # The URL is a single repository
            try:
                # repo = g.get_repo(args.url)
                # results = repo.search_code(pattern)
                results = search_repo(url, pattern)
                for result in results:
                    print(colored(f"{args.url}/tree/master/{result[0].path}#L{result[1]}", "magenta"))
            except Exception as e:
                print(f"Error: {e}")
    else:
        try:
            # repo = g.get_repo(args.repo)
            # results = repo.search_code(pattern)
            results = search_repo(args.repo, pattern)
            for result in results:
                print(colored(f"{args.repo}/tree/master/{result[0].path}#L{result[1]}", "green"))
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    # Initialize the argument parser
    parser = argparse.ArgumentParser()

    # Add the repository name argument
    #parser.add_argument("repo", required=False, help="Name of the repository to search in")

    # Add the URL option argument
    parser.add_argument("-u", "--url", help="URL of the repository (single or file containing URLs)")

    # Add the regex argument
    parser.add_argument("-r", "--regex", help="Regex pattern to search for")

    try:
        # Parse the command-line arguments
        args = parser.parse_args()
    except:
        exit(-2)

    # Set the pattern to search for
    if args.regex:
        pattern = args.regex
    else:
        pattern = "latestRoundData"
    
    if args.url:
        git_regex_search(args.url, pattern)
    else:
        print(colored("Print Something is wrong"), "red")
        exit(-3)