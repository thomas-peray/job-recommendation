import re
from ftfy import fix_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd
from nltk.corpus import stopwords

# Load dataset:
jd_df = pd.read_csv('structured_data.csv')

# Define stop words
stopw = set(stopwords.words('english'))

# Load the extracted resume skills:
file_path = 'profile_resume.txt'

# Read the content of the resume text file
with open(file_path, 'r') as file:
    resume_content = file.read()

# Extract information from the structured text file
experience = re.search(r'Experience : "(\d+)', resume_content).group(1)
qualifications = re.search(r'Qualifications\s*:\s*"([^"]*)"', resume_content).group(1)
salary_range = re.search(r'Salary Range\s*:\s*"([^"]*)"', resume_content).group(1)
location = re.search(r'location\s*:\s*"([^"]*)"', resume_content).group(1)
country = re.search(r'Country\s*:\s*"([^"]*)"', resume_content).group(1)
work_type = re.search(r'Work Type\s*:\s*"([^"]*)"', resume_content).group(1)

# Create a dictionary to represent the resume information
resume_info = {
    'Experience': experience,
    'Qualifications': qualifications,
    'Salary Range': salary_range,
    'location': location,
    'Country': country,
    'Work Type': work_type,
}

# Convert the dictionary to a DataFrame
resume_df = pd.DataFrame([resume_info])


def ngrams(string, n=3):
    string = fix_text(string)  # fix text
    string = string.encode("ascii", errors="ignore").decode()  # remove non-ascii chars
    string = string.lower()
    chars_to_remove = [")", "(", ".", "|", "[", "]", "{", "}", "'"]
    rx = '[' + re.escape(''.join(chars_to_remove)) + ']'
    string = re.sub(rx, '', string)
    string = string.replace('&', 'and')
    string = string.replace(',', ' ')
    string = string.replace('-', ' ')
    string = string.title()  # normalize case - capital at start of each word
    string = re.sub(' +', ' ', string).strip()  # get rid of multiple spaces and replace with a single
    string = ' ' + string + ' '  # pad names for ngrams...
    string = re.sub(r'[,-./]|\sBD', r'', string)
    ngrams = zip(*[string[i:] for i in range(n)])
    return [''.join(ngram) for ngram in ngrams]


vectorizer = TfidfVectorizer(min_df=1, analyzer=ngrams, lowercase=False)
tfidf = vectorizer.fit_transform(resume_df['Qualifications'].astype('U'))

nbrs = NearestNeighbors(n_neighbors=1, n_jobs=-1).fit(tfidf)
jd_test = jd_df['Qualifications'].astype('U').values


def getNearestN(query):
    queryTFIDF_ = vectorizer.transform(query)
    distances, indices = nbrs.kneighbors(queryTFIDF_)
    return distances, indices


distances, indices = getNearestN(jd_test)
matches_df = pd.DataFrame({'Match confidence': distances.flatten()})
jd_df['Match confidence'] = matches_df['Match confidence']
recommended_jobs = jd_df.sort_values('Match confidence').head(5)
pd.set_option('display.max_columns', None)
print(recommended_jobs.head(5))
