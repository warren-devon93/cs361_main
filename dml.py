from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")
path_to_cwd = config["main"]["path"]
db_filename = "recipes"
request = {"db_path": path_to_cwd + db_filename, "statement": ""}
insert_recipes = "INSERT INTO Recipes VALUES (:rec_name)"
insert_ingredients = "INSERT INTO Ingredients VALUES (:ing_name)"
insert_instructions = "INSERT INTO Instructions VALUES (:rec_name, :inst_num, :inst_desc)"
insert_units = "INSERT INTO Units VALUES (:unit_name)"
insert_rec_ing = "INSERT INTO Recipes_Ingredients VALUES (:rec_name, :unit_name, :ing_name, :amount)"
update_amount = "UPDATE Recipes_Ingredients SET amount = ? WHERE rec_ing_id = ?"
update_instructions = "UPDATE Instructions SET inst_num = ? inst_desc = ? WHERE inst_id = ?"
delete_recipe = "DELETE FROM Recipes WHERE rec_name = ?"
