from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")
path_to_cwd = config["main"]["path"]
db_filename = "recipes"
request = {"db_path": path_to_cwd + db_filename, "statement": ""}
creates = ("""CREATE TABLE Recipes 
                    (rec_name TEXT PRIMARY KEY)""",
              """CREATE TABLE Ingredients 
                    (ing_name TEXT PRIMARY KEY)""",
              """CREATE TABLE Instructions 
                    (inst_id INT PRIMARY KEY, rec_name TEXT, step_num INT, step_desc TEXT,
                    FOREIGN KEY (rec_name) REFERENCES Recipes (rec_name)
                        ON DELETE CASCADE)""",
              """CREATE TABLE Units 
                    (unit_name TEXT PRIMARY KEY)""",
              """CREATE TABLE Recipes_Ingredients 
                    (rec_ing_id INT PRIMARY KEY, rec_name TEXT, unit_name TEXT, ing_name TEXT, amount REAL,
                    FOREIGN KEY (rec_name) REFERENCES Recipes (rec_name)
                        ON DELETE CASCADE,
                    FOREIGN KEY (unit_name) REFERENCES Units (unit_name)
                        ON DELETE CASCADE,
                    FOREIGN KEY (ing_name) REFERENCES Ingredients (ing_name)
                        ON DELETE CASCADE)""")