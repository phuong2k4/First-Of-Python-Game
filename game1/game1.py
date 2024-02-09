#Thu vien chua pygame
import pygame
pygame.init
#Hang trong luc
p = 0.2
bird_y = 0
#Tieu de va icon game
pygame.display.set_caption('Game Test')
icon = pygame.image.load(r'E:\firstpythongame\game1\assets\yellowbird-downflap.png')
pygame.display.set_icon(icon)

#Set background cho game
bg = pygame.image.load(r'E:\firstpythongame\game1\assets\background-night.png')
bg=pygame.transform.scale2x(bg)
#Set a float for 
fl= pygame.image.load(r'E:\firstpythongame\game1\assets\floor.png')
fl=pygame.transform.scale2x(fl)
fl_x=0
#Set a bird for a game
bird = pygame.image.load(r'E:\firstpythongame\game1\assets\yellowbird-midflap.png')
bird = pygame.transform.scale2x(bird)
bird_hcn = bird.get_rect(center=(100,386))
#Cua so Terminal
screen = pygame.display.set_mode((432,768))  #Kich thuoc man

#Vong lap(giu cua so terminal luon chay khi chua co ngoai le)
running = True
while running:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y = -10      
    screen.blit(bg,(0,0))
    fl_x-=0.5
    screen.blit(fl,(fl_x,600))
    screen.blit(fl,(fl_x+432,600))
    if fl_x==-432:
        fl_x=0
    #Get a bird transition like real life
    screen.blit(bird,bird_hcn)
    bird_y += p
    bird_hcn.centery += bird_y
    pygame.display.update()