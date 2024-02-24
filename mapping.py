import numpy as np
import matplotlib.pyplot as plt
import picar_4wd as fc
import time
import math

import car_utils

from bresenham import bresenham

ANGLE_RANGE = 180
STEP = 5
INTERPOLATION_THRESHOLD = 25

def create_mapping():
    arr = np.zeros((101, 101))
    coordinates = set({})

    prev = ()
    for angle in range(0, ANGLE_RANGE + 1, STEP):
        dist = fc.get_distance_at(angle - 90)
        if dist != -2:
            x = (int)(math.cos(math.radians(angle)) * dist)
            y = (int)(math.sin(math.radians(angle)) * dist)
            curr = (x + 50, y)
            
            if (curr[0] < np.size(arr, 0) and curr[1] < np.size(arr, 1) and curr[0] > 0 and curr[1] > 0):
                arr[curr] = 1
                coordinates.add(curr)
                if (angle > 0 and prev != () and car_utils.euclidean(curr, prev) <= INTERPOLATION_THRESHOLD):
                    point_between = set(bresenham(curr[0], curr[1], prev[0], prev[1])).difference(coordinates)
                    for x in point_between:
                        arr[x] = 1
                        coordinates.add(x)
                    prev = ()
                elif(prev != () and car_utils.euclidean(curr, prev) > INTERPOLATION_THRESHOLD):
                    prev = ()
                prev = curr
            time.sleep(.01)
    fc.servo.set_angle(0)
            
    
    car_utils.plot_points(coordinates, "Ultrasonic Mapping", np.size(arr, 0) + 10, np.size(arr, 1) + 10, False)

    return arr