import requests

def test_github_file_existence(owner, repo, path):
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

    response = requests.get(url)
    assert  response.status_code == 200

if __name__ == "__main__":
    owner = "nogibjj"
    repo = "IDS706_DataEngineering_BarbaraFlores_Project1"
    path1 = "Total_applicants.png"
    path2 = "Employee_count.png"
    path3 = "LinkedIn_Followers.png"
    test_github_file_existence(owner, repo, path1)
    test_github_file_existence(owner, repo, path2)
    test_github_file_existence(owner, repo, path3)
