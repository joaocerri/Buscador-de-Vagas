import requests as r

skills =  ["python", "machine learning", "data analysis", "sql"]

url = "https://api.example.com/data"

response = r.get(url)
data = response.json()

for job in data['jobs']:

    job_title = job['title']
    job_description = job['description']

    totSkills = 0
    for skill in skills:
        if skill.lower() in job_description.lower() or skill.lower() in job_title.lower():
            totSkills += 1

    if totSkills > 0:
        print(f"Job Title: {job_title}")
        print(f"Description: {job_description}")
        print(f"Required Skill: {skill}")
        print("-" * 40)