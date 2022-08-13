#=========Imports==========================

import runer
from buttons import *

#===========G. Vars========================

bg = pygame.image.load("2.png")
x = ""#click
y = ""#hover
win = pygame.display.set_mode([600, 600])
pygame.display.set_caption("Main Menu for GHub!")
run = True
b1 = Button(0, 0, 200, 200, (104, 41, 205), "Tower Defence", (88, 247, 136))
b2 = Button(400, 0, 200, 200, (104, 41, 205), "Lario Kart", (88, 247, 136))
b3 = Button(200, 200, 200, 200, (104, 41, 205), "Apocales", (88, 247, 136))
b4 = Button(0, 400, 200, 200, (104, 41, 205), "Rock Paper Sissors server", (88, 247, 136))
b5 = Button(400, 400, 200, 200, (104, 41, 205), "Rock Paper Sissors Online", (88, 247, 136))
buttons = [b1, b2, b3, b4, b5]

#===========FUNctions=======================

def which_one(i):
    if i is b1:
        return "tdg"
    elif i is b2:
        return "kart"
    elif i is b3:
        return "fps"
    elif i is b4:
        return "gole"
    elif i is b5:
        return "rps"
#===========spagetti code===================

while run:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            run = False
    if y != "" or x != "":
        if x == "kart":
            bg = pygame.image.load("1.png")
            pygame.display.flip()
            runer.open(runer.games["kart"], runer.x)
            pygame.quit()
            quit()            
        elif y == "kart":
            bg = pygame.image.load("1.png")
        elif x == "tdg":
            bg = pygame.image.load("0.png")
            pygame.display.flip()
            runer.open(runer.games["tdg"], runer.x)
            pygame.quit()
            quit()            
        elif y == "tdg":
            bg = pygame.image.load("0.png")
        elif x == "fps":
            bg = pygame.image.load("3.png")
            pygame.display.flip()
            runer.open(runer.games["fps"], runer.x)
            pygame.quit()
            quit()            
        elif y == "fps":
            bg = pygame.image.load("3.png")
        elif x == "gole":
            bg = pygame.image.load("4.png")
            pygame.display.flip()
            runer.open(runer.games["gole.sv"], runer.x)
            runer.open(runer.games["rps"], runer.x)
            x = ""            
        elif y == "gole":
            bg = pygame.image.load("4.png")
        elif x == "rps":
            bg = pygame.image.load("5.png")
            pygame.display.flip()
            runer.open(runer.games["rps"], runer.x)
            pygame.quit()
            quit()            
        elif y == "rps":
            bg = pygame.image.load("5.png")
        
        
    pos = pygame.mouse.get_pos()
    for i in buttons:
       if i.clicked(pos):
           y = which_one(i)
    left, middle, right = pygame.mouse.get_pressed()
    if left:
        for i in buttons:
            if i.clicked(pos):
                x = which_one(i)
    win.blit(bg, [0, 0, 640, 640])
    b1.draw(win)
    b2.draw(win)
    b3.draw(win)
    b4.draw(win)
    b5.draw(win)
    pygame.display.flip()
