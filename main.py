"""
Main cli or app entry point
"""

from mylib.calculator import mean_variable, median_variable, count_variable


if __name__ == "__main__":
    for i in ["Total_applicants", "Employee_count", "LinkedIn_Followers"]:
        print(f"The mean of variable {i} is {round(mean_variable('LinkedInTechJobsDataset.csv', i))}.")
    print()
    for i in ["Total_applicants", "Employee_count", "LinkedIn_Followers"]:
        print(f"The median of variable {i} is {round(median_variable('LinkedInTechJobsDataset.csv', i))}.")
    print()
    for i in ["Total_applicants", "Employee_count", "LinkedIn_Followers"]:
        print(f"The count of variable {i} is {round(count_variable('LinkedInTechJobsDataset.csv', i))}.")
