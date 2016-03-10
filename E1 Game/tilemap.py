import pygame

class Tile(pygame.Rect):

    List = []
    width = 40
    height = 40
    total_tiles = 1
    H = 1
    V = 18
    

    def __init__(self, x, y, Type):

        self.parent = None
        self.H = 0
        self.G = 0
        self.F = 0

        self.type = Type
        self.number = Tile.total_tiles
        Tile.total_tiles += 1

        if Type == 'empty':
            self.walkable = True
        else:
            self.walkable = False

        pygame.Rect.__init__(self,(x,y), (Tile.width, Tile.height))
        Tile.List.append(self)


    def get_tile(number):
        for tile in Tile.List:
            if tile.number == number:
                return tile

    def draw_tiles(screen):
        half = Tile.width // 2
        
        for tile in Tile.List:
            if not tile.type == 'empty':
                pygame.draw.rect(screen, [40,40,40], tile)
