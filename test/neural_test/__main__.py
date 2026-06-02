import numpy as np, pygame, time, threading

WIDTH, HEIGHT = 600,400

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

running = True

t0 = 0
dt = 0

dots = np.array([])
it = 0

def raying():
    global dots, it
    ray_num = 7
    fov = np.deg2rad(90)
    center = (300,200)
    direction = np.array([(np.cos(fov/ray_num-fov/2), np.sin(fov/ray_num-fov/2)) for i in range(ray_num)])
    rays = np.array([np.array(center,np.float64) for i in range(ray_num)])
    while it < 30:
        rays += direction
        np.append(dots,rays)
        time.sleep(0.1)
        it += 0.1
threading.Thread(target=raying).start()

#try:
while running:
    mouse = np.array(pygame.mouse.get_pos())-(300,200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('grey')

    pygame.draw.circle(screen,'black',(300,200),5,1)


    n = np.linalg.norm(mouse)

    n2= np.acos(mouse[0]/n)/np.pi
    print(n2)

    print(dots)
    for dot in tuple(dots):
        pygame.draw.circle(screen,'red',dot,2)

    pygame.draw.line(screen,'orange',(300,200),((mouse[0]*32/n)+300,(mouse[1]*32/n)+200),3)

    pygame.display.flip()
    dt = clock.tick(30)/1000
    t0 += dt
#except:
#    it = 80