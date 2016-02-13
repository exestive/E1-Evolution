import pygame

class Robot(pygame.sprite.Sprite):
    """
    this class will get the robot and the mmovement

    """

    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.lead_x = 645
        self.lead_y = 520
        self.rect = self.image.get_rect(center=(self.lead_x,self.lead_x))

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



pygame.init()

def mainloop():
    clock = pygame.time.Clock()
    crashed = False
    
    #creating the background
    screen = pygame.display.set_mode((1280,640))
    background = pygame.image.load('back.png')
    screen.blit(background, (0,0))

    #calling classes
    space_ship = Robot('robot.png')



    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True



        #drawing the robot to the screen
        space_ship.movemnt()
        space_ship.draw(screen)
        

        
        pygame.display.update()
        clock.tick(27)
    

mainloop()



pygame.quit()
