import numpy as np

def relu(x):
    if x > 0:
        return

#
#
#
#
#

ray_num = 7
angle = np.deg2rad(90)

center = (0,0)

direction = np.array([(np.cos(angle/ray_num-angle/2), np.sin(angle/ray_num-angle/2)) for i in range(ray_num)])
rays = np.array([center for i in range(ray_num)])


for i in range(ray_num):
    rays += direction

# ray.direction = direction + angle*ray