import pygame, sys
import pygame.imageext
from pygame.locals import *
import globals as gl

pygame.init()
pygame.key.set_repeat(60)
FPS = 60
WIDTH, HEIGHT = 640, 680
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
lives = 3
score = 0


fenetre = pygame.display.set_mode((340, 480))
perso = pygame.image.load("pac.png").convert_alpha()
position_perso = perso.get_rect()


SCORE_FONT = pygame.font.SysFont("Arial", 24)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

GHOST_SIZE = 20
GHOST_SPEED = 2
PILL_SIZE = 10
ghost = pygame.Rect(WIDTH / 2 + 50, HEIGHT / 2, GHOST_SIZE, GHOST_SIZE)
pill = pygame.Rect(WIDTH / 2 + 100, HEIGHT / 2, PILL_SIZE, PILL_SIZE)
#direction perso :
Right = True
Left = False
Up = False
Down = False
direction = "left"
'''def MoveR () :
    global position_perso
    if event.key == pygame.K_RIGHT:
        Right = True
        Left = False
        Up = False
        Down = False
        while Right == True :
            position_perso = position_perso.move(gl.pas_deplacement,0)
            if Down == True : Right = False
            if Left == True : Right = False
            if Up == True : Right = False'''
    
running = True
while running :
    y=0
    for row in gl.tab_niveau :
        x=0
        for tuile in row :
            if tuile == '1':
                fenetre.blit(gl.mur,(x*16, y*16))
            if tuile == '0':
                fenetre.blit(gl.terrain,(x*16, y*16))
            x+=1
        y+=1
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

            #sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "up"
            while direction == "up":
                position_perso = position_perso.move(0,-gl.pas_deplacement)
            if event.key == pygame.K_DOWN:
                position_perso = position_perso.move(0,gl.pas_deplacement)
                
            if event.key == pygame.K_LEFT:
                position_perso = position_perso.move(-gl.pas_deplacement,0)
                
            if event.key == pygame.K_RIGHT:
                #MoveR()
                position_perso = position_perso.move(gl.pas_deplacement,0)
                
    if ghost.x < position_perso.x:
        ghost.x += GHOST_SPEED

    if ghost.x > position_perso.x:
        ghost.x -= GHOST_SPEED

    if ghost.y < position_perso.y:
        ghost.y += GHOST_SPEED

    if ghost.y > position_perso.y:
        ghost.y -= GHOST_SPEED
    pygame.draw.rect(screen, RED, ghost)
    pygame.draw.rect(screen, WHITE, pill)
    score_text = SCORE_FONT.render("Score: " + str(score), True, WHITE)

    lives_text = SCORE_FONT.render("Lives: " + str(lives), True, WHITE)

    screen.blit(score_text, (10, 10))

    screen.blit(lives_text, (10, 30))

    pygame.display.flip()
    fenetre.fill([0,0,0])
    fenetre.blit(perso, position_perso)
    pygame.time.Clock().tick(FPS)

pygame.quit()