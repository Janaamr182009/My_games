#printing a welcome message and asking which door the player would choose
print("""──▄────▄▄▄▄▄▄▄────▄───
─▀▀▄─▄█████████▄─▄▀▀──
─────██─▀███▀─██──────
───▄─▀████▀████▀─▄────
─▀█────██▀█▀██────█▀──""")
doors=input("""welcome to the island!\n there is two doors in front of you. red door🚪 and a blue door🚪\nwich one will you choose?(write the color name only)\n""")
#preparing the result of the players choice and then asking for his choice for the next challenge 
if doors.lower()=="blue":
  print("ops! You opened the crocodiles door!")
  print("GAME OVER!")
elif doors.lower()=="red":
  box=input("""Great! Now you entered a room\nyou have three boxes:white box 🎁, green box 🎁 and yellow box 🎁\n which one will you choose?\n""")
#printing the results for the players choice
  if box.lower()=="white":
    print("ops! You opened a box full of snakes!\nGAME OVER!")
  elif box.lower()=="yellow":
    print("ops!you opened a box full of spiders!\nGAME OVER!")
  elif box.lower()=="green":
    print("You found the treasure!\nCongratilaition little pirate🦜🏴‍☠️!")
  else:
    print("please follow the rules")
else:
  print("please follow the rules")
