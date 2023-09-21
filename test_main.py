import pandas as pd
from mylib.calculator import mean_variable, median_variable, count_variable

    
#if __name__ == "__main__":

def test_mean():
    assert mean_variable("data_test.csv", "age") == 32

def test_median():
    assert median_variable("data_test.csv", "age") == 30

def test_count_variable():
    assert count_variable("data_test.csv", "age") == 5



