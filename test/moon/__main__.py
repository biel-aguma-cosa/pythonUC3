import pygame, numpy as np
from scipy.constants import G

pygame.init()

clock = pygame.time.Clock()
tps = 0.1
dt = 1/tps

compact = 1000
def km(n):
    global compact
    return n * compact
def un_km(n):
    global compact
    return n / compact

class screen:
    w = 1200
    h = 800
    surface = pygame.display.set_mode((w,h))

class moon:
    pos = np.array([600,0],dtype=np.float64)
    spd = np.array([0,3683],dtype=np.float64)
    w = 7.3*10**22
    r = 1740
class earth:
    pos = np.array([0,0],dtype=np.float64)
    spd = np.array([0,0],dtype=np.float64)
    w = 5.972*10**24
    r = 6380

V = moon.pos-earth.pos
D = np.linalg.norm(V)
F = G*earth.w*moon.w/D if D else np.float64(0)

C = np.array([600,400],dtype=np.float64)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.surface.fill('black')
    
    V = moon.pos-earth.pos
    D = np.linalg.norm(V)
    F = G*earth.w*moon.w/D if D else np.float64(0)

    print(V, D, F)

    moon .spd += (F*V/np.pow(D,2))/dt
    earth.spd += (F*V/np.pow(D,2))/dt

    moon .pos += moon .spd
    earth.pos += earth.spd

    print(un_km(earth.pos),un_km(moon.pos))
    pygame.draw.circle(screen.surface,'blue' ,C,un_km(earth.r))
    pygame.draw.circle(screen.surface,'white',un_km(moon.pos)-un_km(earth.r)+C,un_km(moon.r))

    pygame.display.flip()
    dt = clock.tick(60)/1000

print(G)
