import requests as r
from datetime import datetime

skills =  ["python", "machine learning", "data analysis", "sql"]

current_date = datetime.now().date()

url = "https://api.example.com/data"

try:
    response = r.get(url)
    data = response.json()

    for job in data['jobs']:

        job_title = job['title']
        job_description = job['description']
        finded_skills = []
        date = datetime.strptime(job['date_posted'], "%Y-%m-%d").date()
        totDays = (current_date - date).days

        if totDays <= 30:
            for skill in skills:
                if skill.lower() in job_description.lower() or skill.lower() in job_title.lower():
                    finded_skills.append(skill)

        if len(finded_skills) > 0:
            print(f"Job Title: {job_title}")
            print(f"Description: {job_description}")
            print(f"Skills that match: {finded_skills}")
            print(f"Date Posted: {date}")
            print("-" * 40)
except Exception as e:
    print(f"An error occurred: {e}")