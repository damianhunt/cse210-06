import pygame
from constants import *
from casting.ship import Ship
from casting.laser import Laser

class Enemy(Ship):
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self._ship_img, self._laser_img = self.COLOR_MAP[color]
        self._mask = pygame.mask.from_surface(self._ship_img)

    def move(self, vel):
        self._y += vel

    def shoot(self):
        if self._cool_down_counter == 0:
            laser = Laser(self._x-20, self._y, self._laser_img)
            self._lasers.append(laser)
            self._cool_down_counter = 1


#def collide(obj1, obj2):
#    offset_x = obj2.x - obj1.x
#    offset_y = obj2.y - obj1.y
#    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None