import pygame
from Objects import *
from tileC import Tile

  
def A_Star(screen, item, total_frames, FPS):
    
    half = Tile.width // 2

    N = -18
    S = 18
    E = 1
    W = -1

    NW = -19
    NE = -17
    SE = 19
    SW = 17

    for tile in Tile.List:
        tile.parent = None
        tile.H = 0
        tile.G = 0
        tile.F = 0

    def movement(tiles, diagonals, surrounding_node):
        if surrounding_node.number not in diagonals:
            tiles.append(surrounding_node)
        return tiles

    def get_surrounding_tiles(starting_node):
        
        array =(
            (starting_node.number + N),
            (starting_node.number + NE),
            (starting_node.number + E),
            (starting_node.number + SE),
            (starting_node.number + S),
            (starting_node.number + SW),
            (starting_node.number + W),
            (starting_node.number + NW),
            )

        tiles = []

        onn = starting_node.number 
        diagonals = [onn + NE, onn + NW, onn + SE, onn + SW]

        for tile_number in array:

            surrounding_tile = Tile.get_tile(tile_number)
            if tile_number not in range(1, Tile.total_tiles + 1):
                continue

            if surrounding_tile.walkable and surrounding_tile not in closed_list:
                # tiles.append(surrounding_tile) # Diagonal movement
                tiles = movement(tiles, diagonals, surrounding_tile)

        return tiles

    def G(tile):
        
        diff = tile.number - tile.parent.number

        if diff in (N, S, E, W):
            tile.G = tile.parent.G + 10
        elif diff in (NE, NW, SW, SE):
            tile.G = tile.parent.G + 14

    def H():
        for tile in Tile.List:
            tile.H = 10 * (abs(tile.x - item.x) + abs(tile.y - item.y)) / Tile.width

    def F(tile):
        # F = G + H
        tile.F = tile.G + tile.H

    def swap(tile):
        open_list.remove(tile)
        closed_list.append(tile)

    def get_LFV(): # get Lowest F Value

        F_Values = []
        for tile in open_list:
            F_Values.append(tile.F)

        o = open_list[::-1]

        for tile in o:
            if tile.F == min(F_Values):
                return tile

    def move_to_G_cost(LFV, tile):

        G_value = 0
        diff = LFV.number - tile.number

        if diff in (N, S, E, W):
            G_value = LFV.G + 10
        elif diff in (NE, NW, SE, SW):
            G_value = LFV.G + 14

        return G_value

    def loop():

        LFV = get_LFV() 

        swap(LFV)
        surrounding_nodes = get_surrounding_tiles(LFV)

        for node in surrounding_nodes:

            if node not in open_list:

                open_list.append(node)
                node.parent = LFV

            elif node in open_list:
                
                cal_G = move_to_G_cost(LFV, node)
                if cal_G < node.G:

                    node.parent = LFV
                    G(node)
                    F(node)

        if open_list == [] or item.get_tile() in closed_list:
            return

        for node in open_list:
            G(node)
            F(node)

            # pygame.draw.line(screen, [255, 0, 0],
            # [node.parent.x + half, node.parent.y + half],
            # [node.x + half, node.y + half] )

        loop()

        

    for robot in Robot.List:

        open_list = []
        closed_list = []

        robot_tile = robot.get_tile()
        open_list.append(robot_tile)

        surrounding_nodes = get_surrounding_tiles(robot_tile)

        for node in surrounding_nodes:
            node.parent = robot_tile
            open_list.append(node)      

        swap(robot_tile)

        H()

        for node in surrounding_nodes:
            G(node)
            F(node) 

        loop()

        return_tiles = []

        parent = item.get_tile()

        while True:

            return_tiles.append(parent)

            parent = parent.parent

            if parent == None:
                break

            if parent.number == robot.get_number():
                break

        #for tile in return_tiles:
            #pygame.draw.circle(screen, [34, 95, 200],
            #[tile.x + half - 2, tile.y + half - 2], 5 )

        if len(return_tiles) > 1:
            if total_frames % (FPS / 4) == 0:
                next_tile = return_tiles[-1]
                robot.x = next_tile.x
                robot.y = next_tile.y


            
