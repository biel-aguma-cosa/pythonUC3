import pygame, numpy as np
from scipy.constants import G

pygame.init()

clock = pygame.time.Clock()
tps = 60
dt = 1/tps

def km(n):
    return n * 2000
def un_km(n):
    return n / 2000

class screen:
    w = 1200
    h = 800
    surface = pygame.display.set_mode((w,h))

class moon:
    pos = np.array([385600,100],dtype=np.float64)
    spd = np.array([3683,0],dtype=np.float64)
    w = 7.3*10**22
    r = 1.740
class earth:
    pos = np.array([600,400],dtype=np.float64)
    spd = np.array([0,0],dtype=np.float64)
    w = 5.972*10**24
    r = 6.380

V = moon.pos-earth.pos
D = np.linalg.norm(V)
F = G*earth.r*moon.r/D if D else 0

moon .spd += F*V/D
earth.spd += F*V/D

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.surface.fill('black')
    
    pygame.draw.circle(screen.surface,'blue',earth.pos,100)
    pygame.draw.circle(screen.surface,'white',moon.pos,10)

    pygame.display.flip()
    clock.tick(tps)

print(G)
