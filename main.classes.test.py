import pygame
from tileC import Tile
import Funk
from Objects import *


class Control():

    def __init__(self):
        self.screen = pygame.display.set_mode((720,440))
        self.crashed = False
        self.clock = pygame.time.Clock()
        self.frames = 27
        self.item1 = Item(200,240)
        self.robot = Robot(400,120)


        invalids = (1,2,3,4,5,6,7,8,9,10,11,12,
                    13,14,15,16,17,18,19,37,55,73,91,
                    109,127,145,163,181,182,183,184,185,186
                    ,187,188,189,190,191,192,193,194,195,196,197
                    ,198,36,54,72,90,108,126,144,162,180,198)

        for y in range(0,self.screen.get_height(),40):
            for x in range (0,self.screen.get_width(),40):
                if Tile.total_tiles in invalids:
                    Tile(x,y, 'solid')
                else:
                    Tile(x,y, 'empty')
                
        

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.crashed = True

    def game_loop(self):
        while not self.crashed:
            self.event()
            Tile.draw_tiles(self.screen)
            self.robot.draw(self.screen)
            Item.draw_item(self.screen)
            print(self.robot)
            print(self.item1)
            self.clock.tick(self.frames)
            pygame.display.update()

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('A.L.L Project')
    
    run = Control()
    run.game_loop()
    pygame.quit()


main()