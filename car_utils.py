import matplotlib.pyplot as plt

def manhattan(a, b) -> int:
        # Manhattan distance on a square grid
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidean(a, b) -> int:
    return int(((a[0] - b[0])**2 + (a[1]-b[1])**2)**.5)

def plot_points(coords, title, xlim, ylim, line):
    if (line):
        plt.plot([x[0] for x in coords], [x[1] for x in coords], marker='o', linestyle='-', color='b')
    else:
        plt.scatter([x[0] for x in coords], [x[1] for x in coords])
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim([0, xlim])
    plt.ylim([0, ylim])
    plt.grid(True)
    plt.show()

def find_closest_square(x, size):
    """
    Find the closest square in a 100x100 grid to a point (px, py) located outside the grid.
    
    Args:
    - px: The x coordinate of the point.
    - py: The y coordinate of the point.
    
    Returns:
    A tuple (closest_x, closest_y) representing the grid coordinates of the closest square.
    """
    # Define the grid size
    grid_size = size  # Max index for a 0-indexed grid (coordinates range from 0 to 99)
    
    # Calculate the closest point on the grid's boundary
    # For a point to the left or right, clamp the x coordinate
    closest_x = min(max(x[0], 0), grid_size - 1)
    # For a point above or below, clamp the y coordinate
    closest_y = min(max(x[1], 0), grid_size - 1)
    
    # Return the coordinates of the closest square
    return (closest_x, closest_y)

def path_to_directions(path, num):
    directions = []
    turn = 0
    distance = 0
    for i in range(1, num):
        if (path[i][0] > path[i-1][0]):
            directions.append("RIGHT")
            path = [(-x[1], x[0]) for x in path]
            print("new path ", path)
            turn +=1
        elif(path[i][0] < path[i-1][0]):
            directions.append("LEFT")
            path = [(x[1], -x[0]) for x in path]
            turn -=1
        elif(path[i][1] > path[i-1][1]):
            directions.append("UP")
            distance+=1
        elif(path[i][1] < path[i-1][1]):
            directions.append("DOWN")
            distance-=1
    return (directions, turn, distance)