import pygame
from tileC import Tile
import Funk
from Objects import *
#from movement import *
from a_star import A_Star
import time


class Background(pygame.sprite.Sprite):
    """
    this class will get the backgorund item on screen

    """

    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()


    def draw(self,surface):
        surface.blit(self.image,(0,0))




class Control():

    def __init__(self):
        self.screen = pygame.display.set_mode((720,440))
        self.crashed = False
        self.clock = pygame.time.Clock()
        self.FPS = 7
        self.total_frames = 0
        self.total_frames +1
        self.item = Item(200,240)
        self.item_silver = Item_1(400,200)
        self.item_g = Item_2(330,370)
        self.item_d = Item_3(120,160)
        self.robot = Robot(360,220)
        self.time = 0.15
        self.background = Background('newback.png')
        self.key = pygame.key.get_pressed


        invalids = (163,181,182,197,198,180)

        for y in range(0,self.screen.get_height(),40):
            for x in range (0,self.screen.get_width(),40):
                if Tile.total_tiles in invalids:
                    Tile(x,y, 'solid')
                else:
                    Tile(x,y, 'empty')
                
        

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    A_Star(self.screen, self.item, self.total_frames, self.FPS)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    A_Star(self.screen, self.item_silver, self.total_frames, self.FPS)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    A_Star(self.screen, self.item_g, self.total_frames, self.FPS)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    A_Star(self.screen, self.item_d, self.total_frames, self.FPS)

        #interaction(self.screen, self.item, self.total_frames, self.FPS)


    def game_loop(self):
        while not self.crashed:
            self.background.draw(self.screen)
            self.total_frames +1
            self.event()
            #Item.spawn_item(self.total_frames, self.FPS)
            
            Tile.draw_tiles(self.screen)
            self.robot.draw(self.screen)
            self.item.draw_item(self.screen)
            self.item_silver.draw_item(self.screen)
            self.item_g.draw_item(self.screen)
            self.item_d.draw_item(self.screen)
            #print(self.robot)
            #print(self.item1)
            self.clock.tick(self.FPS)
            #time.sleep(self.time)
            pygame.display.flip()

            

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('A.L.L Project')
    
    run = Control()
    run.game_loop()
    pygame.quit()


main()
