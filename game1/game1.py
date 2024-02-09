#Thu vien chua pygame
import pygame
pygame.init

#Tieu de va icon game
pygame.display.set_caption('Game Test')
icon = pygame.image.load(r'E:\firstpythongame\game1\assets\yellowbird-downflap.png')
pygame.display.set_icon(icon)

#Cua so Terminal
screen = pygame.display.set_mode((1200,840))  #Kich thuoc man

#Vong lap(giu cua so terminal luon chay khi chua co ngoai le)
running = True
while running:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
