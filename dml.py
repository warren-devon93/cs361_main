units = ("tsp", "tbsp", "cup", "pint", "quart", "gallon", "oz", "lb", "g", "kg", "dash", "stick", "drop", "unit")

inserts = {
    "recipe": """INSERT OR IGNORE INTO Recipes (rec_name) VALUES ('?')""", 
    "ingredient": "INSERT OR IGNORE INTO Ingredients (ing_name) VALUES ('?')",
    "instruction": """INSERT INTO Instructions (rec_name, step_num, step_desc) 
                    VALUES ('?', ?, '?')""",
    "unit": "INSERT INTO Units (unit_name) VALUES ('?')",
    "rec_ing": """INSERT INTO Recipes_Ingredients (rec_name, unit_name, ing_name, ammount) 
                    VALUES ('?', '?', '?', ?)"""
}
updates = {
    "Ingredients": """UPDATE Recipes_Ingredients SET 
                        unit_name = ('?'), 
                        amount = (?), 
                        ing_name = ('?')
                            WHERE rec_ing_id = (?)""",
    "instruction": """UPDATE Instructions SET 
                        step_num = (?), 
                        step_desc = ('?')
                            WHERE inst_id = (?)"""
}
selects = {
    "all": "SELECT rec_name FROM Recipes",
    "name": "SELECT rec_name FROM Recipes WHERE rec_name = ('?')",
    "ingredients": """SELECT unit_name, amount, ing_name FROM Recipes_Ingredients 
                        WHERE rec_name = ('?')""",
    "instructions": """SELECT step_num, step_desc FROM Instructions WHERE rec_name = ('?')"""
} 
delete = "DELETE FROM Recipes WHERE rec_name = ('?')"
