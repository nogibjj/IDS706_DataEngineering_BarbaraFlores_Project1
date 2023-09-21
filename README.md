[![CI](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/actions/workflows/cicd.yml)

IDS706_DataEngineering_BarbaraFlores_Project1
## 📊🤖 Continuous Integration using GitHub Actions of Python Data Science Project

In this project, we delve into the world of Continuous Integration (CI), harnessing the power of GitHub Actions to streamline and improve the development process of a Python Data Science project. 
As a learning exercise for various data engineering tools, we will conduct an analysis of a database, including the following files:

- Jupyter Notebook [LinkedInTechJobs.ipynb](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project1/blob/main/LinkedInTechJobs.ipynb) with:
  - Cells that perform descriptive statistics using Polars or Panda.
  - Tested by using nbval plugin for pytest
- Python Script performing the same descriptive statistics using Polars or Panda
- lib.py file that shares the common code between the script and notebook
- Makefile with the following:
  - Run all tests (must test notebook and script and lib)
  - Formats code with Python black
  - Lints code with Ruff
  - Installs code via:  pip install -r requirements.txt
- test_script.py to test script
- test_lib.py to test library
- Pinned requirements.txt
- GitHub Actions performs all four Makefile commands with badges for each one in the README.md

### 🔍 Dataset: 
For this asigment, we will use the [LinkedIn Tech Jobs dataset](https://www.kaggle.com/datasets/joebeachcapital/linkedin-jobs?resource=download&select=final_data.csv) 

The [LinkedInTechJobsDataset.csv](LinkedInTechJobsDataset.csv) is a comprehensive collection of job listings and related information sourced from LinkedIn, one of the world's leading professional networking platforms. This dataset provides valuable insights into job opportunities, job market trends, and various attributes associated with job listings .
