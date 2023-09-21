from mylib.calculator import mean_variable, median_variable, count_variable

def aggregate_statistics(path, variable_list):
    for i in variable_list:
        print(f"The mean of variable {i} is {round(mean_variable(path, i))}.")
        print(f"The median of variable {i} is {round(median_variable(path, i))}.")
        print(f"The count of variable {i} is {round(count_variable(path, i))}.")


if __name__ == "__main__":
    aggregate_statistics('LinkedInTechJobsDataset.csv', ["Total_applicants", "Employee_count", "LinkedIn_Followers"])
