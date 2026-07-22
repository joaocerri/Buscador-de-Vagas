import requests as r
from datetime import datetime

skills =  []
exclude_words = []
answer = ""

while answer != "0" and answer != "1":
    answer = input("Type the skill you want to search or 0 to exit: ")
    if(answer != "0" and answer != "1"):
        skills.append(answer)

answer = ""

while answer != "0":
    answer = input("Type the word you want to exclude or 0 to exit: ")
    if(answer != "0" and answer != "1"):
        exclude_words.append(answer)

current_date = datetime.now().date()

url = "https://apis.codante.io/api/job-board/jobs"

try:
    response = r.get(url)
    data = response.json()

    for job in data.get('data'):

        job_title = job.get('title')
        job_description = job.get('description')
        found_skills = []
        date = datetime.strptime(job.get('updated_at')[:10], "%Y-%m-%d").date()
        total_days = (current_date - date).days
        has_exclude_word = False

        for word in exclude_words:
            if word.lower() in job_description.lower() or word.lower() in job_title.lower():
                has_exclude_word = True

        if has_exclude_word:
            continue 

        if total_days <= 30:
            for skill in skills:
                if skill.lower() in job_description.lower() or skill.lower() in job_title.lower():
                    found_skills.append(skill)

        if len(found_skills) > 0:
            print(f"Job Title: {job_title}")
            print(f"Company: {job.get('company')}")
            print(f"Description: {job_description}")
            print(f"Skills that match: {found_skills}")
            print(f"Date Posted: {date}")
            print("-" * 40)
except Exception as e:
    print(f"An error occurred: {e}")