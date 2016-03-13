import pygame
from tilemap import Tile
from Objects import *
from a_star import A_Star
from Extra_feature import *
import sys


class Background(pygame.sprite.Sprite):
    """
    this class will get image for the backgorund and will blits
    onto screen when its called

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
        self.item_d = Item_3(120,160)
        self.robot = Robot(360,60)
        self.background = Background('newback.png')
        self.key = pygame.key.get_pressed




        invalids = (163,181,182,197,198,180,1,37,
                    55,73,91,109,127,145,18,36,54,72,90,108,126,
                    144,162,19,56,57,39)

        for y in range(0,self.screen.get_height(),40):
            for x in range (0,self.screen.get_width(),40):
                if Tile.total_tiles in invalids:
                    Tile(x,y, 'solid')
                else:
                    Tile(x,y, 'empty')
                
        

    def event(self):
        Mouse_position = pygame.mouse.get_pos()
        Mouse_x = Mouse_position[0] // Tile.width
        Mouse_y = Mouse_position[1] // Tile.height
        
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
                    A_Star(self.screen, self.item_d, self.total_frames, self.FPS)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    Character.sortByValue_ascending()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    Character.sortByValue_descending()


            if event.type == pygame.MOUSEBUTTONDOWN:
                for tile in Tile.List:
                    if tile.x == (Mouse_x * Tile.width) and tile.y == (Mouse_y * Tile.width):
                        tile.type = 'solid'
                        tile.walkable = False
                        break

     


    def game_loop(self):
        while not self.crashed:
            self.background.draw(self.screen)
            self.total_frames +1
            self.event()
            #interactive_tiles(self.screen,self.Mouse_position, self.events)
            Tile.draw_tiles(self.screen)
            self.robot.draw(self.screen)
            self.item.draw_item(self.screen,self.robot)
            self.item_silver.draw_item(self.screen,self.robot)
            self.item_d.draw_item(self.screen,self.robot)
            self.clock.tick(self.FPS)
            pygame.display.flip()

            

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('A.L.L Project')
    
    run = Control()
    run.game_loop()
    pygame.quit()


if __name__ == '__main__':
    main()
