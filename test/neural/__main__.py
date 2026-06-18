import numpy as np, pygame, time, threading, random

WIDTH, HEIGHT = 600,400

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

running = True

t0 = 0
dt = 0

GRID0 = np.array([[0 for i in range(20)] for i in range(30)])

for i in range(30):
    GRID0[ i][ 0] = 1
    GRID0[ i][19] = 1
for i in range(20):
    GRID0[ 0][ i] = 1
    GRID0[29][ i] = 1

def reset(walls=30):
    global GRID, center
    x, y = 0, 0
    GRID = GRID0.copy()
    for i in range(walls):
        GRID[random.randint(0,29),random.randint(0,19)] = 1
    GRID[random.randint(0,29),random.randint(0,19)] = 5
    while GRID[x,y] != 0:
        x = random.randint(0,29)
        y = random.randint(0,19)
    center = np.array((x*20+10,y*20+10))
reset()

rays = []
fov  = np.deg2rad(97)
ray_num = 360
rays = np.array([np.array(center,np.float64) for i in range(ray_num)])
angle = 0

shader = np.array(pygame.PixelArray(pygame.Surface([WIDTH,HEIGHT])))[:,:]+1
print(shader.shape)
def distance(point,line,pixels):
    dx = rays[:,0] - center[0]
    dy = rays[:,1] - center[1]
    cx = rays[:,0] * center[1]
    cy = rays[:,1] * center[0]
    px = pixels[..., 0, np.newaxis]
    py = pixels[..., 1, np.newaxis]
    
    top = np.abs(dy*px-dx*py+cx-cy)

    bottom = np.sqrt(np.pow(dy,2)+np.pow(dx,2))

    result = top/bottom
eh = shader[:,:,np.newaxis]*(255,255,255)
print(shader.shape)

while running:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('grey')

    angle += -np.deg2rad((key[pygame.K_RIGHT] - key[pygame.K_LEFT])*5)

    input_mov = np.array((key[pygame.K_d] - key[pygame.K_a],key[pygame.K_s] - key[pygame.K_w]))
    input_mov = input_mov*4/(np.linalg.norm(input_mov)) if np.linalg.norm(input_mov) != 0 else input_mov*0

    theta = np.atan2(input_mov[0],input_mov[1])

    px = -(input_mov[0] * np.cos(-angle) - input_mov[1] * np.sin(-angle))
    py = -(input_mov[0] * np.sin(-angle) + input_mov[1] * np.cos(-angle))

    next_pos = center[0]+int(px),center[1]+int(px)
    if GRID[next_pos[0]//20,center[1]//20] == 0:
        center[0] += int(px)
    elif GRID[next_pos[0]//20,center[1]//20] == 5:
        reset()
        #reward 
    else:
        center[0] -= int(px)
        #punish

    if GRID[center[0]//20,next_pos[1]//20] == 0:
        center[1] += int(py)
    elif GRID[next_pos[0]//20,center[1]//20] == 5:
        reset()
        #reward 
    else:
        center[1] -= int(py)
        # punish

    direction = np.array([(np.cos((-angle+i*(fov/ray_num))+fov/2), np.sin((-angle+i*(fov/ray_num))+fov/2)) for i in range(ray_num)])
    rays /= (rays+0.00000000000001)
    rays *= center
    for i in range(400):
        clean = GRID[np.int64(rays[:,0]//20),np.int64(rays[:,1]//20)] == 0
        if i % 20 == 0:
            for ray in tuple(rays):
                #print((ray//20)*20)
                if GRID[int(ray[0]//20)][int(ray[1]//20)] == 1:
                    pygame.draw.rect(screen,'red',((ray[0]//20)*20,(ray[1]//20)*20,19,19))
                elif GRID[int(ray[0]//20)][int(ray[1]//20)] == 5:
                    #reward
                    pygame.draw.rect(screen,'blue',((ray[0]//20)*20,(ray[1]//20)*20,19,19))
                else:
                    pygame.draw.rect(screen,'green',((ray[0]//20)*20,(ray[1]//20)*20,19,19))
        rays[clean] += direction[clean]*1
    hit   = GRID[np.int64(rays[:,0]//20),np.int64(rays[:,1]//20)] == 1
    result = np.zeros(ray_num)
    result[ hit] = 1 - np.linalg.norm(rays[hit] - center, axis=1)/400
    #print(GRID[np.int64(rays[:,0]//20),np.int64(rays[:,1]//20)])
    #print(result)
    #pygame.draw.lines(screen,'red',True,rays.copy())
    #pygame.draw.polygon(screen,'red',rays,)
    #for ray in tuple(rays.copy()):
    #    pygame.draw.line(screen,'red',center,ray)
    pygame.draw.line(screen,'red',center,rays[0])
    pygame.draw.line(screen,'red',center,rays[len(rays)-1])
    #pygame.draw.line(screen,'blue',center,((mouse[0]*32/(n+0.00000000000001))+center[0],(mouse[1]*32/n+0.0000000000000001)+center[1]),1)
    pygame.draw.circle(screen,'black',center,5,1)

    pygame.display.flip()
    bop = []
    pygame.surfarray.blit_array(screen,shader)
    dt = clock.tick(30)/1000
    t0 += dt
running = False