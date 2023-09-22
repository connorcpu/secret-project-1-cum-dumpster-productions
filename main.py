    # --- Merijn, Connor en Filip ---
import pygame, sys, random
from pygame.locals import QUIT

#create array with the coordinate of each square in the picture
vakjes = [[160, 683], [286, 683], [356, 683], [415, 683], [482, 683],
[545, 683], \
[618, 683], [692, 683], [758, 683], [828, 643], [895, 598], [937, 549],
[965, 489], \
[982, 430], [982, 353], [968, 283], [944, 220], [905, 167], [833, 111],
[744, 66], \
[664, 62], [597, 62], [536, 62], [464, 62], [398, 62], [335, 62], [265,
66], [198, 94], \
[142, 129], [104, 174], [83, 227], [65, 283], [65, 367], [83, 435], [116,
491], [160, 535], \
[216, 570], [282, 587], [342, 587], [405, 587], [468, 587], [536, 587],
[615, 587], \
[692, 587], [755, 578], [816, 528], [863, 458], [877, 402], [874, 335],
[856, 283], \
[804, 202], [737, 160], [632, 157], [545, 157], [468, 157], [394, 157],
[328, 157], \
[265, 167], [195, 223], [167, 325], [188, 403], [221, 454], [282, 482],
[413, 456]]

#parse command line arguments
debug = False
i = 0

while i < len(sys.argv):
  arg = sys.argv[i]
  print(arg)
  if arg == "--debug":
    debug = True
    print(debug)
  i += 1

#const for dice possions
dicePos = [285, 270]
devilsDicePos = [665, 270]

#'global' variable wether or not the mous is on the dice 
hoveringDice = False

#create array to hold the index of the square for both players
posities = [0, 0]

#keep track of both players health
health = [100, 100]

#keep track of whos turn it is, 0 = player 1; 1 = player 2
beurt = 0

#declare here to upgrade scope so it can be renderd to the screen
worp = 0

#declare where banna peels are
peels = []
#load images
bord = pygame.image.load("assets/bord.png")
dice = pygame.image.load("assets/dice.png")
devilsDice = pygame.image.load("assets/devils dice.png")
peel = pygame.image.load("assets/placeholder50x50.png") 

#function for normal dice or space
def normal():

  #shit python :|
  global worp
  
  #choose a random number between 1 and 6 (including 1 and 6) and 
  worp = random.randint(1, 6)
  doBeurt()

#function for devils dice
def devilTurn():

  #python is garbage
  global worp
  global health
  global beurt

  #choose random number, avarage should be higher than normal dice, combined with a penalty it creates 'exciting' gameplay
  worp = random.randint(-16, 20)

  #player health should go down when they use a devils turn
  health[beurt] = health[beurt] - 10
  
  #because the game is ending we dont need propper turns anymore se we can reuse 'beurt'
  if health[beurt] <= 0:
    if beurt == 0:
      beurt = 1
    elif beurt == 1:
      beurt = 0

    #inform the players who won and exit
    print(f"player {beurt + 1} ({players[beurt]}) heeft gewonnen")
    pygame.quit()
    sys.exit()


  doBeurt()

