import map_graph
import mapping
import movement
import object_detection
import numpy as np
import car_utils
import time

final_goal = (200, 250)
PATH_STEPS = 5

while 1:
    intermediate_goal = car_utils.find_closest_square(final_goal, 101)
    
    
    print(intermediate_goal)
    start = (50, 0)

    us_map = mapping.create_mapping()
    graph = map_graph.MapGraph(us_map)
    path = graph.a_star(start, intermediate_goal)
    
    directions, relative_dir, relative_dist = car_utils.path_to_directions(path, min(PATH_STEPS, len(path)))
    for i in directions:
        print(i)
        if (i == "RIGHT"):
            movement.turn_right()
            time.sleep(.05)
            movement.forward()
        if (i == "LEFT"):
            movement.turn_left()
            time.sleep(.05)
            movement.forward()
        if (i == "UP"):
            movement.forward()
        if (i == "DOWN"):
            movement.backward()

    final_goal = (final_goal[0] - relative_dir, final_goal[1] - relative_dist)

    if (relative_dir % 4 == 1):
        final_goal = (-final_goal[1], final_goal[0])
    elif(relative_dir % 4 == 2):
        final_goal = (-final_goal[0], final_goal[1])
    elif(relative_dir % 4 == 3):
        final_goal = (final_goal[1], -final_goal[0])
    
    print(final_goal)
    time.sleep(.05)
    input()
    if (intermediate_goal == final_goal):
        print("At destination...")
        break
        
""" Object Detection
object_detection.run('/home/peka/Labs/Lab1/models/efficientdet_lite0.tflite', 0, 640, 480, 4, False)
"""

