CREATE TABLE
    usuarios (
        id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        username VARCHAR(150) NOT NULL
    );

CREATE TABLE
    vagas (
        id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        title VARCHAR(150) NOT NULL,
        jobdescription TEXT NOT NULL,
        company VARCHAR(100) NOT NULL,
        update_at TIMESTAMP
    );

CREATE TABLE
    skills (
        id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        skill VARCHAR(100) UNIQUE NOT NULL
    );

CREATE TABLE
    vaga_skills (
        vaga_id INTEGER NOT NULL,
        skill_id INTEGER NOT NULL,
        PRIMARY KEY (vaga_id, skill_id),
        FOREIGN KEY (vaga_id) REFERENCES vagas (id) ON DELETE CASCADE,
        FOREIGN KEY (skill_id) REFERENCES skills (id) ON DELETE CASCADE
    );

CREATE TABLE
    exclude_words (
        id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        word VARCHAR(100) UNIQUE NOT NULL
    );