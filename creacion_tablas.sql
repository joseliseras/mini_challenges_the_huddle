-- Crear tabla Pokemones
CREATE TABLE pokemones (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    habilidad VARCHAR(50),
    hp INT,
    ataque INT,
    defensa INT,
    velocidad INT
);

-- Crear tabla entrnadores
CREATE TABLE entrenadores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    edad INT,
    ciudad VARCHAR(50)
);

-- Crear tabla entrenador_pokemon
CREATE TABLE entrenador_pokemon (
    id SERIAL PRIMARY KEY,
    entrenador_id INT REFERENCES entrenadores(id),
    pokemon_id INT REFERENCES pokemones(id),
    UNIQUE (entrenador_id, pokemon_id)
);

-- Crear tabla batalla
CREATE TABLE batallas (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    entrenador1_id INT REFERENCES entrenadores(id),
    entrenador2_id INT REFERENCES entrenadores(id),
    pokemon1_id INT REFERENCES pokemones(id),
    pokemon2_id INT REFERENCES pokemones(id),
    resultado VARCHAR(50)
);
