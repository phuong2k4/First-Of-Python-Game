#Thu vien chua pygame
import pygame
pygame.init( )

#Hang trong luc
p = 0.2
bird_y = 0 #vi tri bat len 
score=0 #Khoi tao diem
highScore = 0
game_play = True

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
bird_hcn = bird.get_rect(center=(100,296))

#Ham check va cham
def check_vc():
    if bird_hcn.bottom>=850 or bird_hcn.top <= -75:
        return False
    else:
        return True
#Tao man hinh khoi dau

#Tao man hinh out game
screen_out = pygame.image.load(r'E:\firstpythongame\game1\assets\gameover.png')
screen_out = pygame.transform.scale2x(screen_out)
screen_out_hcn = screen_out.get_rect(center=(216,384))

#Cua so Terminal
screen = pygame.display.set_mode((432,768))  #Kich thuoc man

#score
game_font = pygame.font.Font(r'E:\firstpythongame\game1\04B_19.TTF',40)
def score_view():
    if game_play: 
        score_f = game_font.render(f'Score: {(int(score))}',True,(255,255,255))
        score_hcn = score_f.get_rect(center=(200,100))
        screen.blit(score_f,score_hcn)
    if game_play==False:
        #High Score
        highScore = game_font.render(f'High Score: {(int(score))}',True,(255,255,255))
        highScore_hcn = highScore.get_rect(center=(200,100))
        screen.blit(highScore,highScore_hcn)
#Vong lap(giu cua so terminal luon chay khi chua co ngoai le)
running = True
while running:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type== pygame.KEYDOWN:
            #if game allway true 
            if event.key == pygame.K_SPACE and game_play:
                bird_y = -10
                #if u touch a float or highest sky
            if event.key == pygame.K_SPACE and game_play == False:
                game_play = True
                bird_y = 0
                score = 0 
                bird_hcn.center=(100,296)
    screen.blit(bg,(0,0))
    fl_x-=0.5
    screen.blit(fl,(fl_x,700))
    screen.blit(fl,(fl_x+432,700))
    if fl_x==-432:
        fl_x=0

    if game_play:
    #Get a bird transition like real life
        screen.blit(bird,bird_hcn)
        bird_y += p
        bird_hcn.centery += bird_y
        score+=0.01
        if score > highScore:
            highScore = score
        score_view()
        game_play = check_vc()
    else:
        screen.blit(screen_out,screen_out_hcn)
        score_view()
    pygame.display.update()



    #the last of upadte
    