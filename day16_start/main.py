# import turtle
#
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
#
# screen = turtle.Screen()
# print(screen.canvheight)
#
# screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("S.N", "123")
table.add_column("Pokemon name", ['Pikachu', 'Squirtle', 'Charmender'])
table.add_column("Types", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
