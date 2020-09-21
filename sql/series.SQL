CREATE TABLE series (
    serie_id INTEGER PRIMARY KEY, 
    name VARCHAR(30), 
    name_url VARCHAR(40), 
    image_url TEXT, 
    descricao TEXT, 
    genero VARCHAR(15), 
    avg_note INTEGER DEFAULT 0);