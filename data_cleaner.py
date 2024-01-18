import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# Load the dataset
df = pd.read_csv('job_profiles.csv')

# Define English stopwords
stopw = set(stopwords.words('english'))


# Define conversion functions
def convert_salary(value):
    if 'Unknown' in value:
        return None
    elif '-' in value:
        values = re.findall(r'\$\d+K', value)
        min_value = int(values[0].replace('$', '').replace('K', '')) if values else None
        max_value = int(values[1].replace('$', '').replace('K', '')) if len(values) > 1 else None
        if min_value and max_value:
            return (min_value + max_value) / 2
        elif min_value:
            return min_value
        elif max_value:
            return max_value
        else:
            return None
    else:
        return int(re.findall(r'\$\d+K', value)[0].replace('$', '').replace('K', ''))


def convert_size(value):
    if isinstance(value, int):
        return value
    elif 'Unknown' in value:
        return None
    elif ' to ' in value:
        sizes = value.split(' to ')
        min_size = int(sizes[0].replace('+', '').replace(',', '').split()[0])
        max_size = int(sizes[1].replace('+', '').replace(',', '').split()[0])
        return (min_size + max_size) / 2
    else:
        return int(value.replace('+', '').replace(',', '').split()[0])


def exp_to_range(exp: str) -> (int, int):
    exp = exp[0:len(exp) - 6]
    exp_split = exp.split(" to ")
    min_range = int(exp_split[0])
    max_range = int(exp_split[1])
    return min_range, max_range


def convert_experience(value):
    if 'Unknown' in value:
        return None
    elif ' to ' in value:
        return exp_to_range(value)
    else:
        exp_value = int(value.replace(' Years', ''))
        return exp_value, exp_value


# Apply conversion functions
df['Experience'] = df['Experience'].apply(convert_experience)
df['Salary Range'] = df['Salary Range'].apply(convert_salary)
df['Company Size'] = df['Company Size'].apply(convert_size)

# Additional processing of 'Job Description' and 'Company Profile' columns
df['Processed_JD'] = df['Job Description'].apply(
    lambda x: ' '.join([word for word in str(x).split() if len(word) > 2 and word not in stopw]))

# Select specified columns
selected_columns = ['Experience', 'Qualifications', 'Salary Range', 'location', 'Country', 'Work Type', 'Preference',
                    'Job Title', 'Role', 'Job Description', 'Benefits', 'skills', 'Responsibilities']

# Create a new DataFrame with selected columns
new_df = df[selected_columns]

# Drop rows with null values in 'Salary Range'
new_df = new_df.dropna(subset=['Salary Range'])

# Save the new DataFrame to a CSV file
new_df.to_csv('structured_data.csv', index=False)
