import requests

def test_github_file_existence(name, repo, path_to_file):
    url = f"https://api.github.com/repos/{name}/{repo}/contents/{path_to_file}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"The file {path_to_file} exist in the repository.")
    elif response.status_code == 404:
        print(f"The file  {path_to_file} exist in the repository.")
    else:
        print(f"There was an issue verifying the existence of the file {path_to_file}.")
        print("Status code: {response.status_code}")

if __name__ == "__main__":
    name = "nogibjj" 
    repo = "IDS706_DataEngineering_BarbaraFlores_Project1"  
    path_to_file1 = "Total_applicants.png"  
    test_github_file_existence(name, repo, path_to_file1)
    path_to_file2 = "Employee_count.png"  
    test_github_file_existence(name, repo, path_to_file2)
    path_to_file3 = "LinkedIn_Followers.png"
    test_github_file_existence(name, repo, path_to_file3)
