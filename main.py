from turtle import Turtle,Screen
from prettytable import PrettyTable
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100.20)
#print(timmy)

# my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()

table = PrettyTable()
#my_list = ["Rice", "Beans", "Yam", "plantain", "spaghetti", "noodles"]
pokemon_names = ["Pikachu", "Squirtle","Charmander"]
pokemon_types = ["Electric", "Water","Fire"]

table.add_column("Pokemon Names", pokemon_names)
table.add_column("Types", pokemon_types)
table.align = "l"

print(table)