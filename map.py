import pygame, sys, copy, random
from pygame.locals import *

def evolution():
    pygame.init()
    screen=pygame.display.set_mode((900,450))
    screenRect=screen.get_rect()
    backGround=pygame.Surface((screen.get_size()))
    backgroundRect=backGround.get_rect()
    backGround.fill((97,191,71))
    backGround=backGround.convert()
    backGroundc=backGround.copy()
    screen.blit(backGround,(0,0))
    carSurface=pygame.Surface((30,30))
    carSurface.set_colorkey((0,0,0))
    carImg=pygame.image.load("car.png")
    carImg=carImg.convert_alpha()
    carRect=carImg.get_rect()

    dx=0
    dy=0



    drawLevel =  ["xxxxxxxxxxxxxxxxxxxxxxxx......",
                  "x...a..................x......",
                  "x..b1c..x........x..e..x......",
                  "x...d...x........x.f2g.x......",
                  "x.....xxxxxx.....x..h..x......",
                  "x..xxxx..........xxxxx.x......",
                  "x....i.....x...........x......",
                  "x...j3k....xxxxxxx.....x......",
                  "x....l.....x...x....m..x......",
                  "x..............xxx.n4o.x......",
                  "x..xxxxxx........x..p..x......",
                  "x........q....x..x.....x......",
                  "x.......r5s...x..x.....x......",
                  "x........t....x........x......",
                  "xxxxxxxxxxxxxxxwxxxxxxxx......"]

    def drawblock(figure):
        
        if figure=="wall":
            wall=pygame.image.load("wall.png")
            wall.convert_alpha()
            return wall
        elif figure=="grass":
            grass=pygame.image.load("grass.png")
            grass.convert_alpha()
            return grass
        elif figure=="lidl":
            lidl=pygame.image.load("lidl.png")
            lidl.convert_alpha()
            return lidl
        elif figure=="asda":
            asda=pygame.image.load("asda.png")
            asda.convert_alpha()
            return asda
        elif figure=="tesco":
            tesco=pygame.image.load("tesco.png")
            tesco.convert_alpha()
            return tesco
        elif figure=="sainsburys":
            sainsburys=pygame.image.load("sainsburys.png")
            sainsburys.convert_alpha()
            return sainsburys
        elif figure=="mns":
            mns=pygame.image.load("mns.png")
            mns.convert_alpha()
            return mns
        elif figure=="apple":
            apple=pygame.image.load("apple.png")
            apple.convert_alpha()
            return apple
        elif figure=="cheese":
            cheese=pygame.image.load("cheese.png")
            cheese.convert_alpha()
            return cheese
        elif figure=="jam":
            jam=pygame.image.load("jam.png")
            jam.convert_alpha()
            return jam
        elif figure=="milk":
            milk=pygame.image.load("milk.png")
            milk.convert_alpha()
            return milk



    def renderring(mapLevel):

        lines=len(mapLevel)
        columns=len(mapLevel[0])

        length=screenRect.width/columns
        height=screenRect.height/lines
        wallb=drawblock("wall")
        grassb=drawblock("grass")
        asdab=drawblock("asda")
        sainsburysb=drawblock("sainsburys")
        tescob=drawblock("tesco")
        lidlb=drawblock("lidl")
        mnsb=drawblock("mns")
        milkb=drawblock("milk")
        appleb=drawblock("apple")
        jamb=drawblock("jam")
        cheeseb=drawblock("cheese")

        backGround=backGroundc.copy()
        
        for y in range(lines):
            for x in range(columns):
                
                if mapLevel[y][x] == "x":
                    backGround.blit(wallb, (length * x, height * y))
                elif mapLevel[y][x] == "a":
                    backGround.blit(appleb, (length * x, height * y))
                elif mapLevel[y][x] == "e":
                    backGround.blit(appleb, (length * x, height * y))
                elif mapLevel[y][x] == "i":
                    backGround.blit(appleb, (length*x, height * y))
                elif mapLevel[y][x] == "m":
                    backGround.blit(appleb,  (length * x, height * y))
                elif mapLevel[y][x] == "q":
                    backGround.blit(appleb,  (length * x, height * y))
                elif mapLevel[y][x] == "b":
                    backGround.blit(milkb,  (length * x, height * y))
                elif mapLevel[y][x] == "f":
                    backGround.blit(milkb,  (length * x, height * y))
                elif mapLevel[y][x] == "j":
                    backGround.blit(milkb,  (length * x, height * y))
                elif mapLevel[y][x] == "n":
                    backGround.blit(milkb,  (length * x, height * y))
                elif mapLevel[y][x] == "r":
                    backGround.blit(milkb, (length * x, height * y))
                elif mapLevel[y][x] == "c":
                    backGround.blit(cheeseb, (length * x, height * y))
                elif mapLevel[y][x] == "g":
                    backGround.blit(cheeseb, (length * x, height * y))
                elif mapLevel[y][x] == "k":
                    backGround.blit(cheeseb, (length*x, height * y))
                elif mapLevel[y][x] == "o":
                    backGround.blit(cheeseb,  (length * x, height * y))
                elif mapLevel[y][x] == "s":
                    backGround.blit(cheeseb,  (length * x, height * y))
                elif mapLevel[y][x] == "d":
                    backGround.blit(jamb,  (length * x, height * y))
                elif mapLevel[y][x] == "h":
                    backGround.blit(jamb,  (length * x, height * y))
                elif mapLevel[y][x] == "l":
                    backGround.blit(jamb,  (length * x, height * y))
                elif mapLevel[y][x] == "p":
                    backGround.blit(jamb,  (length * x, height * y))
                elif mapLevel[y][x] == "t":
                    backGround.blit(jamb,  (length * x, height * y))
                elif mapLevel[y][x] == "1":
                    backGround.blit(tescob,  (length * x, height * y))
                elif mapLevel[y][x] == "2":
                    backGround.blit(sainsburysb,  (length * x, height * y))
                elif mapLevel[y][x] == "3":
                    backGround.blit(asdab,  (length * x, height * y))
                elif mapLevel[y][x] == "4":
                    backGround.blit(mnsb,  (length * x, height * y))
                elif mapLevel[y][x] == "5":
                    backGround.blit(lidlb,  (length * x, height * y))
                elif mapLevel[y][x] == ".":
                    backGround.blit(grassb,  (length * x, height * y))
                elif mapLevel[y][x] == ".":
                    backGround.blit(grassb,  (length * x, height * y))
                elif mapLevel[y][x] == "w":
                    carx = length * x
                    cary = height * y

                    backGround.blit(carImg,  (length * x, height * y))
                    
        screen.blit(backGroundc, (0,0))

        return length, height, carx, cary , lines, columns, backGround

    length, height, carx, cary , lines, columns, backGround = renderring(drawLevel)


    clock=pygame.time.Clock()
    mainloop=True
    FPS=60


    while mainloop:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False

        pygame.display.set_caption("Evolution Bargain Finder Robot!")
        screen.blit(backGround,(0,0))
        pygame.display.flip()


if __name__=="__main__":
    evolution()
























