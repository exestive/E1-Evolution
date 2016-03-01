import pygame
from tileC import Tile

class Character(pygame.Rect):
    width = 40
    height = 40

    def __init__(self,x, y):
        pygame.Rect.__init__(self,x,y,Character.width, Character.height)

    def __str__(self):
        return str(self.get_number())

    def get_number(self):
        return (self.x / self.width + Tile.H) + (self.y / self.height) * Tile.V
        

    def get_tile(self):
        return Tile.get_tile(self.get_number())


class Item(Character):

    List = []

    def __init__(self,x,y):
        Character.__init__(self,x,y)
        Item.List.append(self)

    def draw_item(screen):
        for item in Item.List:
            pygame.draw.rect(screen,[210,24,77], item)

class Robot(Character):

    List = []

    def __init__(self,x,y):
        Character.__init__(self,x,y)
        Robot.List.append(self)

    def draw(self,screen):
        for robot in Robot.List:
            r = self.width // 2
            pygame.draw.circle(screen, [77,234,156], (self.x + r, self.y + r), r)
