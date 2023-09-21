from mylib.calculator import mean_variable, median_variable, count_variable

def aggregate_statistics(path, variable_list):
     for i in variable_list:
        print(f"The mean of variable {i} is {round(mean_variable('LinkedInTechJobsDataset.csv', i))}.")
        print(f"The median of variable {i} is {round(median_variable('LinkedInTechJobsDataset.csv', i))}.")
        print(f"The count of variable {i} is {round(count_variable('LinkedInTechJobsDataset.csv', i))}.")


if __name__ == "__main__":
    path = 'LinkedInTechJobsDataset.csv'
    variable_list = ["Total_applicants", "Employee_count", "LinkedIn_Followers"]

    aggregate_statistics(path, variable_list)
