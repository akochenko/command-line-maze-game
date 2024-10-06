##main variables
positionX = 0
positionY = 0
positionXExit = 0
positionYExit = 4
lives = 5
answer = ""
choice = ""
moves = 0
counter = 0

##reset 
def reset():
  global positionX
  global positionY
  global lives
  global answer
  global choice
  global moves
  global counter
  positionX = 0
  positionY = 0
  lives = 5
  answer = ""
  choice = ""
  moves = 0
  counter = 0
  

##colors
##hints
def away():
  awayX = positionX - positionXExit
  awayY = positionY - positionYExit
  if awayX <0:
    awayX = -1 * awayX
  if awayY <0:
    awayY = -1 * awayY
  away = awayX + awayY
  print("You are", away, "positions away from the exit, disregarding walls!")

 
## space
def space():
  print("")

## movements and questions counter
def move():
  global moves
  moves = moves + 1
  return(moves)

def count():
  global counter
  counter = counter + 1
  return(counter)


def livesCheck():
  if lives == 0:
    print("You have no more lives left!")
    print("Don't worry, you can try again! Enter 'T' to restart!")
    tryAgain = input("").upper()
    if tryAgain == "T":
      reset()
      position00()
    else: 
      print("Thank you for playing the BLIND MAZE!")


def movesCheck():
  if moves == 30:
    print("You have excited 30 moves, it seems like you are lost.")
    print("Don't worry, you can try again!", "\033[4m" "Enter 'T' to restart!", "\033[0m")
    tryAgain = input("").upper()
    if tryAgain == "T":
      reset()
      position00()
    else: 
      print("Thank you for playing the BLIND MAZE!")
      
##end
def exitFound():
  print("\u001b[45;1m""CONGRATULATIONS!" "\033[0m", "\u001b[35;1m" "You found the exit!!!""\033[0m")
  space()
  print("It took you", moves, "moves to reach the exit! You still have", lives, "lives!")
  space()
  print("\033[4m" "Type'T' if you wish to try again and minimise the number of moves!", "\033[0m")
  tryAgain = input("").upper()
  if tryAgain == "T":
    reset()
    position00()


##questions defs

def q1 ():
  global lives 
  space()
  print("\u001b[35;1m" "It's time for a question!")
  print("How long does it take for a plastic bottle to completely decompose?")
  space()
  print("A: 500 years")
  print("B: 50 years")
  print("C: 5 years")
  print("D: 5 months")
  
  
  answer = input("Choose a letter: ").upper()
  while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    space()
    print("\033[0m" "This is not an option. Please input a letter.")
    answer = input("").upper()
    
  if answer == "A":
    space()
    print("\u001b[32;1m" "Correct!", "\033[0m" "You get a hint!")
    away()
  else:
    lives = lives - 1
    space()
    print( "\u001b[31;1m" "Wrong!", "\033[0m" "It takes 500 years for a plastic bottle to decompose.")
    print("You lose a life! You have only", lives, " left!")
    
  livesCheck()

def q2 ():
  global lives
  space()
  print("\u001b[35;1m" "It's time for a question!")
  print("What is the greenhouse effect?")
  space()
  print("A: Greenhouses become too warm")
  print("B: The Earth is expanding due to the heat")
  print("C: Gases in the atmoshphere trap heat")
  print("D: The Sun is radiating more heat")

  answer = input("Choose a letter: ").upper()
  while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    space()
    print("\033[0m" "This is not an option. Please input a letter.")
    answer = input("").upper()
    
  if answer == "C":
    space()
    print("\u001b[32;1m" "Correct!", "\033[0m" "You get a hint!")
    away()
  else:
    lives = lives - 1
    space()
    print("\u001b[31;1m" "Wrong!", "\033[0m" "The greenhouse effect is when gases in the atmosphere trap heat!")
    print("You have only", lives, "left!")

  livesCheck()

def q3 ():
  global lives
  space()
  print("\u001b[35;1m" "It's time for a question!")
  print("What affects climate change the most?")
  space()
  print("A: Factories")
  print("B: Transportation")
  print("C: Landfills")
  print("D: Agriculture")

  answer = input("Choose a letter: ").upper()
  while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    space()
    print("\033[0m" "This is not an option. Please input a letter.")
    answer = input("").upper()
    
  if answer == "B":
    space()
    print("\u001b[32;1m" "Correct!", "\033[0m" "You get a hint!")
    away()
    
  else:
    lives = lives - 1
    space()
    print("\u001b[31;1m" "Wrong!", "\033[0m" "Transportation affects climate change the most!")
    print("You have only", lives, "left!")

  livesCheck()

