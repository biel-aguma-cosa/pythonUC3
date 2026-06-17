import torch, pygame, time, threading, random

WIDTH, HEIGHT = 600,400

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

running = True

t0 = 0
dt = 0

if torch.cuda.is_available():
    print("--- cuda")
    torch.device("cuda")
else:
    print("--- cpu")
    torch.device("cpu")

GRID0 = torch.zeros((30,30))

GRID0[ :][ 0] = 1
GRID0[ :][19] = 1
GRID0[ 0][ :] = 1
GRID0[29][ :] = 1

def reset(walls=30):
    global GRID, center
    x, y = 0, 0
    GRID = torch.alias_copy(GRID0)
    for i in range(walls):
        GRID[random.randint(0,29),random.randint(0,19)] = 1
    GRID[random.randint(0,29),random.randint(0,19)] = 5
    while GRID[x,y] != 0:
        x = random.randint(0,29)
        y = random.randint(0,19)
    center = torch.tensor((x*20+10,y*20+10))
reset()

fov  = torch.deg2rad(torch.tensor(97))
ray_num = 7
rays = torch.ones([ray_num,2])[:]*center
angle = 0


while running:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('grey')

    angle += -torch.deg2rad(torch.tensor((key[pygame.K_RIGHT] - key[pygame.K_LEFT])*5))

    input_mov = torch.tensor((key[pygame.K_d] - key[pygame.K_a],key[pygame.K_s] - key[pygame.K_w])).type(torch.float64)
    input_mov = input_mov*4/(torch.norm(input_mov)) if torch.norm(input_mov) != 0 else input_mov*0

    theta = torch.atan2(input_mov[0],input_mov[1])

    px = -(input_mov[0] * torch.cos(-angle) - input_mov[1] * torch.sin(-angle))
    py = -(input_mov[0] * torch.sin(-angle) + input_mov[1] * torch.cos(-angle))

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

    direction = torch.tensor([(torch.cos((-angle+i*(fov/ray_num))+fov/2), torch.sin((-angle+i*(fov/ray_num))+fov/2)) for i in range(ray_num)])
    rays[:] = torch.where(rays!=0,rays/rays,1)
    rays[:] = rays*center
    for i in range(400):
        print(GRID.shape)
        clean = GRID[(rays[:,0]//20).type(torch.int64),(rays[:,1]//20).type(torch.int64)] == 0
        if i % 20 == 0:
            for ray in tuple(rays[:]):
                if GRID[int(ray[0]//20)][int(ray[1]//20)] == 1:
                    pygame.draw.rect(screen,'red',(int(ray[0]//20)*20,int(ray[0]//20)*20,19,19))
                elif GRID[int(ray[0]//20)][int(ray[1]//20)] == 5:
                    #reward
                    pygame.draw.rect(screen,'blue',(int(ray[0]//20)*20,int(ray[0]//20)*20,19,19))
                else:
                    pygame.draw.rect(screen,'green',(int(ray[0]//20)*20,int(ray[0]//20)*20,19,19))
        rays[clean] += direction[clean]*1
    hit   = GRID[(rays[:,0]//20).type(torch.int64),(rays[:,1]//20).type(torch.int64)] == 1
    result = torch.zeros(ray_num)
    result[hit] = 1 - torch.linalg.norm(rays[hit] - center, axis=1)/400

    for ray in tuple(torch.alias_copy(rays)):
        pygame.draw.line(screen,'red',tuple(center.type(int)),tuple(ray.type(int)))
    #pygame.draw.line(screen,'blue',center,((mouse[0]*32/(n+0.00000000000001))+center[0],(mouse[1]*32/n+0.0000000000000001)+center[1]),1)
    pygame.draw.circle(screen,'black',tuple(center.type(int)),5,1)

    pygame.display.flip()
    dt = clock.tick(30)/1000
    t0 += dt
running = False