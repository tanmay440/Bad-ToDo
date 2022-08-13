import pygame
import assets

clock = pygame.time.Clock()
win = pygame.display.set_mode((1365, 768))

#=================ROW 1====================

button1 = assets.Button(0, 0, 452, 253, (12, 12, 12), "", (255, 255, 255))
button2 = assets.Button(455, 0, 452, 253, (12, 12, 12), "", (255, 255, 255))
button3 = assets.Button(910, 0, 452, 253, (12, 12, 12), "", (255, 255, 255))

#=================ROW 2======================

button4 = assets.Button(0, 256, 452, 253, (12, 12, 12), "", (255, 255, 255))
button5 = assets.Button(455, 256, 452, 253, (12, 12, 12), "", (255, 255, 255))
button6 = assets.Button(910, 256, 452, 253, (12, 12, 12), "", (255, 255, 255))

#=================ROW 3=======================

button7 = assets.Button(0, 512, 452, 253, (12, 12, 12), "", (255, 255, 255))
button8 = assets.Button(455, 512, 452, 253, (12, 12, 12), "", (255, 255, 255))
button9 = assets.Button(910, 512, 452, 253, (12, 12, 12), "", (255, 255, 255))
buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]


click = True
def messagebox(text):
    button_font = pygame.font.SysFont("Impact", 22)
    text_surface = button_font.render(text, 1, (45, 167, 235))
    win.blit(text_surface, (1365 /
                            2 - text_surface.get_width()/2, 768/2 - text_surface.get_height()/2))

def anyone_won():
    '''WIN CHECK FOR TIC TACK TOE'''
    if(button1.text == "X" and button2.text == "X" and button3.text == "X" or
         button4.text == "X" and button5.text == "X" and button6.text == "X" or
         button7.text == "X" and button8.text == "X" and button9.text == "X" or
         button3.text == "X" and button6.text == "X" and button9.text == "X" or
         button5.text == "X" and button2.text == "X" and button8.text == "X" or
         button1.text == "X" and button4.text == "X" and button7.text == "X" or
         button1.text == "X" and button5.text == "X" and button9.text == "X" or
         button3.text == "X" and button5.text == "X" and button7.text == "X" ):
        win.fill((0, 0, 0))
        messagebox("X has won a game")
        return
        
        
        
    if(button1.text == "O" and button2.text == "O" and button3.text == "O" or
         button4.text == "O" and button5.text == "O" and button6.text == "O" or
         button7.text == "O" and button8.text == "O" and button9.text == "O" or
         button3.text == "O" and button6.text == "O" and button9.text == "O" or
         button5.text == "O" and button2.text == "O" and button8.text == "O" or
         button1.text == "O" and button4.text == "O" and button7.text == "O" or
         button1.text == "O" and button5.text == "O" and button9.text == "O" or
         button3.text == "O" and button5.text == "O" and button7.text == "O" ):
        win.fill((0, 0, 0))
        messagebox("O has won a game")
        return
    i = 0
    for x in buttons:
        if x == "":
            continue
        i += 1
    
    if i == 9:
        
        return"Tie"
        
        

        
def whoose_turn():
    '''
    TURN DECIDER
    '''
    global click
    if click == True:
        click = False
    elif click == False:
        click = True


run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():  
        
        if event.type == pygame.QUIT:
            run = False
    
    win.fill((45, 167, 235))
    
    left, middle, right = pygame.mouse.get_pressed()
    
    if left:
        pos = pygame.mouse.get_pos()

        for i in buttons:
            x = i.clicked(pos)

            if x:

                if click and i.text == "":
                    i.text = "O"
                    
                elif i.text == "" and click == False:
                    i.text = "X"

                click = not click

    for i in buttons:
        i.draw(win)

    
    messagebox(anyone_won())
    pygame.display.flip()
    