def q4():
  global lives
  space()
  print("\u001b[35;1m" "It's time for a question!")
  print("Which gas would be found in the largest amounts on Earth? ")
  space()
  print("A: Oxygen")
  print("B: Carbon dioxide")
  print("C: Hydrogen")
  print("D: Nitrogen")
  
  answer = input("Choose a letter: ").upper()
  while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    space()
    print("\033[0m" "This is not an option. Please input a letter.")
    answer = input("").upper()
    
  if answer == "D":
    space()
    print("\u001b[32;1m" "Correct!", "\033[0m" "You get a hint!")
    away()
  else:
    lives = lives - 1
    space()
    print("\u001b[31;1m" "Wrong!", "\033[0m" "Nitrogen has the largest amount on earth! ")
    print("You have only", lives, "left!")

  livesCheck()

def q5():
  global lives
  space()
  print("\u001b[35;1m" "It's time for a question!")
  print("In how many years will the sun explode?")
  space()
  print("A: 800,000 years")
  print("B: 8 billion years")
  print("C: 800 years")
  print("D: 5 billion years")
  
  answer = input("Choose a letter: ").upper()
  while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    space()
    print("\033[0m" "This is not an option. Please input a letter.")
    answer = input("").upper()
    
  if answer == "B":
    space()
    print("\u001b[32;1m" "Correct!", "\033[0m" "You get a hint!")
    away()
  
  else:
    lives = lives - 1
    space()
    print("\u001b[31;1m" "Wrong!", "\033[0m" "The sun will die in 8 billion years! ")
    print("You have only", lives, "left!")

  livesCheck()

def q6():
  global lives
  space()
  print( "\u001b[35;1m""It's time for a question!")
  print("Which country is the world's biggest carbon emitter?")
  space()
  print("A: India")
  print("B: USA")
  print("C: China")
  print("D: Russia")

  answer = input("Choose a letter: ""\033[0m").upper()
  while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    space()
    print("This is not an option. Please input a letter.")
    answer = input("").upper()
    
  if answer == "C":
    space()
    print("\u001b[32;1m""Correct!""\033[0m", "You get a hint!")
    print("The position of the exit is 0, 4")
    
  else:
    lives = lives - 1
    space()
    print("\u001b[31;1m""Wrong!""\033[0m", "China is the biggest carbon polluter!")
    print("You have only", lives, "left!")

  livesCheck()

def q7():
  global lives
  space()
  print("\u001b[35;1m""It's time for a question!")
  print("Which one of these is NOT an aim in the Paris Agreement.")
  space()
  print("A: Limit temperature increase to 3°C")
  print("B: Save and increase forest area")
  print("C: Divert more money to achieve these objectives")
  print("D: Achieve zero emissions by mid-century")
  
  answer = input("Choose a letter: ""\033[0m").upper()
  while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    space()
    print("This is not an option. Please input a letter.")
    answer = input("").upper()
    
  if answer == "A":
    space()
    print("\u001b[32;1m""Correct!""\033[0m", "You get a hint!")
    away()
  else:
    lives = lives - 1
    space()
    print("\u001b[31;1m""Wrong!""\033[0m", "Limit temperature to 3°C is not an aim in the Paris Agreement, it's actually 1.5°C!")
    print("You have only", lives, "left!")

  livesCheck()

def q8():
  global lives
  space()
  print( "\u001b[35;1m""It's time for a question!")
  print("Which country is best controlling climate change?")
  space()
  print("A: UK")
  print("B: Norway")
  print("C: Sweden")
  print("D: Denmark")

  answer = input("Choose a letter: ""\033[0m").upper()
  while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    space()
    print("This is not an option. Please input a letter.")
    answer = input("").upper()
    
  if answer == "D":
    space()
    print("\u001b[32;1m""Correct!""\033[0m", "You get a hint!")
    away()
    
  else:
    lives = lives - 1
    space()
    print("\u001b[31;1m""Wrong!""\033[0m", "Denmark is best controlling climate change!")
    print("You have only", lives, "left!")

    livesCheck()


