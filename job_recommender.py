import re
from ftfy import fix_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd


def predict(profile: dict):
    def getNearestN(query):
        queryTFIDF = vectorizer.transform(query)
        distances, indices = nbrs.kneighbors(queryTFIDF)
        return distances, indices

    # Load dataset:
    jd_df = pd.read_csv('job_profiles.csv')

    # Convert the dictionary to a DataFrame
    resume_df = pd.DataFrame([profile])

    # Combine the extracted information into a single string:
    resume_text = f"{profile['Experience']} {profile['Qualifications']} {profile['Salary Range']} {profile['Skills']}"
    
    vectorizer = TfidfVectorizer(min_df=1, analyzer=ngrams, lowercase=False)
    tfidf = vectorizer.fit_transform([resume_text])

    nbrs = NearestNeighbors(n_neighbors=1, n_jobs=-1).fit(tfidf)
    jd_test = jd_df['Job Description'].astype('U').values
    
    distances, indices = getNearestN(jd_test)
    test = list(jd_test)
    matches = []

    for i, j in enumerate(indices):
        dist = round(distances[i][0], 2)
        temp = [dist]
        matches.append(temp)

    distances, indices = getNearestN(jd_test)
    matches_df = pd.DataFrame({'Match confidence': distances.flatten()})
    jd_df['Match confidence'] = matches_df['Match confidence']
    recommended_jobs = jd_df.sort_values('Match confidence').head(5)
    pd.set_option('display.max_columns', None)
    
    top5 = recommended_jobs.head(5)
    
    return top5.to_dict('records')
    
    
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
    string = string.title()  # normalize case - capital at the start of each word
    string = re.sub(' +', ' ', string).strip()  # get rid of multiple spaces and replace with a single
    string = ' ' + string + ' '  # pad names for ngrams...
    string = re.sub(r'[,-./]|\sBD', r'', string)
    ngrams = zip(*[string[i:] for i in range(n)])
    return [''.join(ngram) for ngram in ngrams]


