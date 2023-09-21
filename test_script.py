from script import aggregate_statistics
import requests

def check_github_file_existence(owner, repo, path):
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

    response = requests.get(url)
    assert  response.status_code == 200


if __name__ == "__main__":
    owner = "nogibjj"
    repo = "IDS706_DataEngineering_BarbaraFlores_Project1"
    path1 = "total_applicants.png"
    check_github_file_existence(owner, repo, path1)
 