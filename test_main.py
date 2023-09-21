"""
Test goes here

"""
import pandas as pd
from mylib.calculator import mean_variable, median_variable, count_variable

#def test_add():
 #   assert add(1, 2) == 3
def check_mean_variable(path, variable):
    df = pd.read_csv(path)
    if mean_variable(path, variable) ==  df[variable].mean():
        return True
    else:
        raise Exception(
            "houston we have a problem"   
        )   
    
def check_median_variable(path, variable):
    df = pd.read_csv(path)
    if median_variable(path, variable) ==  df[variable].median():
        return True
    else:
        raise Exception(
             "houston we have a problem"    
        )      

def check_count_variable(path, variable):
    df = pd.read_csv(path)
    if count_variable(path, variable) == df[variable].sum() / df[variable].mean() :
        return True
    else:
        raise Exception(
             "houston we have a problem"   
        )      
    
if __name__ == "__main__":
    assert check_mean_variable("LinkedInTechJobsDataset.csv","Total_applicants")
    assert check_median_variable("LinkedInTechJobsDataset.csv","Total_applicants")
    assert check_count_variable("LinkedInTechJobsDataset.csv","Total_applicants")
