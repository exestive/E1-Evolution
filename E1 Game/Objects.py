import pygame
from tilemap import Tile


class Character(pygame.Rect):
    width = 40
    height = 40

    inventory = {'Bronze' : 0,
                 'Silver' : 0,
                 'Diamond': 0}

    def __init__(self,x, y):
        pygame.Rect.__init__(self,x,y,Character.width, Character.height)

    def __str__(self):
        return str(self.get_number())

    def get_number(self):
        return (self.x / self.width + Tile.H) + (self.y / self.height) * Tile.V
        

    def get_tile(self):
        return Tile.get_tile(self.get_number())

    def sortByValue_ascending():
        sort = sorted(Character.inventory.items(), key = lambda t:t[1])
        print (sort)

    def sortByValue_descending():
        sort = sorted(Character.inventory.items(), key = lambda t:t[1], reverse=True)
        print (sort)

    


class Item(Character):

    List = []
    newList = []

    def __init__(self,x,y):
        self.image = pygame.image.load('R_Bronze.png')
        Character.__init__(self,x,y)
        Item.List.append(self)
        Item.newList.append(self)

    def draw_item(self,screen,robot):
        for item in Item.newList:
            screen.blit(self.image,(self.x,self.y))
            
            if robot.x % Tile.width == 0 and robot.y % Tile.height == 0:
                    if item.x % Tile.width == 0 and item.y % Tile.height == 0:

                        tile_number = item.get_number()

                        north = tile_number + -(Tile.V)
                        south = tile_number + (Tile.V)
                        east = tile_number + (Tile.H)
                        west = tile_number + -(Tile.H)

                        compass = [north,south,east,west, tile_number]

                        if robot.get_number() in compass:
                            print('Congratulations you collected a bronze chest')
                            Character.inventory.update({'Bronze' : 10})
                            Item.newList.remove(self)
                            print(Character.inventory)
            break





class Item_1(Character):

    List = []
    newList = []

    def __init__(self,x,y):
        self.image = pygame.image.load('R_Silver.png')
        Character.__init__(self,x,y)
        Item_1.List.append(self)
        Item_1.newList.append(self)

    def draw_item(self,screen,robot):
        for item in Item_1.newList:
            screen.blit(self.image,(self.x,self.y))

            if robot.x % Tile.width == 0 and robot.y % Tile.height == 0:
                    if item.x % Tile.width == 0 and item.y % Tile.height == 0:

                        tile_number = item.get_number()

                        north = tile_number + -(Tile.V)
                        south = tile_number + (Tile.V)
                        east = tile_number + (Tile.H)
                        west = tile_number + -(Tile.H)

                        compass = [north,south,east,west, tile_number]


                        if robot.get_number() in compass:
                            print('Congratulations you collected a silver chest')
                            Character.inventory.update({'Silver' : 15})
                            Item_1.newList.remove(self)
                            print(Character.inventory)
            break





class Item_3(Character):

    List = []
    newList = []

    def __init__(self,x,y):
        self.image = pygame.image.load('R_Diamond.png')
        Character.__init__(self,x,y)
        Item_3.List.append(self)
        Item_3.newList.append(self)

    def draw_item(self,screen,robot):
        for item in Item_3.newList:
            screen.blit(self.image,(self.x,self.y))

                        
            if robot.x % Tile.width == 0 and robot.y % Tile.height == 0:
                    if item.x % Tile.width == 0 and item.y % Tile.height == 0:

                        tile_number = item.get_number()

                        north = tile_number + -(Tile.V)
                        south = tile_number + (Tile.V)
                        east = tile_number + (Tile.H)
                        west = tile_number + -(Tile.H)

                        compass = [north,south,east,west, tile_number]


                        if robot.get_number() in compass:
                            print('Congratulations you collected a diamond chest')
                            Character.inventory.update({'Diamond' : 7})
                            Item_3.newList.remove(self)
                            print(Character.inventory)
            break
                        




class Robot(Character):

    List = []
    

    def __init__(self,x,y):
        self.image = pygame.image.load('robotred40.png')
        Character.__init__(self,x,y)
        Robot.List.append(self)

    def draw(self,screen):
        for robot in Robot.List:
            screen.blit(self.image,(self.x,self.y))


