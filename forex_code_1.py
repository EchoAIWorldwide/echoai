import requests
from config import GITHUB_ACCESS_TOKEN, GITHUB_REPO_OWNER, GITHUB_REPO_NAME

def create_file(file_name, file_content):
    url = f"https://api.github.com/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/contents/{file_name}"
    headers = {
        "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "message": f"Add {file_name}",
        "content": file_content
    }
    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"File {file_name} created successfully")
    else:
        print(f"Failed to create file {file_name}")
        print(f"Response: {response.content}")

if __name__ == '__main__':
    file_name = "forex_code_1.py"
    file_content = "forex code 1"
    create_file(file_name, file_content)