def q9():
  global lives
  space()
  print("\u001b[35;1m""It's time for a question!")
  print("What's the increase in carbon dioxide in the atmosphere since 1800s?")
  space()
  print("A: 56%")
  print("B: 47%")
  print("C: 33%")
  print("D: 21%")
  
  answer = input("Choose a letter: ""\033[0m").upper()
  while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    space()
    print("This is not an option. Please input a letter.")
    answer = input("").upper()
    
  if answer == "B":
    space()
    print("\u001b[32;1m""Correct!""\033[0m", "You get a hint!")
    away()
    
  else:
    lives = lives - 1
    space()
    print( "\u001b[31;1m""Wrong!""\033[0m", "Carbon dioxide has increased by 47% since the 1800s!")
    print("You have only", lives, "left!")

    livesCheck()
  
def q10():
  global lives
  space()
  print("\u001b[35;1m""It's time for a question!")
  print("Which one is NOT a danger of plastics?")
  space()
  print("A: corrosion")
  print("B: sea and wildlife pollution")
  print("C: produces chemical pollutants/toxins")
  print("D: not biodegradable")

  answer = input("Choose a letter: ").upper()
  while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    space()
    print("\033[0m" "This is not an option. Please input a letter.")
    answer = input("").upper()
    
  if answer == "A":
    space()
    print("\u001b[32;1m" "Correct!""\033[0m", "You get a hint!")
    away()
  else:
    lives = lives - 1
    space()
    print( "\u001b[31;1m""Wrong!" "\033[0m", "Corrosion is not a danger of plastics!")
    print("You have only", lives, "left!")

    livesCheck()

## questions defs
def counterCheck():
  if counter == 3:
    q1()
  elif counter == 6:
    q2()
  elif counter == 9:
    q3()
  elif counter == 12:
    q4()
  elif counter == 15:
    q5()
  elif counter == 18:
    q6()
  elif counter == 21:
    q7()
  elif counter == 24:
    q8()
  elif counter == 27:
    q9()
  elif counter == 30:
    q10()
## movements
def east (): 
  global positionX
  positionX = positionX + 1
  return(positionX)

def west ():
  global positionX
  positionX = positionX - 1

def north ():
  global positionY
  positionY = positionY + 1

def south ():
  global positionY
  positionY = positionY - 1


##position functions

