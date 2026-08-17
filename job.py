import datetime
from datetime import datetime
import connection


class Job:
    def __init__(self, title, description, updated_at):
        self.title = title
        self.description = description
        self.updated_at = updated_at

    def have_exclude_word(self, exclude_words):
        for word in exclude_words:
            if word.lower() in self.description.lower() or word.lower() in self.title.lower():
                return True
        return False

    def is_recent(self):
        date = datetime.strptime(self.updated_at[:10], "%Y-%m-%d").date()
        total_days = (datetime.now().date() - date).days
        return total_days <= 30

    def match_skills(self, skills):
        found_skills = []
        for skill in skills:
            if skill.lower() in self.description.lower() or skill.lower() in self.title.lower():
                found_skills.append(skill)
        return found_skills

    def createJob(self, title, description, updated_at, company, skills ):
        try:
            con = Connection("localhost", "buscador_vagas", "postgres", "181006") 
            con = manipular(f"INSERT INTO jobs (title, jobdescription, updated_at, company) VALUES ('{title}', '{description}', '{updated_at}', '{company}')")
            con.fechar()
        except Exception as e:
                print(f"An error occurred: {e}")
        