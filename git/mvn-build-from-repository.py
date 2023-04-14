import json
import os
import shutil
from pathlib import Path

from git import Git
from git import Repo

with open('repositories.json') as data_file:
    data = json.load(data_file)

home = str(Path.home())
tmp_repo_path = f"{home}/pipe_repositories"


class Repository:
    def __init__(self, name, url):
        self.path = f"{tmp_repo_path}/{name}"
        self.url = url
        self.g = Git()

    def clone_repo(self):
        repo = Repo.clone_from(self.url, self.path)
        return repo

    def checkout_branch(self, branch):
        self.g.checkout(branch)

    def chdir_repo_directory(self):
        os.chdir(self.path)


def get_current_branch():
    repo = Repo()
    try:
        active_branch = repo.active_branch
    except Exception as exp:
        print(exp)
        active_branch = 'DETACHED_' + repo.head.object.hexsha
    return active_branch


def get_tags():
    repo = Repo()
    return repo.tags


def clean_up():
    shutil.rmtree(tmp_repo_path)


repositories_list = []
for item_list in data['repositories']:
    repositories_list.append(item_list)

for repository in repositories_list:
    item_name = data['repositories'][repository]['name']
    item_url = data['repositories'][repository]['url']
    item_cmd = data['repositories'][repository]['cmd']
    item_branches = data['repositories'][repository]['branches']
    except_items = data['repositories'][repository]['exceptions']
    item_repo = Repository(item_name, item_url)
    repo_exists = os.path.exists(item_name)
    if repo_exists:
        print(f"Repository {item_name} already present locally")
    else:
        try:
            item_repo.clone_repo()
        except Exception as e:
            print(e)
    item_repo.chdir_repo_directory()
    tags = get_tags()

    # Build from specified branches
    for item_branch in item_branches:
        if str(item_branch) not in except_items:
            print(f"Building {item_name} from BRANCH {item_branch}")
            try:
                item_repo.checkout_branch(item_branch)
                os.system(item_cmd)
            except Exception as e:
                print(e)

    # Build from tags (releases)
    for tag in tags:
        if str(tag) not in except_items:
            print(f"Building {item_name} from TAG {tag}")
            try:
                item_repo.checkout_branch(tag)
                os.system(item_cmd)
            except Exception as e:
                print(e)
    # Change to previous directory
    os.chdir("..")

# Clean up
try:
    clean_up()
except Exception as e:
    print(e)
