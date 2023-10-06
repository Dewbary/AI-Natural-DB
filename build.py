import os

from db import create_table, create_connection
from schema import *


def insert_to_trainers(conn):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = """
INSERT INTO Trainers (Name, Age, Region) VALUES 
('Ash', 10, 'Kanto'),
('Misty', 10, 'Kanto'),
('Brock', 15, 'Kanto'),
('May', 10, 'Hoenn'),
('Max', 8, 'Hoenn'),
('Dawn', 10, 'Sinnoh'),
('Paul', 11, 'Sinnoh'),
('Cynthia', 21, 'Sinnoh');
    """

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_types(conn):

    sql = """
INSERT INTO Types (TypeName) VALUES 
('Fire'),
('Water'),
('Grass'),
('Electric'),
('Psychic'),
('Rock'),
('Ground'),
('Ice'),
('Flying'),
('Poison');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_moves(conn):

    sql = """
INSERT INTO Moves (MoveName, Power, TypeID) VALUES 
('Ember', 40, 1),
('Flamethrower', 90, 1),
('Water Gun', 40, 2),
('Hydro Pump', 110, 2),
('Razor Leaf', 55, 3),
('Solar Beam', 120, 3),
('Thunderbolt', 90, 4),
('Thunder', 110, 4),
('Psychic', 90, 5),
('Confusion', 50, 5),
('Rock Throw', 50, 6),
('Earthquake', 100, 7),
('Ice Beam', 90, 8),
('Fly', 70, 9),
('Poison Jab', 80, 10);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_pokemon(conn):
    sql = """
INSERT INTO Pokemon (Name, Level, TrainerID, TypeID) VALUES 
('Charmander', 10, 1, 1),
('Squirtle', 10, 2, 2),
('Bulbasaur', 10, 3, 3),
('Pikachu', 12, 1, 4),
('Mewtwo', 70, 8, 5),
('Onix', 14, 3, 6),
('Groudon', 50, 4, 7),
('Articuno', 50, 5, 8),
('Pidgeot', 36, 1, 9),
('Arbok', 22, 7, 10);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_pokemon_moves(conn):

    sql = """
INSERT INTO Pokemon_Moves (PokemonID, MoveID) VALUES 
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(3, 6),
(4, 7),
(4, 8),
(5, 9),
(5, 10),
(6, 11),
(7, 12),
(8, 13),
(9, 14),
(10, 15);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def main():
    database = "./pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    create_table(conn, sql_trainers_table)
    insert_to_trainers(conn)
    create_table(conn, sql_types_table)
    insert_to_types(conn)
    create_table(conn, sql_moves_table)
    insert_to_moves(conn)
    create_table(conn, sql_pokemon_table)
    insert_to_pokemon(conn)
    create_table(conn, sql_pokemon_moves_table)
    insert_to_pokemon_moves(conn)

    print("Database build successful!")

if __name__ == "__main__":
    main()