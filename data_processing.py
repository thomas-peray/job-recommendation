"""
Data Processing for Job Profiles

This script processes a dataset of job profiles. It uses the csv module to read the data.

The script requires the Python csv module.

The script assumes that there is a CSV file in the specified filepath. This file should contain job profiles.

Functions:
    exp_to_range(exp)
    salary_to_range(salary)
    genre_to_int(genre)
    load_data(filepath)
"""
import csv

"""
    Convert the experience range into a tuple of minimum and maximum values.

    Parameters:
        exp (str): The experience range.

    Returns:
        tuple: The minimum and maximum experience.
"""
def exp_to_range(exp: str) -> (int, int):
    exp = exp[0:len(exp) - 6]
    exp_split = exp.split(" to ")
    min_range = int(exp_split[0])
    max_range = int(exp_split[1])
    return min_range, max_range

"""
    Convert the salary range into a tuple of minimum and maximum values.

    Parameters:
        salary (str): The salary range.

    Returns:
        tuple: The minimum and maximum salary.
"""
def salary_to_range(salary: str) -> (int, int):
    salary = salary[1:len(salary) - 1]
    salary_split = salary.split("K-$")
    min_range = int(salary_split[0])
    max_range = int(salary_split[1])
    return min_range, max_range

"""
    Convert the genre into an integer.

    Parameters:
        genre (str): The genre.

    Returns:
        int: The integer representation of the genre.
"""
def genre_to_int(genre: str) -> int:
    return 0 if genre == "Female" else 1

"""
    Load the data from a CSV file.

    Parameters:
        filepath (str): The path to the CSV file.

    Returns:
        tuple: A tuple containing two lists. The first list contains the evidence (features) and the second list contains the labels (targets).
"""
def load_data(filepath: str) -> (list, list):
    evidence: str = []
    labels: str = []

    with open(filepath, 'r') as raw:
        reader = csv.DictReader(raw)
        for each_row in reader:
            row: list = []
            min_range, max_range = exp_to_range(each_row["Experience"])
            row.append(min_range)
            row.append(max_range)

            row.append(str(each_row["Qualifications"]))

            min_range, max_range = salary_to_range(each_row["Salary Range"])
            row.append(min_range)
            row.append(max_range)

            row.append(str(each_row["location"]))
            row.append(str(each_row["Country"]))
            row.append(int(each_row["Company Size"]))
            row.append(genre_to_int(each_row["Preference"]))

            evidence.append(row)

            labels.append(str(each_row["Job Title"]))

    return evidence, labels
