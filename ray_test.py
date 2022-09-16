import pybullet as p
import pybullet_data
import numpy as np
import os
import time
import random


def point_test(check_point, ray_len):

    count_x = 0
    p_list_0 = [
        [check_point[0] + ray_len, check_point[1],           check_point[2]          ],
        [check_point[0] - ray_len, check_point[1],           check_point[2]          ],
        [check_point[0]          , check_point[1] + ray_len, check_point[2]          ],
        [check_point[0]          , check_point[1] - ray_len, check_point[2]          ],
        [check_point[0]          , check_point[1],           check_point[2] + ray_len],
        [check_point[0]          , check_point[1],           check_point[2] - ray_len]
    ]

    p_list_1 = [check_point] * 6

    for i in range(6):
        inside = p.rayTest(p_list_0[i], p_list_1[i])
        # p.addUserDebugLine(p_list_1[i], p_list_0[i], [1,0,0])
        # time.sleep(0.5)
        # print(inside[0][-2])
        if inside[0][-2] != (0.0,0.0,0.0):
            count_x += 1

    if count_x == 6:
        return 1  # inside
    else:
        return 0  # outside

def inside_data_sampling(n):
    inside_data = []
    while True:
        point = [random.random()-0.5, random.random()-0.5, random.random()]
        if point_test(point, 1)==1:
            # print(point)
            inside_data.append(point)

        if len(inside_data) == n:
            np.savetxt("data/pcloud01.csv", inside_data)
            break
    

if __name__ == "__main__":

    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    plane = p.loadURDF("plane.urdf")

    startPos = [0,0,1]
    startOrientation = p.getQuaternionFromEuler([0,0,0])
    boxId = p.loadURDF("r2d2.urdf",startPos, startOrientation)

    p.setGravity(0, 0, -9.8)
    p.addUserDebugLine([0.5,0.5,0], [0.5,0.5,1], [1,0,0])
    p.addUserDebugLine([0.5,-0.5,0], [0.5,-0.5,1], [1,0,0])
    p.addUserDebugLine([-0.5,-0.5,0], [-0.5,-0.5,1], [1,0,0])
    p.addUserDebugLine([-0.5,0.5,0], [-0.5,0.5,1], [1,0,0])
    for _ in range(1000):
        p.stepSimulation()

    inside_data_sampling(1000)
    # print(point_test([0,0,0.3], 1))


    
    