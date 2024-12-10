import pygame, sys
import pygame.imageext
from pygame.locals import *
import globals as gl
class Perso :
    '''
        Affiche pac-man et le gère 
    '''
    def __init__(self) :
        self._perso = pygame.image.load("pac.png").convert_alpha()
        self._position_perso = self._perso.get_rect()
        self._lives = 3
        self._direction = "Right"
    
    def get_lives(self):
        return self._lives
    def get_position_perso(self):
        return self._position_perso
    
    def set_lives(self,pv) :
        self._lives += pv
    def set_position_perso(self,pos) :
        self._position_perso = pos
    
    def create(self):
        gl.fenetre.blit(self._perso,self._position_perso)
    
    def set_direction(self,dir):
        self._direction = dir
    def get_direction(self):
        return self._direction
        
    def deplacer(self) :
        if self.get_direction() == "Right" :
            self._position_perso = self._position_perso.move(10,0)
        if self.get_direction() == "Left" :
            self._position_perso = self._position_perso.move(-10,0)
        if self.get_direction() == "Up" :
            self._position_perso = self._position_perso.move(0,10)
        if self.get_direction() == "Down" :
            self._position_perso = self._position_perso.move(0,-10)