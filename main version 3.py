import pygame


class Background(pygame.sprite.Sprite):
    """
    this class will get the backgorund item on screen

    """

    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()


    def draw(self,surface):
        surface.blit(self.image,(0,0))


class Robot(pygame.sprite.Sprite):
    """
    this class will get the robot and the mmovement

    """

    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.lead_x = 645
        self.lead_y = 520


    def movemnt(self):
        key = pygame.key.get_pressed()
        dist = 10
        if key[pygame.K_DOWN]:
            self.lead_y += dist
        elif key[pygame.K_UP]:
            self.lead_y -= dist
        if key[pygame.K_RIGHT]:
            self.lead_x += dist
        elif key[pygame.K_LEFT]:
            self.lead_x -= dist

    def draw(self,surface):
        surface.blit(self.image,(self.lead_x,self.lead_y))



class Coin(pygame.sprite.Sprite):
    """
    this class will get the coin item on screen

    """

    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.lead_x = 145
        self.lead_y = 220


    def draw(self,surface):
        surface.blit(self.image,(self.lead_x,self.lead_y))


class Control():

    def __init__(self):
        self.screen = pygame.display.set_mode((1280,640))
        self.crashed = False
        self.clock = pygame.time.Clock()
        self.frames = 27
        self.background = Background('back.png')
        self.space_ship = Robot('am_space_ship_thumb')
        self.item = Coin('coin.png')
        

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.crashed = True

    def game_loop(self):
        while not self.crashed:
            self.event()
            self.background.draw(self.screen)
            self.space_ship.draw(self.screen)
            self.space_ship.movemnt()
            self.item.draw(self.screen)
            self.clock.tick(self.frames)
            pygame.display.update()

def main():
    pygame.init()
    pygame.display.set_caption('A.L.L Project')
    
    run = Control()
    run.game_loop()
    pygame.quit()


main()
