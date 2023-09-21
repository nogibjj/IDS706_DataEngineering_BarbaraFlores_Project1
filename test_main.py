import pandas as pd
import main
from mylib.calculator import mean_variable, median_variable, count_variable

    
#if __name__ == "__main__":
assert mean_variable("data_test.csv", "age") == 32
assert median_variable("data_test.csv", "age") == 30
assert count_variable("data_test.csv", "age") == 5


