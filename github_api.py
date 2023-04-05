import requests
import json
from config import GITHUB_ACCESS_TOKEN, GITHUB_REPO_OWNER, GITHUB_REPO_NAME

# Function to create a new repository
def create_repo(repo_name):
    url = f"https://api.github.com/user/repos"
    headers = {
        "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print(f"Repository {repo_name} created successfully")
    else:
        print(f"Failed to create repository {repo_name}")
        print(f"Response: {response.content}")
        
# Function to update an existing repository
def update_repo(repo_name, description):
    url = f"https://api.github.com/repos/{GITHUB_REPO_OWNER}/{repo_name}"
    headers = {
        "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "description": description
    }
    response = requests.patch(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print(f"Repository {repo_name} updated successfully")
    else:
        print(f"Failed to update repository {repo_name}")
        print(f"Response: {response.content}")
        
# Function to create a new issue in a repository
def create_issue(repo_name, title, body):
    url = f"https://api.github.com/repos/{GITHUB_REPO_OWNER}/{repo_name}/issues"
    headers = {
        "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "title": title,
        "body": body
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print(f"Issue '{title}' created successfully in repository {repo_name}")
    else:
        print(f"Failed to create issue '{title}' in repository {repo_name}")
        print(f"Response: {response.content}")
