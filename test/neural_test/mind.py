import numpy as np

def relu(x):
    if x > 0:
        return

# up down left right | rotate_left rotate_right
# i1 h1 h1 o1
# i2 h2 h2 o2
# i3 h3 h3 o3
# i4 h4 h4 o4
# i5 h5 h5 o5
# i6       06
# i7
# i8

ray_num = 7
angle = np.deg2rad(90)

center = (0,0)

direction = np.array([(np.cos(angle/ray_num-angle/2), np.sin(angle/ray_num-angle/2)) for i in range(ray_num)])
rays = np.array([center for i in range(ray_num)])


for i in range(ray_num):
    rays += direction

# ray.direction = direction + angle*ray