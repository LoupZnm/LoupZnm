import pygame, sys
import pygame.imageext
from pygame.locals import *
import globals as gl
from labyrinthe import Labyrinthe
from perso import Perso

pygame.init()
pygame.key.set_repeat(60)
FPS = 60
WIDTH, HEIGHT = 340, 340
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
score = 0
pacperso = Perso()
pacperso.get_lives()


SCORE_FONT = pygame.font.SysFont("Arial", 24)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

GHOST_SIZE = 20
GHOST_SPEED = 2
PILL_SIZE = 10
ghost = pygame.Rect(WIDTH / 2 + 50, HEIGHT / 2, GHOST_SIZE, GHOST_SIZE)
pill = pygame.Rect(WIDTH / 2 + 100, HEIGHT / 2, PILL_SIZE, PILL_SIZE)

paclab = Labyrinthe()

running = True
while running :
    print(paclab)
    paclab.create()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

            #sys.exit()
    if pygame.event.get() == K_RIGHT :
        pacperso.set_direction("Right")
    if pygame.event.get() == K_LEFT :
        pacperso.set_direction("Left")
    if pygame.event.get() == K_UP :
        pacperso.set_direction("Up")
    if pygame.event.get() == K_DOWN :
        pacperso.set_direction("Down")
        
                
    if ghost.x < pacperso.get_position_perso().x:
        ghost.x += GHOST_SPEED

    if ghost.x > pacperso.get_position_perso().x:
        ghost.x -= GHOST_SPEED

    if ghost.y < pacperso.get_position_perso().y:
        ghost.y += GHOST_SPEED

    if ghost.y > pacperso.get_position_perso().y:
        ghost.y -= GHOST_SPEED
    
    pygame.draw.rect(screen, WHITE, pill)
    pacperso.create()
    pygame.draw.rect(screen, RED, ghost)
    
    score_text = SCORE_FONT.render("Score: " + str(score), True, WHITE)
    lives_text = SCORE_FONT.render("Lives: " + str(pacperso.get_lives()), True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 30))

    pygame.display.flip()
    gl.fenetre.fill([0,0,0])
    pygame.time.Clock().tick(FPS)

pygame.quit()