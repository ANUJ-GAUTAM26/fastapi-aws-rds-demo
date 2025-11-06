-- Create tables
CREATE TABLE IF NOT EXISTS dim_sources (
    source_id SERIAL PRIMARY KEY,
    source_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_authors (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(255) NOT NULL
);

-- Insert data
INSERT INTO dim_sources (source_name) VALUES
    ('BBC'),
    ('CNN'),
    ('Reuters'),
    ('The Guardian'),
    ('Al Jazeera'),
    ('The Verge'),
    ('TechCrunch'),
    ('Bloomberg'),
    ('New York Times'),
    ('Financial Times');

INSERT INTO dim_authors (author_name) VALUES
    ('Alice Johnson'),
    ('Bob Kumar'),
    ('Carlos Mendez'),
    ('Dana Lee'),
    ('Emma Stone'),
    ('Frank Wang'),
    ('Grace Kim'),
    ('Henry Patel'),
    ('Isha Singh'),
    ('James Miller');
