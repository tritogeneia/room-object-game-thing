from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("Skeletons sit at their seats, their cracked and yellowing skulls staring at the goblets of wine they never got to finish.")

ballroom = Room("Ballroom")
ballroom.set_description("The glow of the moonlight that shines through the dingy windows catches each speck of dust in the air, making the spiderwebs that cling to the abandoned chairs glisten.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

current_room = kitchen
#print a new line, gets details, makes whatever the player types a variable and moves in that direction
while True:
	print("\n")
	current_room.get_details()
	command = input("> ")
	current_room = current_room.move(command)
