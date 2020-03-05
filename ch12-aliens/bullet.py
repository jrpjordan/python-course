import pygame
from pygame.sprite import Sprite

# inherits from sprite makes to treat all the instances in the game as a single object
class Bullet(Sprite):
    """ Class for manage bullets shooted from the ship. """
    
    def __init__(self, ai_game):
        """ Create an object at the ship current's position. """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet in rect(0,0) and set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet's position at a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """ Move the bullet up the screen. """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet to the screen. """
        pygame.draw.rect(self.screen, self.color, self.rect)
