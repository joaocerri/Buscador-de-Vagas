import os
import requests as r
from datetime import datetime

from user import User
from job import Job
from connection import Connection

def main():
    user = User()
    con = Connection("localhost", "buscador_vagas", "postgres", "181006") 
    
    aux = con.consultar("SELECT skill FROM skills")
    user_skills = []
    for skill in aux:
        user_skills.append(skill[0])

    aux = con.consultar("SELECT word FROM exclude_words")
    user_exclude_words = []
    for word in aux:
        user_exclude_words.append(word[0])

    while True:
        answer = input("Type the skill you want to search (or 0 to finish): ").strip()
        if answer == "0":
            break
        if answer in user.get_skills() or answer in user_skills:
            print(f"Skill '{answer}' already exists.")
            continue
        user.set_skills(answer)
        os.system('cls' if os.name == 'nt' else 'clear')


    for skill in user.get_skills():
        if skill not in user_skills:
            con.manipular(f"INSERT INTO skills (skill) VALUES ('{skill}')")
        else:
            print(f"Skill '{skill}' already exists in the database.")

    for skill in user_skills:
        user.set_skills(skill)
        
    while True:
        answer = input("Type the word you want to exclude (or 0 to finish): ").strip()
        if answer == "0":
            break
        if answer in user.get_exclude_words() or answer in user_exclude_words:
            print(f"Word '{answer}' already exists.")
            continue
        os.system('cls' if os.name == 'nt' else 'clear')
        user.set_exclude_words(answer)

    for word in user.get_exclude_words():
        if word not in user_exclude_words:
            con.manipular(f"INSERT INTO exclude_words (word) VALUES ('{word}')")
        else:
            print(f"Word '{word}' already exists in the database.")

    for word in user_exclude_words:
        user.set_exclude_words(word)

    if not user.get_skills():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("No skills provided. Exiting.")
        return

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Searching for jobs with skills: {user.get_skills()}")
    print(f"Excluding jobs with words: {user.get_exclude_words()}")
    print("-" * 40)

    url = "https://apis.codante.io/api/job-board/jobs"

    try:
        response = r.get(url)
        data = response.json()

        found_jobs = 0

        for job_data in data.get('data', []):

            job = Job(
                title=job_data.get('title', ''),
                description=job_data.get('description', ''),
                updated_at=job_data.get('updated_at', '')
            )

            if not job.is_recent():
                continue

            if job.have_exclude_word(user.get_exclude_words()):
                continue

            matched_skills = job.match_skills(user.get_skills())

            if matched_skills:
                found_jobs += 1
                print(f"Job Title: {job.title}")
                print(f"Company: {job_data.get('company', 'N/A')}")
                print(f"Skills matched: {matched_skills}")
                print(f"Updated at: {job.updated_at[:10]}")
                print("-" * 40)

        print(f"\nSearch completed! Total of jobs found: {found_jobs}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()