def position_20():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m" "north(N)," "\u001b[33;1m" "east (E).", "\033[0m" "It's a corner, there's a wall to the south and to the west. Please input your choice.")
  choice = input("").upper()
  while choice != "E" and choice != "N":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "E":
    east()
    position_10()
  elif choice == "N":
    north()
    position_21()
    


def position_10():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m" "north(N),", "\u001b[33;1m" "east(E)", "\033[0m" "or", "\033[1;32m" "west(W)","\033[0m" ". There's a wall to the south. Please input your choice.")
  choice = input("").upper()
  while choice != "E" and choice != "N" and choice != "W":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "E":
    east()
    position00()
  elif choice == "N":
    north()
    position_11()
  elif choice == "W":
    west()
    position_20()
    


def position00():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "This is your starting position,", positionX, positionY, "\033[0m")
  print("You can move", "\u001b[33;1m" "east (E)", "\033[0m" "or", "\033[1;32m""west (W)." "\033[0m", "There's a wall to the north. Please input your choice.")
  choice = input("").upper()
  while choice != "E" and choice != "W":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "E":
    east()
    position10()
  elif choice == "W":
    west()
    position_10()

    

def position10():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m" "north(N)",  "\033[0m" "or","\033[1;32m"  "west(W)","\033[0m." "There's a wall to the south and to the east. Please input your choice.")
  choice = input("").upper()
  while choice != "W" and choice != "N":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "N":
    north()
    position11()
  elif choice == "W":
    west()
    position_10()


def position20():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m" "north(N),", "\033[0m" "it's a dead end. Please input your choice.")
  choice = input("").upper()
  while choice != "N":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "N":
    north()
    position21()



def position30():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m" "north(N),", "\033[0m" "it's a dead end. Please input your choice.")
  choice = input("").upper()
  while choice != "N":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "N":
    north()
    position31()


def position_21():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m" "north(N),", "\u001b[31;1m" "south(S)", "\033[0m" "or", "\u001b[33;1m" "east(E)." ,"\033[0m" "There's a wall to the west. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "N" and choice != "E":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "E":
    east()
    position_11()
  elif choice == "N":
    north()
    position_22()
  elif choice == "S":
    south()
    position_20()


def position_11():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m" "north(N),", "\u001b[31;1m" "south(S)", "\033[0m" "or", "\033[1;32m" "west(W).", "\033[0m" "There's a wall to the east. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "N" and choice != "W":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "W":
    west()
    position_21()
  elif choice == "N":
    north()
    position_12()
  elif choice == "S":
    south()
    position_10()


def position01():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\u001b[33;1m" "east(E),", "\033[0m" "it's a dead end. Please input your choice.")
  choice = input("").upper()
  while choice != "E":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "E":
    east()
    position11()


def position11():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\u001b[31;1m" "south(S)", "\033[0m" "or", "\033[1;32m" "west(W)." ,"\033[0m" "There's a wall to the north and to the east. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "W":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "W":
    west()
    position01()
  elif choice == "S":
    south()
    position10()


def position21():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m" "north(N)", "\033[0m" "or","\u001b[31;1m" "south(S).", "\033[0m" "There's a wall to the west and to the east. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "N":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "S":
    south()
    position20()
  elif choice == "N":
    north()
    position22()


def position31():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m" "north(N)", "\033[0m" "or","\u001b[31;1m" "south(S).", "\033[0m" "There's a wall to the west and to the east. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "N":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "S":
    south()
    position30()
  elif choice == "N":
    north()
    position32()
    

def position_22():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\u001b[33;1m" "east(E)", "\033[0m" "or", "\u001b[31;1m" "south(S).", "\033[0m" "There's a wall to the west and to the north. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "E":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "E":
    east()
    position_12()
  elif choice == "N":
    north()
    position_23()


def position_12():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move ", "\u001b[33;1m" "east(E),", "\033[1;32m" "west(W)" , "\033[0m" "or", "\u001b[31;1m" "south(S).", "\033[0m" "There's a wall to the north. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "E" and choice != "W":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "S":
    south()
    position_11()
  elif choice == "W":
    west()
    position_22()
  elif choice == "E":
    east()
    position02()


def position02():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\u001b[33;1m" "east(E)", "\033[0m""or", "\033[1;32m""west(W).""\033[0m", "There's a wall to the north and to the south. Please input your choice.")
  choice = input("").upper()
  while choice != "E" and choice != "W":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "E":
    east()
    position12()
  elif choice == "W":
    west()
    position_12()


def position12():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m""north(N),", "\u001b[33;1m" "east(E)", "\033[0m""or", "\033[1;32m" "west(W).""\033[0m", "There's a wall to the south. Please input your choice.")
  choice = input("").upper()
  while choice != "E" and choice != "W" and choice != "N":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "W":
    west()
    position02()
  elif choice == "N":
    north()
    position13()
  elif choice == "E":
    east()
    position22()


def position22():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m""north(N),", "\u001b[31;1m""south(S)", "\033[0m""or", "\033[1;32m""west(W).""\033[0m", "There's a wall to the east. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "N" and choice != "W":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "S":
    south()
    position21()
  elif choice == "N":
    north()
    position23()
  elif choice == "W":
    west()
    position12()


def position32():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m""north(N)", "\033[0m""or", "\u001b[31;1m""south(S).""\033[0m", "There's a wall to the west and to the east. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "N":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "S":
    south()
    position31()
  elif choice == "N":
    north()
    position33()


def position_23():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m" "north(N)", "\033[0m""or", "\u001b[33;1m""east(E).""\033[0m", "There's a wall to the south and to the west. Please input your choice.")
  choice = input("").upper()
  while choice != "E" and choice != "N":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "E":
    east()
    position_13()
  elif choice == "N":
    north()
    position_24()


def position_13():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m""north(N),","\u001b[33;1m" "east(E)", "\033[0m""or", "\033[1;32m""west(W).""\033[0m", "There's a wall to the south. Please input your choice.")
  choice = input("").upper()
  while choice != "E" and choice != "W" and choice != "N":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "E":
    east()
    position03()
  elif choice == "W":
    west()
    position_23()
  elif choice == "N":
    north()
    position_14()


def position03():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m" "north(N),", "\u001b[33;1m" "east(E)","\033[0m" "or", "\033[1;32m" "west(W).""\033[0m", "There's a wall to the south. Please input your choice.")
  choice = input("").upper()
  while choice != "W" and choice != "N" and choice != "E":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "W":
    west()
    position_13()
  elif choice == "N":
    north()
    position04()
  elif choice == "E":
    east()
    position13()


def position13():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m""north(N),", "\u001b[31;1m""south(S),", "\u001b[33;1m""east(E)", "\033[0m""or", "\033[1;32m""west(W)!""\033[0m", "Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "N" and choice != "E" and choice != "W":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "S":
    south()
    position12()
  elif choice == "N":
    north()
    position14()
  elif choice == "E":
    east()
    position23()
  elif choice == "W":
    west()
    position03()


def position23():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move","\033[1;34m""north(N),","\u001b[31;1m" "south(S)", "\033[0m" "or", "\033[1;32m" "west(W).""\033[0m", "There's a wall to the to the east. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "N" and choice != "W":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "S":
    south()
    position13()
  elif choice == "N":
    north()
    position24()
  elif choice == "W":
    west()
    position22()


def position33():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;34m""north(N)", "\033[0m""or", "\u001b[31;1m""south(S).""\033[0m", "There's a wall to the west and to the east. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "N":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "S":
    south()
    position32()
  elif choice == "N":
    north()
    position34()


def position_24():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\u001b[33;1m""east(E)", "\033[0m""or", "\u001b[31;1m""south(S).""\033[0m", "It's a corner, there's a wall to the west and to the north. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "E":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "S":
    south()
    position_23()
  elif choice == "E":
    east()
    position_14()


def position_14():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\u001b[33;1m""east(E),", "\033[1;32m"  "west(W)", "\033[0m""or", "\u001b[31;1m""south(S).""\033[0m", "There's a wall to the north. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "E" and choice != "W":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "S":
    south()
    position_13()
  elif choice == "E":
    east()
    position04()
  elif choice == "W":
    west()
    position_24()


def position04():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  exitFound()


def position14():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\u001b[33;1m""east(E),","\033[1;32m" "west(W)", "\033[0m""or", "\u001b[31;1m""south(S).", "\033[0m", "There's a wall to the north. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "W" and choice != "E":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "S":
    south()
    position13()
  elif choice == "W":
    west()
    position04()
  elif choice == "E":
    east()
    position24()


def position24():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\u001b[33;1m""east(E),", "\033[1;32m"   "west(W)", "\033[0m""or", "\u001b[31;1m""south(S).""\033[0m", "There's a wall to the north. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "W" and choice != "E":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "S":
    south()
    position23()
  elif choice == "W":
    west()
    position14()
  elif choice == "E":
    east()
    position34()


def position34():
  counterCheck()
  movesCheck()
  count()
  move()
  space()
  print("\033[1;36m" "Your position is", positionX, ",", positionY , "\033[0m")
  print("You can move", "\033[1;32m""west(W)", "\033[0m""or", "\u001b[31;1m""south(S).""\033[0m", "It's a corner, there's a wall to the north and to the east. Please input your choice.")
  choice = input("").upper()
  while choice != "S" and choice != "W":
    space()
    print("This is not an option. Please input a letter.")
    choice = input("").upper()
  if choice == "S":
    south()
    position33()
  elif choice == "W":
    west()
    position24()
 
    
##all positions

##main code
print ("Welcome to the", "\u001b[46m""\033[1m""\033[4m" "BLIND MAZE!" "\033[0m")
space()
print ("You have to find the exit as fast as possible while answering questions! ")
space()
print("Try to visualize the maze as you can't see the map!")
space()
print("Every 3 moves you have to answer a question. You start with 5 lives. Wrong answer, lost life. Right answer, a hint!", "\u001b[44m""\033[1m""\033[4m" "GOOD LUCK ALL PARTICIPANTS!")
space()
print("\033[0m" "You can move", "\033[1;34m" "north ↑,","\u001b[31;1m" "south ↓,","\u001b[33;1m" "east →", "\033[0m" "or", "\033[1;32m" "west ← !" "\033[0m")
space()
position00()


##questions

  