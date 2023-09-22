import pandas as pd
import matplotlib.pyplot as plt
from lib import mean_variable, median_variable, count_variable

def aggregate_statistics(path, variable_list):
    print(" \nSome descriptive statistics: \n")
    for i in variable_list:
        print(f"The mean of {i} is {round(mean_variable(path, i))}.")
        print(f"The median of {i} is {round(median_variable(path, i))}.")
        print(f"The count of {i} is {round(count_variable(path, i))}.\n")

def hist_plot(path, variable_list):
    print("Let's see how these variables behave when graphed with a histogram.")

    df = pd.read_csv(path) 
    for variable in variable_list:
        plt.hist(df[[variable]], bins=10,)
        plt.xlabel(variable)
        plt.ylabel('frequency')
        plt.title('Histogram of {0} per job posting'.format(variable))
        plt.savefig("{}.png".format(variable))
        plt.clf()


if __name__ == "__main__":
    aggregate_statistics(
        'LinkedInTechJobsDataset.csv', 
        ["Total_applicants", "Employee_count", "LinkedIn_Followers"]
        )
    hist_plot("LinkedInTechJobsDataset.csv", 
        ["Total_applicants", "Employee_count", "LinkedIn_Followers"]
        )
