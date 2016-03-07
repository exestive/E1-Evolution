import pygame
from tileC import Tile
from random import randint

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
        self.image = pygame.image.load('R_Bronze.png')
        Character.__init__(self,x,y)
        Item.List.append(self)

    def draw_item(self,screen):
        for item in Item.List:
            screen.blit(self.image,(self.x,self.y))





class Item_1(Character):

    List = []

    def __init__(self,x,y):
        self.image = pygame.image.load('R_Silver.png')
        Character.__init__(self,x,y)
        Item.List.append(self)

    def draw_item(self,screen):
        for item in Item.List:
            screen.blit(self.image,(self.x,self.y))


class Item_2(Character):

    List = []

    def __init__(self,x,y):
        self.image = pygame.image.load('R_Gold.png')
        Character.__init__(self,x,y)
        Item.List.append(self)

    def draw_item(self,screen):
        for item in Item.List:
            screen.blit(self.image,(self.x,self.y))



class Item_3(Character):

    List = []

    def __init__(self,x,y):
        self.image = pygame.image.load('R_Diamond.png')
        Character.__init__(self,x,y)
        Item.List.append(self)

    def draw_item(self,screen):
        for item in Item.List:
            screen.blit(self.image,(self.x,self.y))




class Robot(Character):

    List = []
    

    def __init__(self,x,y):
        self.image = pygame.image.load('robotred40.png')
        Character.__init__(self,x,y)
        Robot.List.append(self)

    def draw(self,screen):
        for robot in Robot.List:
            screen.blit(self.image,(self.x,self.y))