#create a function for a turn and handing the turn over so multiple user inputs can trigger a turn
def doBeurt():

  #AANSCHOUW python being dogwater
  global beurt
  global worp
  global posities
  global players
  global debug
  
  #print the predcited moving info to the user
  #the moving prediction does not account for moving backwards at the end or negative turn that go below 0
  if debug:
    print(f"speler {beurt + 1} ({players[beurt]}) op plek {posities[beurt]} heeft {worp} gegooit en zou naar gaan {posities[beurt] + worp}")

  #if the dice is negative the predicted posision can be below 0, this must set the pos to 0
  if worp < 0 and posities[beurt] + worp < 0:
    posities[beurt] = 0
  
  #check if the playeu has reached the end, overshot the end or should just go forward
  #move forward
  elif (posities[beurt] + worp) < 63:

    posities[beurt] += worp

  #player has reached the end
  elif posities[beurt] + worp == 63:

    #inform the players who won and exit
    print(f"player {beurt + 1} heeft gewonnen")
    pygame.quit()
    sys.exit()

  #EXTRA FETURE: waneer je meer gooit dan nodig ga je acheruit, dus je moet exact gooien wat je nodig hebt
  #player has overshot the end
  elif posities[beurt] + worp > 63:

    posities[beurt] = 63 - (worp - (63 - posities[beurt]))

  skip = False

  #mysteryboxes at posities 3, 19, 24, 37, 43, 55
  for pos in [3, 19, 24, 37, 43, 55]:
    if posities[beurt] == pos:

      #lil debug
      if debug:
        print("pickup mysteryboxe")

      #0 is banna peel, 1 is skip turn, 2 is oponent moves backwards
      roll = random.randint(0, 2)
      #roll = 2

      #lil debug
      if debug:
        print(f"roll: {roll}")
      
      #setup variable to later make sure the player who placed the peel doesnt slip
      placedPeel = False

      #elif to handle mysteryboxes
      if roll == 0:

        #store where the peels are
        peels.append(posities[beurt])

        #make sure the player that places the peel doesnt slip
        placedPeel = True

        #player feedback
        print("someone landed on the peel")

      #handle making the opponent skip
      elif roll == 1:

        skip = True
        
        if debug:
          print("making oponent skip turn")
      
      #handle oponent being moved back 5 spaces without moving the player to negative positions
      elif roll == 2:
      
        #find out who the opponent is
        if beurt == 0:
          oponent = 1
        else:
          oponent = 0

        #print info
        print(f"player {oponent + 1} ({players[oponent]}) will has been moved back 5 spaces, from {posities[oponent]}, to {posities[oponent] - 5}")

        #move the player
        posities[oponent] = posities[oponent] - 5

        #handle negative spaces
        if posities[oponent] < 0:
          posities[oponent] = 0
      
      #check if the player landed on a peel, consider the placedPeel variable to make sure the player doesnt slip on their own peel
      for pos in peels:
        if posities[beurt] == pos and not placedPeel:
          posities[beurt] = posities[beurt] - 8

  #lil debug
  if debug:
    print(beurt)
    print(posities[beurt])

  #if the opponent has to skip their turn retun just before handing over the turn
  if skip:
    return

  #the place to put future code (put the code above this live so it stays accurate)

  #set the turn to the next player, whould use shorthand if python could:
  #beurt = !beurt or beurt = beurt == 1? 0 : 1
  if beurt == 0:

    beurt = 1

  elif beurt == 1:

    beurt = 0

#initialize pygame and a clock; set the name and size of the window
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1050, 754))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()

#auto fill names if debug is active, this makes debugging SO MUCH faster
if debug == False:
  player1Name = input("please enter player 1's name: ")
  player2Name = input("please enter player 2's name: ")
elif debug == True:
  player1Name = "Connor"
  player2Name = "Merijn"

players = [player1Name, player2Name]

