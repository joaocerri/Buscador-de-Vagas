class user: 

    def __init__(self):
        self.skills = []
        self.exclude_words = []

    def get_skills(self):
        return self.skills
    
    def get_exclude_words(self):
        return self.exclude_words

    def set_skills(self, skills):
        self.skills.append(skills)

    def set_exclude_words(self, exclude_words):
        self.exclude_words.append(exclude_words)

    def clear_skills(self):
        self.skills = []

    def clear_exclude_words(self):
        self.exclude_words = []

    def exclude_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)
            
    def exclude_exclude_word(self, exclude_word):
        if exclude_word in self.exclude_words:
            self.exclude_words.remove(exclude_word)