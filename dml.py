from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")
path_to_cwd = config["main"]["path"]
db_filename = "recipes"
request = {"db_path": path_to_cwd + db_filename, "statement": ""}
units = ("tsp", "tbsp", "cup", "pint", "quart", "gallon", "oz", "lb", "g", "kg", "dash", "stick", "drop", "unit")
inserts = {
    "recipe": f"INSERT OR IGNORE INTO Recipes VALUES ({rec_name})", 
    "ingredient": f"INSERT OR IGNORE INTO Ingredients VALUES ({ing_name})",
    "instruction": f"INSERT INTO Instructions VALUES ({rec_name}, {step_num}, {step_desc})",
    "unit": f"INSERT INTO Units VALUES ({unit_name})",
    "rec_ing": f"INSERT INTO Recipes_Ingredients VALUES ({rec_name}, {unit_name}, {ing_name}, {amount})"
}
updates = {
    "Ingredients": f"""UPDATE Recipes_Ingredients SET 
                        unit_name = {unit_name}, 
                        amount = {amount}, 
                        ing_name = {ing_name} 
                            WHERE rec_ing_id = {rec_ing_id}""",
    "instruction": f"""UPDATE Instructions SET 
                        step_num = {step_num}, 
                        step_desc = {step_desc} 
                            WHERE inst_id = {inst_id}"""
}
selects = {
    "all": "SELECT rec_name FROM Recipes",
    "name": f"SELECT rec_name FROM Recipes WHERE rec_name = {rec_name}",
    "ingredients": f"""SELECT unit_name, amount, ing_name FROM Recipes_Ingredients 
                        WHERE rec_name = {rec_name}""",
    "instructions": f"""SELECT step_num, step_desc FROM Instructions WHERE rec_name = {rec_name}"""
} 
delete = f"DELETE FROM Recipes WHERE rec_name = {rec_name}"
