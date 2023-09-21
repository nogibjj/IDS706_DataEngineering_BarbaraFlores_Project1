import pandas as pd
import matplotlib.pyplot as plt
from mylib.calculator import mean_variable, median_variable, count_variable

def aggregate_statistics(path, variable_list):
    for i in variable_list:
        print(f"The mean of variable {i} is {round(mean_variable(path, i))}.")
        print(f"The median of variable {i} is {round(median_variable(path, i))}.")
        print(f"The count of variable {i} is {round(count_variable(path, i))}.")

def hist_plot(path,variable):
    df = pd.read_csv(path) 
    plt.hist(df[[variable]], bins=10,)
    plt.xlabel(variable)
    plt.ylabel('frequency')
    plt.title('Histogram of {0} per job posting'.format(variable))
    plt.savefig("{}.png".format(variable))


if __name__ == "__main__":
    aggregate_statistics('LinkedInTechJobsDataset.csv', ["Total_applicants", "Employee_count", "LinkedIn_Followers"])
    hist_plot("LinkedInTechJobsDataset.csv", "Total_applicants")
