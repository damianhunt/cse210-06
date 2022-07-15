import pygame
from constants import *
from casting.ship import Ship
from casting.laser import Laser
from casting.enemy import Enemy

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self._ship_img = YELLOW_SPACE_SHIP
        self._laser_img = YELLOW_LASER
        self._mask = pygame.mask.from_surface(self._ship_img)
        self._max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self._lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self._lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self._lasers:
                            self._lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self._x, self._y + self._ship_img.get_height() + 10, self._ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self._x, self._y + self._ship_img.get_height() + 10, self._ship_img.get_width() * (self._health/self._max_health), 10))
