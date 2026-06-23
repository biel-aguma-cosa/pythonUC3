import pygame, numpy as np

class Raycast():
    def __init__(self):
        self.grid = np.zeros((600,400),np.float64)
        self.origin = np.array((300,200),np.float64)
        self.ray_count = 60
        self.iterations = 300
        self.angle = np.deg2rad(-45)
        self.fov = np.deg2rad(90)

        self.ray_index = np.arange(self.ray_count)

        self.rays = np.ones((self.ray_count,2),np.float64)
        self.direction = np.zeros((self.ray_count,2),np.float64)

        self.center = np.array([300,200])
        
    def run(self,parent):
        self.rays = np.ones((self.ray_count,2),np.float64)*self.center
        for i in range(self.iterations):
            self.direction[self.ray_index,0] = np.cos((self.ray_index-(self.ray_count-1)/2)*(self.fov/(self.ray_count-1))+self.angle)
            self.direction[self.ray_index,1] = np.sin((self.ray_index-(self.ray_count-1)/2)*(self.fov/(self.ray_count-1))+self.angle)
            x = np.clip(np.int64(self.rays[:,0]),0,self.grid.shape[0]-1)
            y = np.clip(np.int64(self.rays[:,1]),0,self.grid.shape[1]-1)
            clean = self.grid[x,y] == 0
            self.rays[clean] += self.direction[clean]
        distances = 1-np.linalg.norm(self.rays-self.center,axis=1)/self.iterations
        pass
        return [self.center, self.rays, distances]

class Game():
    WIDTH = 600
    HEIGHT = 400
    def __init__(self):

        #main
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        #raycast
        self.raycast = Raycast()

        self.main()
    def main(self):
        self.rects = []
        while self.running:
            key = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill('black')


            input_mov = np.array((key[pygame.K_s] - key[pygame.K_w],key[pygame.K_d] - key[pygame.K_a]))
            input_mov = input_mov*4/(np.linalg.norm(input_mov)) if np.linalg.norm(input_mov) != 0 else input_mov*0
            theta = np.atan2(input_mov[0],input_mov[1])
            px = -(input_mov[0] * np.cos(self.raycast.angle) - input_mov[1] * np.sin(self.raycast.angle))
            py = -(input_mov[0] * np.sin(self.raycast.angle) + input_mov[1] * np.cos(self.raycast.angle))
            self.raycast.center += np.int64(np.array((px,py)))
            self.raycast.angle += np.deg2rad(30) * (key[pygame.K_RIGHT]-key[pygame.K_LEFT]) * self.dt

            raycast = self.raycast.run(self)
            print(raycast)
            if 0 <= mouse[0] < 590 and 0 <= mouse[1] < 390:
                self.rects.append((mouse[0],mouse[1],10,10))
                self.raycast.grid[mouse[0]:mouse[0]+10,mouse[1]:mouse[1]+10] = 1

            # DRAW RECTS HERE

            print(np.rad2deg(self.raycast.angle))

            for line in tuple(raycast[1]):
                pygame.draw.line(self.screen,'red',raycast[0],line)

            pygame.display.flip()
            self.dt = self.clock.tick(60)/1000

Game()