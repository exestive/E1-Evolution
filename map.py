import pygame, sys, copy, random, time, string, math, os, pdb
from pygame.locals import *

global MHA,MHAC,robotImg,RC,robotRect,HF


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
    robotSurface=pygame.Surface((30,30))
    robotSurface.set_colorkey((0,0,0))
    robotImg=pygame.image.load("robot.png")
    robotImg=robotImg.convert_alpha()
    potentialCells=set()


    global MHA,HF,closeList,openList#,cor_x,cor_y
    
    #cor_x=450
    #cor_y=420
    dx=0
    dy=0
    

    

    drawLevel =  ["xxxxxxxxxxxxxxxxxxxxxxxx......",
                  "x...a..................x......",
                  "x..b1c..x........x..e..x......",
                  "x...d...x........x.f2g.x......",
                  "x.....xxxxxx.....x..h..x......",
                  "x..xxxx....w.....xxxxx.x......",
                  "x....i.....x...........x......",
                  "x...j3k....xxxxxxx.....x......",
                  "x....l.....x...x....m..x......",
                  "x..............xxx.n4o.x......",
                  "x..xxxxxx........x..p..x......",
                  "x........q....x..x.....x......",
                  "x.......r5s...x..x.....x......",
                  "x........t....x........x......",
                  "xxxxxxxxxxxxxxxxxxxxxxxx......"]


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
        global robotRect,ar,br,cr,dr,er,fr,gr,hr,ir,jr,kr,lr,mr,nr,oor,pr,qr,rr,sr,tr,HF
        MHAC=0
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
                    ar=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb, ar)                    
                elif mapLevel[y][x] == "e":
                    er=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb, er)
                elif mapLevel[y][x] == "i":
                    ir=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb, ir)
                elif mapLevel[y][x] == "m":
                    mr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb,  mr)
                elif mapLevel[y][x] == "q":
                    qr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb, qr)
                elif mapLevel[y][x] == "b":
                    br=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb, br)
                elif mapLevel[y][x] == "f":
                    fr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb,  fr)
                elif mapLevel[y][x] == "j":
                    jr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb, jr)
                elif mapLevel[y][x] == "n":
                    nr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb,  nr)
                elif mapLevel[y][x] == "r":
                    rr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb,rr)
                elif mapLevel[y][x] == "c":
                    cr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb, cr)
                elif mapLevel[y][x] == "g":
                    gr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb, gr)
                elif mapLevel[y][x] == "k":
                    kr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb,kr)
                elif mapLevel[y][x] == "o":
                    oor=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb, oor)
                elif mapLevel[y][x] == "s":
                    sr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb, sr)
                elif mapLevel[y][x] == "d":
                    dr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb,dr)
                elif mapLevel[y][x] == "h":
                    hr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb, hr)
                elif mapLevel[y][x] == "l":
                    lr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb, lr)
                elif mapLevel[y][x] == "p":
                    pr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb, pr)
                elif mapLevel[y][x] == "t":
                    tr=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(grassb,  (length * x, height * y))
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
                elif mapLevel[y][x] == "w":
                    robotx = length * x
                    roboty = height * y
                    robotImgR=pygame.transform.rotate(robotImg, 0)
                    robotRect=pygame.Rect((x * length, y * height, 30, 30))
                    backGround.blit(robotImg,robotRect)
                    
                   
        def marketHarvestActivator():
                
            length=screenRect.width/columns
            height=screenRect.height/lines                        
            a=random.randrange(1,50)
            b=random.randrange(1,50)
            c=random.randrange(1,50)
            d=random.randrange(1,50)
            harvest=['apple']*a+['jam']*b+['milk']*c+['cheese']*d
            i=random.randrange (1,5)
            v=random.choice(harvest)
            selection=[i,v]
            if i==1:
                if v=='apple':
                    backGround.blit(appleb, (length *4 , height * 1))
                    pos=(int(length) *4 , int(height * 1))
                if v=='cheese':
                    backGround.blit(cheeseb, (length * 5, height * 2))
                    pos=(int(length * 5), int(height * 2))
                if v=='milk':
                    backGround.blit(milkb,  (length * 3, height * 2))
                    pos=(int(length) * 3, int(height * 2))
                if v=='jam':
                    backGround.blit(jamb, (length * 4, height * 3))
                    pos=(int(length) * 4, int(height * 3))
            if i==2:
                if v=='apple':
                    backGround.blit(appleb, (length * 20, height * 2))
                    pos=(int(length * 20),int(height * 2))
                if v=='cheese':
                    backGround.blit(cheeseb, (length * 21, height * 3))
                    pos=(int(length * 21), int(height * 3))
                if v=='milk':
                    backGround.blit(milkb,  (length * 19, height * 3))
                    pos=(int(length) * 19, int(height * 3))
                if v=='jam':
                    backGround.blit(jamb, (length * 20, height * 4))
                    pos=(int(length * 20), int(height * 4))
            if i==3:
                if v=='apple':
                    backGround.blit(appleb, (length * 5, height * 6))
                    pos=(int(length * 5),int(height * 6))
                if v=='cheese':
                    backGround.blit(cheeseb, (length * 6, height * 7))
                    pos=(int(length * 6), int(height * 7))
                if v=='milk':
                    backGround.blit(milkb,  (length * 4, height * 7))
                    pos=(int(length * 4), int(height * 7))
                if v=='jam':
                    backGround.blit(jamb, (length * 5, height * 8))
                    pos=(int(length * 5), int(height * 8))
            if i==4:
                if v=='apple':
                    backGround.blit(appleb, (length * 20, height * 8))
                    pos=(int(length * 20), int(height * 8))
                if v=='cheese':
                    backGround.blit(cheeseb, (length * 21, height * 9))
                    pos=(int(length * 21), int(height * 9))
                if v=='milk':
                    backGround.blit(milkb,  (length * 19, height * 9))
                    pos=(int(length * 19), int(height * 9))
                if v=='jam':
                    backGround.blit(jamb, (length * 20, height * 10))
                    pos=(int(length * 20), int(height * 10))
            if i==5:
                if v=='apple':
                    backGround.blit(appleb, (length * 9, height * 11))
                    pos=(int(length * 9), int(height * 11))
                if v=='cheese':
                    backGround.blit(cheeseb, (length * 10, height * 12))
                    pos=(int(length * 10), int(height * 12))
                if v=='milk':
                    backGround.blit(milkb,  (length * 8, height * 12))
                    pos=(int(length * 8), int(height * 12))
                if v=='jam':
                    backGround.blit(jamb, (length * 9, height * 13))
                    pos=(int(length * 9), int(height * 13))
                backGround.blit(robotImg,robotRect)
            return pos
        #marketHarvestActivator()
        
        return length, height, robotx, roboty , lines, columns, backGround, marketHarvestActivator()

    
    length, height, robotx, roboty , lines, columns, backGround, MHA = renderring(drawLevel)
    
        

    clock=pygame.time.Clock()
    mainloop=True
    FPS=1
    

    """


    _1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _3=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _4=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _5=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _6=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _7=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _8=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _9=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _10=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _11=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _12=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _13=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _14=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
    _15=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']

    Map=[_1,_2,_3,_4,_5,_6,_7,_8,_9,_10,_11,_12,_13,_14,_15]
    
    """

    def pathFinding(xPoint, yPoint):
    
        #openList=set()
        #closeList=set()
        #node={'F':'000','G':'000','H':'000','A':'0','P':'Y0'}

        def locator(xLoc,yLoc):
            
            if xLoc<=0 or yLoc<=0 or xLoc>751 or yLoc>481:
                pass
            
            elif xLoc%30<15 or xLoc%30>0:
                pass
                
            elif xLoc%30>=15 or xLoc%30<=29:
                xLoc-=15
                
            if yLoc%30<15 or yLoc%30>0:
                pass
                
            elif yLoc%30>=15 or yLoc%30<=29:
                yLoc-=15
                
            #print('xlll'+str(xLoc))
            xLoc=xLoc/30
            #print('xlll'+str(xLoc))
            xLoc=round(xLoc,0)
            #print('xlll'+str(xLoc))
            yLoc=yLoc/30
            yLoc=round(yLoc,0)
            xLoc,yLoc=int(xLoc),int(yLoc)
            str1=chr(65+xLoc)
            #print('aval'+ str(ord(str1)))
            str2=str(yLoc)
            container=''.join(str1+str2)
            #closeList.add(container)
            return container
            
            

        
        def neighborAdder(cell_l,cell):
            
            conversion=set()
            
            row=[]
            col=[]
            
            if len(cell_l)>2:
                CL1=cell_l[1]
                CL2=cell_l[2]
                CL=''.join(CL1+CL2)
                CL=int(CL)
            else:
                CL=cell_l[1]
            """
            if (int(ord(cell_l[0])-65))%2==0:
                cell_l[0]=chr(ord(cell_l[0])-1)
                
                print('cell '+cell_l[0])
            else:
                cell_l[0]=chr(ord(cell_l[0])-1)
                CL=int(CL)-1
            print(int(ord(cell_l[0])-65)%2)
            """
    
            if (ord(cell_l[0])-1)<=64:
                
                pass
            else:
                row.append(chr(ord(cell_l[0])-1))
                
            if (ord(cell_l[0]))<=64 or (ord(cell_l[0]))>89:
                pass
            else:
                row.append(cell_l[0])
            if (ord(cell_l[0])+1)>89:
                
                pass
            else:
                
                row.append(chr(ord(cell_l[0])+1))


            CL=int(CL)
            if CL-1<1:
                
                pass
            else:
                
                col.append(CL-1)
    

            if CL<=1 or CL>=14:
                pass
            else:
                
                col.append(CL)
            if (CL+1)>=14:
                
                pass

            else:
                
                col.append(CL+1)
            
            


            for i in row:
                for j in col:
 
                    str1=i
                    str2=j
                    #print(i,j)
                    
                    JJ=ord(cell_l[0])
                    KK=ord(str1)

                    x=''.join(str1+str(str2))

                    #print((int(str2)-1),str1)
                    

                    #if len(cell_l)>2:
                    #    pass
                    #else:
                    #    CL=cell_l[1]
                    #print('dovom:'+ str((ord(cell_l[0]))))
                    #N=drawLevel[4][(ord('N')-65)]
                    #print('ssds    '+str(str2) +  '  SAS    ' + str(ord(str1)-65))
                    if int(str2)>14 or ord(str1)-65>89:
                        M='x'
                    else:
                        M=str(drawLevel[int(str2)][(ord(str1)-65)])
                    
                    #print(2)
                    #print(i,j)
                    #print(M)
                    
                    if x==cell or M=='x' or M=='1' or M=='2' or M=='3' or M=='4' or M=='5':
                        #print('hello')
                        if x==cell:
                            
                            globals()[cell]={'F':0,'G':0,'P':0,'H':0,'D':0}

                            #print(globals()[cell])
                    else:
                        
                        if  KK==JJ and int(str2)< int(CL):      
                            globals()[x]= {'F':0,'G':0,'H':0,'D':'','P':'%s' %cell}
                            globals()[x]['D']='N'


                            conversion.add(x)
                        elif KK==JJ and int(str2)> int(CL):
                            globals()[x]= {'F':0,'G':0,'H':0,'D':'','P':'%s' %cell}
                            globals()[x]['D']='S'


                            conversion.add(x)
                        elif KK>JJ and int(str2)== int(CL):
                            globals()[x]= {'F':0,'G':0,'H':0,'D':'','P':'%s' %cell}
                            globals()[x]['D']='E'

                            conversion.add(x)
                        elif  KK<JJ and int(str2)== int(CL):       
                            globals()[x]= {'F':0,'G':0,'H':0,'D':'','P':'%s' %cell}
                            globals()[x]['D']='W'

                            conversion.add(x)
                        elif KK>JJ and int(str2)< int(CL):
                            globals()[x]= {'F':0,'G':0,'H':0,'D':'','P':'%s' %cell}
                            globals()[x]['D']='NE'


                            conversion.add(x)
                        elif KK<JJ and int(str2)< int(CL):
                            globals()[x]= {'F':0,'G':0,'H':0,'D':'','P':'%s' %cell}
                            globals()[x]['D']='NW'


                            conversion.add(x)
                        elif  KK>JJ and int(str2)> int(CL):       
                            globals()[x]= {'F':0,'G':0,'H':0,'D':'','P':'%s' %cell}
                            globals()[x]['D']='SE'


                            conversion.add(x)
                        elif KK<JJ and int(str2)> int(CL): 
                            globals()[x]= {'F':0,'G':0,'H':0,'D':'','P':'%s' %cell}
                            globals()[x]['D']='SW'
    
                        
                            conversion.add(x)
                            
                        else:
                            pass#print('bye')
                        
                        #print(globals()[x])

            #print(conversion)
            
            return conversion
        
        #print(xPoint,yPoint)
        #print(robotRect)
        #robotRect.x=cor_x
        #robotRect.y=cor_y    
        splt=locator(xPoint,yPoint)
        #print(splt)
        x=neighborAdder(list(splt),splt)

        #print('splt'+splt)
        for i in x:
            #print(i)
            potentialCells.add(i)
        
        
        
        return potentialCells,splt

    

    pathFinding(robotRect.x, robotRect.y)
    closeList=set()
    openList=set()
    
    def fghCalculator(lst2,source,goal):
        drawLevel[5][4]
        #print(lst2)
        #print(lst2,source,goal)
        closeList.add(source)
        #print(closeList)
        RCX=robotRect.x
        RCY=robotRect.y
        def heuristic(x1,x2,y1,y2):
            HF= math.sqrt((int(x1) - int(x2)) * (int(x1) - int(x2)) + (int(y1) - int(y2)) * (int(y1) - int(y2)))
            return HF
        def nameDecomp(string):
            #print(string)
            string1=list(string)
            string1=string[0].split()
            first=(ord(string1[0])-65)*30
                        
            if len(string)>2:
                st1=string[1]
                st2=string[2]
                st=''.join(st1+st2)
                st=int(st)
                second=st*30
            else:
                second=string[1]*30
            ret=(first,second)
            return ret
        def Gcalculator(G):
            #print(G)
            R=globals()[G]['G']+42
            #print(int(globals()[G]['G']+42))
            return R

        for i in range(len(lst2)):
            robotRect.x=RCX
            robotRect.y=RCY
            x=nameDecomp(lst2[i])
            globals()[lst2[i]]['H']= int(round(heuristic(x[0],goal[0],x[1],goal[1]),0))
            globals()[lst2[i]]['G']= int(round(Gcalculator(globals()[lst2[i]]['P']),0))
            globals()[lst2[i]]['F']= int(globals()[lst2[i]]['G'] + globals()[lst2[i]]['H'])
            #print(lst2[i])
        OL=tuple(openList)
        for i in range(len(lst2)):
            if globals()[lst2[i]] not in OL:
                openList.add(lst2[i])
            else:
                openLis.update(lst2[i])
            
        Ffinder=set()
        chk=tuple(openList)
        #chkL=list(openList)
        for x in range(len(chk)):
            b=int(round(globals()[chk[x]]['F'],0))
            Ffinder.add(b)
        z=list(Ffinder)
        #print(z)
        o=z.index(min(z))
        #print(z)
        for n in chk:
            #print('hello')
             v=chk[o]
             v=list(v)
             #print(v)
             v1=(ord(v[0])-65)*30
             
             if len(v)>2:
                 st1=v[1]
                 st2=v[2]
                 st=''.join(st1+st2)
                 st=int(st)
                 v2=st*30             
             else:
                 v2=v[1]*30
             fin=(v1,v2)
             if globals()[chk[o]]!=fin:
                #print(openList)
                #print(drawLevel)
                if globals()[chk[o]]['D']=='N':


                    robotRect.y-=30
 

                       
                elif globals()[chk[o]]['D']=='S':

                    robotRect.y+=30


                        
                elif globals()[chk[o]]['D']=='E':
 
                    robotRect.x+=30
 

                        
                elif globals()[chk[o]]['D']=='W':

                    robotRect.x-=30


                       
                elif globals()[chk[o]]['D']=='NE':

                    robotRect.x+=30
                    robotRect.y-=30


                elif globals()[chk[o]]['D']=='NW':

                    robotRect.x-=30
                    robotRect.y-=30
                    renderring(drawLevel)  

                    #print(globals()[lst2[i]])
                        
                elif globals()[chk[o]]['D']=='SE':

                    robotRect.x+=30
                    robotRect.y+=30
                      
                    
                        
                elif globals()[chk[o]]['D']=='SW':
                       
                #renderring(drawLevel)
                
                    robotRect.x-=30
                    robotRect.y+=30
                    #evolution()
                    #print(globals()[lst2[i]])
             else:  
                print('Finish')
                
        openList.remove(chk[o])
        closeList.add(chk[o])    
        #print(robotRect)
        #print(closeList)
        #print(openList)

        #print(len(lst2),counter)
        print(robotRect)
        pathFinding(robotRect.x,robotRect.y)
        return robotRect
            
        
              

    
    
    potCells,src=pathFinding(robotRect.x, robotRect.y)
    MHAC=0
    list2=tuple(potCells)
    #print(list2[1])
    clock = pygame.time.Clock()
    hrv,drawLevel1=pathFinding(MHA[0],MHA[1])
    while mainloop:
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame window closed by user
                mainloop = False
        
            """
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False 
                if event.key == pygame.K_UP:
                    dy -= 1 
                if event.key == pygame.K_DOWN:
                    dy += 1
                if event.key == pygame.K_RIGHT:
                    dx += 1
                if event.key == pygame.K_LEFT:
                    dx -= 1
        pygame.display.set_caption("[FPS]: %.2f dx: %i dy %i press cursor keys to move ball" % (clock.get_fps(), dx, dy))
        screen.blit(background, (0,0)) # delete all
        # ---------find out probing point of ball surface
        if dx > 0:
            pointx = ballx + ballrect.width
        else:
            pointx = ballx
        if dy > 0:
            pointy = bally + ballrect.height
        else:
            pointy = bally
        # ------- find out if ball want to leave screen
        if pointx + dx < 0:
            ballx = 0
            pointx = 0
            dx = 0
        elif pointx + dx > screenrect.width:
            ballx = screenrect.width - ballrect.width
            pointx = screenrect.width - ballrect.width
            dx = 0
        if pointy + dy < 0:
            bally = 0
            pointy = 0
            dy = 0
        elif pointy + dy > screenrect.height:
            bally = screenrect.height - ballrect.height
            pointy = screenrect.height - ballrect.height
            dy = 0
        # ------- find out if probing point is inside wall
        # make sure proing point does not produce out of index error
        y1 = int(pointy/height)
        y1 = max(0,y1) # be never smaller than 0
        y1 = min(y1,lines-1) # be never bigger than lines
        x1 = int((pointx + dx)/length)
        x1 = max(0,x1) # be never smaller than 0
        x1 = min(x1,columns-1) 
        y2 = int((pointy+dy)/height)
        y2 = max(0,y2)
        y2 = min(y2,lines-1)
        # -------------- check the type of tile where the ball is ------
        if my_maze[y1][x1] == "x":
            dx = 0
        else:
            ballx += dx
        if my_maze[y2][x1] == "x":
            dy = 0
        else:
            bally += dy
        # ---------------move ball surface
        screen.blit(ballsurface, (ballx, bally))

    
        """
        
        ch=random.randrange(1,10000)
        if ch==10 or ch==100 or ch==500 or ch==1000:
            length, height, robotx, roboty , lines, columns, backGround, MHA = renderring(drawLevel)
            print(MHA)
            pass
            if MHA==MHAC:
                pass
            else:
                fghCalculator(list2,src,MHA)
                MHAC=MHA
        """
        if robotRect.x==cor_x and robotRect.y==cor_y:
            cor_x=robotRect.x
            cor_y=robotRect.y
            pathFinding(robotRect.x,robotRect.y)
            print('hi')
            print(MHA[0],MHA[1])
        else:
            print(robotRect.x,robotRect.y)
            print(cor_x,cor_y)
            print('bye')
        """
        pygame.display.set_caption("Evolution Bargain Finder Robot!")
        screen.blit(backGround,(0,0))
        #clock.tick(20)
        pygame.display.flip()

    return renderring(drawLevel),drawLevel
if __name__=="__main__":
    evolution()

    























