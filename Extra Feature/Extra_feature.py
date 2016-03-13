import pygame
from tilemap import Tile
from a_star import A_Star

def interactive_tiles(screen,Mouse_position,event):
    Mouse_x = Mouse_position[0] // Tile.width
    Mouse_y = Mouse_position[1] // Tile.height

    for events in pygame.event.get():    
        if event.type == pygame.MOUSEBUTTONDOWN:
            for tile in Tile.List:
                if tile.x == (Mouse_x * Tile.width) and tile.y == (Mouse_y * Tile.width):
                    tile.type = 'solid'
                    tile.walkable = False
                    break



        
                    
            

