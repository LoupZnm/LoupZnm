import pygame, sys
import pygame.imageext
from pygame.locals import *
import globals as gl
class Labyrinthe :
    '''
    Créer un labyrinthe fonctionnel
    '''
    def __init__(self):
        #Carte 19 largeur (x) , 21 hauteur (y)
        self._tab_niveau = [ 
                     ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                     ['0','1','1','1','1','1','1','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['1','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['1','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['1','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'],
                     ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0'] ]
        
    def create(self):
        y=0
        for colonne in self._tab_niveau :
            x=0
            for tuile in colonne :
                if tuile == '1':
                    mur = pygame.image.load("1.png")
                    gl.fenetre.blit(mur,(x*16, y*16))
                if tuile == '0':
                    terrain = pygame.image.load("0.png")
                    gl.fenetre.blit(terrain,(x*16, y*16))
                x+=1
            y+=1
                
    def __str__(self):
        return 'work' 