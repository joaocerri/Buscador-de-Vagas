import os
import requests as r
from datetime import datetime

from user import User
from job import Job

def main():
    user = User()

    while True:
        answer = input("Type the skill you want to search (or 0 to finish): ").strip()
        if answer == "0":
            break
        user.set_skills(answer)

    while True:
        answer = input("Type the word you want to exclude (or 0 to finish): ").strip()
        if answer == "0":
            break
        user.set_exclude_words(answer)

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

        jobs_encontrados = 0

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
                jobs_encontrados += 1
                print(f"Job Title: {job.title}")
                print(f"Company: {job_data.get('company', 'N/A')}")
                print(f"Skills matched: {matched_skills}")
                print(f"Updated at: {job.updated_at[:10]}")
                print("-" * 40)

        print(f"\nSearch completed! Total of jobs found: {jobs_encontrados}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()