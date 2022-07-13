from msilib.schema import Class
import pygame
from constants import *
from casting.laser import Laser

class Ship:
    '''
    An object with which to do battle.
    Responsible for keeping track of all ships present in the game.
    '''
    
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self._x = x
        self._y = y
        self._health = health
        self._ship_img = None
        self._laser_img = None
        self._lasers = []
        self._cool_down_counter = 0

    def draw(self, window):
        window.blit(self._ship_img, (self._x, self._y))
        for laser in self._lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self._lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self._lasers.remove(laser)

    def cooldown(self):
        if self._cool_down_counter >= self.COOLDOWN:
            self._cool_down_counter = 0
        elif self._cool_down_counter > 0:
            self._cool_down_counter += 1

    def shoot(self):
        if self._cool_down_counter == 0:
            laser = Laser(self._x, self._y, self._laser_img)
            self._lasers.append(laser)
            self._cool_down_counter = 1

    def get_width(self):
        return self._ship_img.get_width()

    def get_height(self):
        return self._ship_img.get_height()
    
    # Inherit Laser class and override it.
    class Ship(Laser):
        '''
        Handles the firing of the laser.
        '''
        
        def __init__(self, x, y, img):
            self._x = x
            self._y = y
            self._img = img
            self._mask = pygame.mask.from_surface(self.img)

        def draw(self, window):
            window.blit(self._img, (self._x, self._y))

        def move(self, vel):
            self._y += vel

        def off_screen(self, height):
            return not(self._y <= height and self._y >= 0)

        def collision(self, obj):
            return collide(self, obj)

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1._mask.overlap(obj2._mask, (offset_x, offset_y)) != None