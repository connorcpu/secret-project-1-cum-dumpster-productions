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

#create array to hold the index of the square for both players
posities = [0, 0]

#keep track of whos turn it is, 0 = player 1; 1 = player 2
beurt = 0

#declare here to upgrade scope so it can be renderd to the screen
worp = 0

#initialize pygame and a clock; set the name and size of the window
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1050, 754))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()

player1Name = input("please enter player 1's name: ")
player2Name = input("please enter player 2's name: ")
players = [player1Name, player2Name]

#game loop
while True:

  #clear sceen from previous frame
  DISPLAYSURF.fill((255,255,255))

  #load image
  bord = pygame.image.load("bord.png")
      
  #render image
  DISPLAYSURF.blit(bord, bord.get_rect())

  font = pygame.font.SysFont(None, 25) 
  #get coords of tile to draw the player
  p1X = vakjes[posities[0]][0]
  p1Y = vakjes[posities[0]][1]
  p1C = (255, 20, 147)
  pygame.draw.circle(DISPLAYSURF, p1C, (p1X, p1Y), 10)
  DISPLAYSURF.blit(font.render(f"{players[0]}", 1, (0, 0, 0)), (p1X - 20, p1Y + 20)) 

  p2X = vakjes[posities[1]][0] + 3
  p2Y= vakjes[posities[1]][1] + 3
  p2C = (147, 20, 255)
  pygame.draw.circle(DISPLAYSURF, p2C, (p2X, p2Y), 10)
  DISPLAYSURF.blit(font.render(f"{players[1]}", 1, (0, 0, 0)), (p2X - 20, p2Y + 20)) 
  #set a font to use, size 25

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
  
  #mouse
  #mx, my = pygame.mouse.get_pos()
  #player
  #pygame.draw.circle(DISPLAYSURF, (0, 255, 0), (mx, my), 10)

  #get all events
  for event in pygame.event.get():

    #try find a keydown event
    if event.type == pygame.KEYDOWN:

      #if there is a keydown event and the key of that event is space execute the moving logic
      if event.key == pygame.K_SPACE:

        #lil debug
        print("spatie")

        #choose a random number between 1 and 6 (including 1 and 6) and print the predcited moving info to the user
        #the moving prediction does not account for moving backwards at the end
        worp = random.randint(1, 6)
        print(f"speler {beurt + 1} ({players[beurt]}) op plek {posities[beurt]} heeft {worp} gegooit en zou naar gaan {posities[beurt] + worp}")

        #check if the playeu has reached the end, overshot the end or should just go forward
        #move forward
        if (posities[beurt] + worp) < 63:
      
          posities[beurt] += worp

        #player has reached the end
        elif posities[beurt] + worp == 63:
      
          print(f"player {beurt + 1} heeft gewonnen")
          pygame.event.post(pygame.event.Event(pygame.QUIT))

        #EXTRA FETURE: waneer je meer gooit dan nodig ga je acheruit, dus je moet exact gooien wat je nodig hebt
        #player has overshot the end
        elif posities[beurt] + worp > 63:

          posities[beurt] = 63 - (worp - (63 - posities[beurt]))

        #lil debug
        print(beurt)
        print(posities[beurt])

        #the place to put futur code (put the code above this live so it stays accurate)

        #set the turn to the next player, whould use shorthand if python could:
        #beurt = !beurt or beurt = beurt == 1? 0 : 1
        if beurt == 0:
      
          beurt = 1
      
        elif beurt == 1:
      
          beurt = 0

      #handle game reset by checking for backspace and then resetting both positions to 0 and giving the turn to player 1
      elif event.key == pygame.K_BACKSPACE:
      
        print("backspace")
        posities[0] = 0
        posities[1] = 0
        beurt = 0

  #somothing to do with the clock that makes pygame funcion as exected; leave here & ignore
  clock.tick(60)

  #handle game end 
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
        
  #render prepared framebuffer to the screen      
  pygame.display.update()