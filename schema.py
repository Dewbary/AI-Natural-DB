sql_trainers_table = """
  CREATE TABLE Trainers (
      TrainerID INTEGER PRIMARY KEY AUTOINCREMENT,
      Name VARCHAR(50) NOT NULL,
      Age INT,
      Region VARCHAR(50)
);
"""

sql_pokemon_table = """
CREATE TABLE Pokemon (
    PokemonID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(50) NOT NULL,
    Level INT,
    TrainerID INT,
    TypeID INT,
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID),
    FOREIGN KEY (TypeID) REFERENCES Types(TypeID)
);
"""

sql_types_table = """
CREATE TABLE Types (
    TypeID INTEGER PRIMARY KEY AUTOINCREMENT,
    TypeName VARCHAR(50) NOT NULL
);
"""

sql_moves_table = """
CREATE TABLE Moves (
    MoveID INTEGER PRIMARY KEY AUTOINCREMENT,
    MoveName VARCHAR(50) NOT NULL,
    Power INT,
    TypeID INT,
    FOREIGN KEY (TypeID) REFERENCES Types(TypeID)
);
"""

sql_pokemon_moves_table = """
CREATE TABLE Pokemon_Moves (
    PokemonID INT,
    MoveID INT,
    FOREIGN KEY (PokemonID) REFERENCES Pokemon(PokemonID),
    FOREIGN KEY (MoveID) REFERENCES Moves(MoveID),
    PRIMARY KEY (PokemonID, MoveID)
);
"""

def get_schema():
    schema = f"{sql_trainers_table}{sql_pokemon_table}{sql_types_table}{sql_moves_table}{sql_pokemon_moves_table}"
    return schema

