import random


def random_generator(maze):
    random.seed()
    for y in range(maze.height):
        for x in range(maze.width):
            if bool(random.getrandbits(1)):
                maze.set_wall(x, y)
