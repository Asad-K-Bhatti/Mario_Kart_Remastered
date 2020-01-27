#_________________________________________________________________Libraries_________________________________________________________________#
import pygame,random,sys,time,os
from os import path

#_____________________________________________________________Display Settings______________________________________________________________#
pygame.init()

display_width = 1400
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bright_red = (196,43,43)
deep_red = (69,7,31)

#_______________________________________________________________Image/Music_________________________________________________________________#
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Chicken Slayer Z')
clock = pygame.time.Clock()

backgroundimg = pygame.image.load('Backgrounds\mainmenu.png')

#_________________________________________________________________Image Functions____________________________________________________________#
def background_display(x,y):
    gameDisplay.blit(backgroundimg, (x,y))

#_________________________________________________________________File Functions_____________________________________________________________#
def instruc_file():
    os.startfile('Instructions.py')

def game_file():
    os.startfile('stageone.py')

def game_message():
    os.startfile('message.py')

def game_references():
    os.startfile('references.py')

def game_website():
    os.startfile('Grade-12-Computer-Science-Summative\Chicken Slayer Z Website\index.html')

#_____________________________________________________________Interface Functions____________________________________________________________#
def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def display_message(message,x,y):
    Largetext = pygame.font.SysFont("comicsansbold", 60)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)

def message(message):
    Largetext = pygame.font.SysFont("comicsansms", 30)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)

def small_text_display(msg, x, y):
    Smalltext = pygame.font.Font("freesansbold.ttf",10)
    textSurf, textRect = text_objects(msg, Smalltext)
    textRect.center = ((x), (y))
    gameDisplay.blit(textSurf, textRect)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_file()
                quit()
            if action == "instructions":
                instruc_file()
                quit()
            if action == "worldmessage":
                game_message()
                quit()
            if action == "references":
                game_references()
                quit()
            if action == "website":
                game_website()
                quit()
            if action == "quit":
                pygame.quit()
                quit()
                
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    Smalltext = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, Smalltext)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect)
    
#_________________________________________________________________Game Function______________________________________________________________#
def game_intro():

    start = True
    while start == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        background_display(0,0)
        small_text_display("This game is not affiliated with Chicken Invaders", 400, 570)
        small_text_display("Copyright © ATV.Inc 2018", 400, 580)
        button("Play",200, 150, 150, 50, deep_red, bright_red,"play")
        button("How to Play",500, 150, 150, 50, deep_red, bright_red,"instructions")
        button("World Message",200, 230, 150, 50, deep_red, bright_red, "worldmessage")
        button("Website",500, 230, 150, 50, deep_red, bright_red,"website")
        button("Quit",500, 230, 150, 50, deep_red, bright_red,"quit")
        high_score_display("The current high score is: ", highscore, 400, 100)
        
        pygame.display.update()
        clock.tick(60)

#______________________________________________________________Program Output_____________________________________________________________#
while True:
    game(display_width, graphics, plife, blife, player_width, blastx, blasty, blastspeed, boss_width, bossx, bossy, bossspeed, eggx, eggy, eggspeed)
    pygame.quit()
    quit()
