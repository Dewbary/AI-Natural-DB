sql_trainers_table = """
  create table trainers (
      trainerid integer primary key autoincrement,
      name varchar(50) not null,
      age int,
      region varchar(50)
);
"""

sql_pokemon_table = """
create table pokemon (
    pokemonid integer primary key autoincrement,
    name varchar(50) not null,
    level int,
    trainerid int,
    typeid int,
    foreign key (trainerid) references trainers(trainerid),
    foreign key (typeid) references types(typeid)
);
"""

sql_types_table = """
create table types (
    typeid integer primary key autoincrement,
    typename varchar(50) not null
);
"""

sql_moves_table = """
create table moves (
    moveid integer primary key autoincrement,
    movename varchar(50) not null,
    power int,
    typeid int,
    foreign key (typeid) references types(typeid)
);
"""

sql_pokemon_moves_table = """
create table pokemon_Moves (
    pokemonid int,
    moveid int,
    foreign key (pokemonid) references pokemon(pokemonid),
    foreign key (moveid) references moves(moveid),
    primary key (pokemonid, moveid)
);
"""

def get_schema():
    schema = f"{sql_trainers_table}{sql_pokemon_table}{sql_types_table}{sql_moves_table}{sql_pokemon_moves_table}"
    return schema

def get_schema_with_examples():
    schemaWithExamples = f"""
    
    {sql_trainers_table}
    3 example rows: ('Ash', 10, 'Kanto'),
    ('Misty', 10, 'Kanto'),
    ('Brock', 15, 'Kanto')

    {sql_pokemon_table}
    3 example rows: ('Charmander', 10, 1, 1),
    ('Squirtle', 10, 2, 2),
    ('Bulbasaur', 10, 3, 3)

    {sql_types_table}
    3 example rows: ('Fire'),
    ('Water'),
    ('Grass')

    {sql_moves_table}
    3 example rows: ('Ember', 40, 1),
    ('Water Gun', 40, 2),
    ('Razor Leaf', 55, 3)

    {sql_pokemon_moves_table}
    3 example rows: (1, 1),
    (2, 2),
    (3, 3),
    """
    return schemaWithExamples