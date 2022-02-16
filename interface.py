import pygame
class Interface:
    def __init__(self,mainGraph,VERSROW):
        pygame.init()
        self.o=0
        self.res = []
        self.screen = 0
        self.userInput = ""
        self.VERSROW = VERSROW
        self.fol = [0]*(VERSROW*VERSROW)
        self.WIDTH, self.HEIGHT = 600,600
        self.size = self.WIDTH/self.VERSROW
        self.WIN=None
        self.source,self.dest = -1,-1
        self.FPS = 60
        self.graph = mainGraph
        self.getReachableS = []
    def startWin(self,caption):
        self.WIN = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption(caption)
    
    def text_objects(self,text, font,color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def idxToCor(self,n,size):
        start = n * size
        row = int(start/self.WIDTH)
        col = start%self.WIDTH
        x = col
        y = row*size
        return (x,y)

    def addLine(self,s,d,w,color=(255,255,255)):
        sx,sy = self.idxToCor(s,self.size)
        dx,dy = self.idxToCor(d,self.size)
        smallText = pygame.font.Font("arial.ttf",15)
        textSurf, textRect = self.text_objects(str(w), smallText,(0,0,255))
        midx = ((sx+(self.size/1.6))+(dx+(self.size/2.6)))/2
        midy = ((sy+(self.size/2))+(dy+(self.size/2)))/2.5
        textRect.center = (midx, midy)
        self.WIN.blit(textSurf, textRect)
        pygame.draw.line(self.WIN,color,((sx+(self.size/1.6)), (sy+(self.size/2))),((dx+(self.size/2.6)), (dy+(self.size/2))),2)
        pygame.draw.circle(self.WIN,color,((dx+(self.size/2.6)), (dy+(self.size/2))),5)
    def perpWin(self,mouse,adj,res):
        self.startWin("Press 'h' for help")
        x,y = 0,0
        c=0
        for i in range(self.VERSROW):
            x=0
            for j in range(self.VERSROW):
                rect = pygame.Rect(x,y,self.size,self.size)
                if x+self.size > mouse[0][0] > x and y+self.size > mouse[0][1] >y:
                    pygame.draw.rect(self.WIN,(3, 127, 204),rect)
                    if(mouse[1][0]):
                        #print(o)
                        if self.o == 0:
                            self.fol[self.source] = 0
                            self.source = c
                            self.fol[self.source] = 1
                        else:
                            self.fol[self.dest] = 0
                            self.dest = c
                            self.fol[self.dest] = 1
                else:
                    if(self.fol[c]):
                        if(c == self.source):
                            pygame.draw.rect(self.WIN,(7, 117, 3),rect)
                        elif(c == self.dest):
                            pygame.draw.rect(self.WIN,(245, 85, 255),rect)
                        else:
                            pygame.draw.rect(self.WIN,(98, 122, 255),rect)
                    else:
                        if c in self.getReachableS:
                            pygame.draw.rect(self.WIN,(255,255,255),rect)
                        else:
                            pygame.draw.rect(self.WIN,(0,0,0),rect)
                smallText = pygame.font.Font("arial.ttf",20)
                textSurf, textRect = self.text_objects(str(c), smallText,(255,0,0))
                textRect.center = ((x+(self.size/2)), (y+(self.size/2)))
                self.WIN.blit(textSurf, textRect)
                c+=1
                x+=self.size
            y+=self.size

        for ver in list(adj.keys()):
            for v in adj[ver]:
                if(v.From() in res[:-1]):
                    idx = res.index(v.From())
                    if(v.To() == res[idx+1]):
                        self.addLine(v.From(),v.To(),v.W(),(0,255,0))
    def helpPage(self):
        self.startWin("Press 'b' to get back")
    def draw_window(self,mouse,g,res,screen):
        if screen == 0:
            self.perpWin(mouse,g,res)
        elif screen == 1:
            self.helpPage()
        pygame.display.update()
    def main(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            mouse = [pygame.mouse.get_pos(),pygame.mouse.get_pressed()]
            g = self.graph.getAdj()
            try:
                self.getReachableS = self.graph.BFS(self.source)
            except:
                pass
            self.draw_window(mouse,g,self.res,self.screen)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_c]:
                self.fol = [0]*(self.VERSROW*self.VERSROW)
                self.source = -1
                self.dest = -1
                self.o = 0
                self.res.clear()
                self.getReachableS.clear()
            elif keys[pygame.K_RETURN]:
                if(self.source != -1):
                    if self.o == 0:
                        self.o = 1
                    if self.o == 1:
                        if(self.dest != -1):
                            totalCost = -1
                            self.res = self.graph.getShortestPath(self.source,self.dest)
                            if not self.res == None:
                                totalCost = self.res[2]
                                self.res = self.res[0]
                            else:
                                self.res = []
                            #print(self.res)
                            print(totalCost)
            elif keys[pygame.K_h]:
                self.screen = 1
            elif keys[pygame.K_b]:
                self.screen = 0    
        pygame.quit()