#game loop
while True:

  #clear sceen from previous frame
  DISPLAYSURF.fill((255,255,255))

  #render images
  DISPLAYSURF.blit(bord, bord.get_rect())
  DISPLAYSURF.blit(dice, (dicePos[0], dicePos[1]))
  DISPLAYSURF.blit(devilsDice, (devilsDicePos[0], devilsDicePos[1]))

  #render banna peels
  for pos in peels:

    #extract x and y, center the image then render
    peelX = vakjes[pos][0] - 25
    peelY = vakjes[pos][1] - 25
    DISPLAYSURF.blit(peel, (peelX, peelY))

  #set a font to use, size 25
  font = pygame.font.SysFont(None, 25) 
  
  #get coords of tile to draw the player
  p1X = vakjes[posities[0]][0] - 5
  p1Y = vakjes[posities[0]][1] - 5
  p1C = (255, 20, 147)
  p1H = health[0]
  pygame.draw.circle(DISPLAYSURF, p1C, (p1X, p1Y), 10)
  pygame.draw.rect(DISPLAYSURF, p1C, (p1X - 20, p1Y - 30, 40, 10), 2)
  pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (p1X - 18, p1Y - 28, int((p1H / 100) * 36), 6), 0)
  DISPLAYSURF.blit(font.render(f"{players[0]}", 1, p1C), (p1X - 20, p1Y + 20)) 

  p2X = vakjes[posities[1]][0] + 5
  p2Y= vakjes[posities[1]][1] + 5
  p2C = (147, 20, 255)
  p2H = health[1]
  pygame.draw.circle(DISPLAYSURF, p2C, (p2X, p2Y), 10)
  pygame.draw.rect(DISPLAYSURF, p2C, (p2X - 20, p2Y - 30, 40, 10), 2)
  pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (p2X - 18, p2Y - 28, int((p2H / 100) * 36), 6), 0)
  DISPLAYSURF.blit(font.render(f"{players[1]}", 1, p2C), (p2X - 20, p2Y + 20)) 

  #render text on screen what was trown for the player
  #write the text in the colour black at 600, 460 with anitaliasing
  #a simplyfied version in provided below so other people can also use it
  #text = f"vorige worp: {worp}"
  #toRender = font.render(text, antialias: 1, color: black)
  #DISPLAYSURF.blit(toRender), coords: (600, 460)
  DISPLAYSURF.blit(font.render(f"vorige worp: {worp}", 1, (0, 0, 0)), (600, 460))

  #render text on screen whos turn it is for the player
  #write the text in the colour black at 600, 440 with anitaliasing
  #a simplyfied version in provided below so other people can also use it
  #text = f"aan de beurt: {beurt + 1}"
  #toRender = font.render(text, antialias: 1, color: black)
  #DISPLAYSURF.blit(toRender), coords: (600, 440)
  DISPLAYSURF.blit(font.render(f"aan de beurt: {players[beurt]}", 1, (0, 0, 0)), (600, 440))
  
  #get mouse pos to see if its on the dice
  mx, my = pygame.mouse.get_pos()
  #if debug:
  #  print(f"mx: {mx} my: {my}")
  
  #i could not be bothered to use some propper library so i just checked if the mouse is within the boundingbox of the dice
  if (mx > dicePos[0] and mx < dicePos[0] + dice.get_width()) and (my > dicePos[1] and my < dicePos[1] + dice.get_height()):
    hoveringDice = True
  else:
    hoveringDice = False

    #check if mouse is over the devils dice, since the mouse cant be over both dices at the same time indenting this block optimizes a tiny bit
    if (mx > devilsDicePos[0] and mx < devilsDicePos[0] + devilsDice.get_width()) and (my > devilsDicePos[1] and my < devilsDicePos[1] + devilsDice.get_height()):
      hoveringDevilsDice = True
    else:
      hoveringDevilsDice = False
  
  #get all events
  for event in pygame.event.get():

    #try find a mous event
    if event.type == pygame.MOUSEBUTTONDOWN:
      if hoveringDice:

        #if you hover over the dice and click trigger a normal turn
        normal()

      elif hoveringDevilsDice:

        #if you hover the devilsDice and click it triggers a devilTurn
        devilTurn()

    #try find a keydown event
    if event.type == pygame.KEYDOWN:

      #if there is a keydown event and the key of that event is space execute the moving logic
      if event.key == pygame.K_SPACE:

        #lil debug
        if debug:
          print("spatie")

        #pressing space triggers a normal turn
        normal()
        
      #handle game reset by checking for backspace and then resetting both positions to 0 and giving the turn to player 1
      elif event.key == pygame.K_BACKSPACE:
      
        if debug:
          print("backspace")
        posities[0] = 0
        posities[1] = 0
        beurt = 0

      #handle game end 
      elif event.type == QUIT:
          pygame.quit()
          sys.exit()
        
  #somothing to do with the clock that makes pygame funcion as exected; leave here & ignore
  clock.tick(60)
  
  #render prepared framebuffer to the screen      
  pygame.display.update()
