import pandas as pd
import re
from collections import Counter
def load_data():
    df = pd.read_csv('data/linkedin_jobs.csv')
    df = df[['posting_title','description']].dropna()
    return df
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text
skills_list = [
    'python','java','c++','sql','machine learning','deep learning','data science',
    'artificial intelligence','tensorflow','pytorch','nlp','power bi','tableau',
    'excel','aws','azure','cloud','devops','docker','kubernetes','react','node',
    'html','css','javascript','flask','django','git','linux','spark','hadoop'
]
def extract_skills(text):
    extracted = []
    for skill in skills_list:
        if skill in text:
            extracted.append(skill)
    return extracted
def get_trending_skills():
    df = load_data()
    df['clean_desc'] = df['description'].apply(clean_text)
    df['skills'] = df['clean_desc'].apply(extract_skills)

    all_skills = [skill for sublist in df['skills'] for skill in sublist]
    skill_counts = Counter(all_skills)

    return skill_counts.most_common(15)
def recommend_by_role(role):
    role = role.lower()
    df = load_data()
    matched_jobs = df[df['posting_title'].str.lower().str.contains(role)]

    if matched_jobs.empty:
        return ["No matching jobs found"]
    matched_jobs['clean_desc'] = matched_jobs['description'].apply(clean_text)
    matched_jobs['skills'] = matched_jobs['clean_desc'].apply(extract_skills)
    all_skills = [skill for sublist in matched_jobs['skills'] for skill in sublist]
    skill_counts = Counter(all_skills)
    return [skill for skill, count in skill_counts.most_common(10)]
