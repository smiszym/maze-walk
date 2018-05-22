from collections import deque
import random


def random_generator(maze):
    random.seed()
    for y in range(maze.height):
        for x in range(maze.width):
            if bool(random.getrandbits(1)):
                maze.set_wall((x, y))


def bfs_generator(maze):
    # Pre-generate all possible walls; the unnecessary we'll be destroyed later
    for y in range(maze.height):
        for x in range(maze.width):
            if x % 2 == 0 or y % 2 == 0:
                maze.set_wall((x, y))

    random.seed()
    visited = deque()
    to_be_visited = deque()

    # Start in the middle of the maze
    visited.append((maze.width // 4, maze.height // 4))
    to_be_visited.append((maze.width // 4 - 1, maze.height // 4))
    to_be_visited.append((maze.width // 4 + 1, maze.height // 4))
    to_be_visited.append((maze.width // 4, maze.height // 4 - 1))
    to_be_visited.append((maze.width // 4, maze.height // 4 + 1))

    random.shuffle(to_be_visited)

    def direction(dir, from_where):
        if dir == 'n':
            return from_where[0], from_where[1] - 1
        elif dir == 's':
            return from_where[0], from_where[1] + 1
        elif dir == 'w':
            return from_where[0] - 1, from_where[1]
        elif dir == 'e':
            return from_where[0] + 1, from_where[1]
        else:
            raise KeyError("Unknown direction: " + repr(dir))

    def cell_position(cell):
        return cell[0] * 2 + 1, cell[1] * 2 + 1

    def inside_maze(cell):
        return 0 <= cell[0] < maze.width//2 and 0 <= cell[1] < maze.height//2

    def wall_between(cell1, cell2):
        a = cell_position(cell1)
        b = cell_position(cell2)
        return (a[0]+b[0])//2, (a[1]+b[1])//2

    while True:
        try:
            where_to_go = to_be_visited.popleft()
        except IndexError:
            break # all cells visited
        choices = ['n', 's', 'w', 'e']
        random.shuffle(choices)
        for choice in choices:
            from_where = direction(choice, where_to_go)
            if from_where in visited:
                assert inside_maze(from_where)
                maze.set_wall(wall_between(where_to_go, from_where), False)
                visited.append(where_to_go)
                inner_choices = ['n', 's', 'w', 'e']
                random.shuffle(inner_choices)
                for dir in inner_choices:
                    candidate = direction(dir, where_to_go)
                    if inside_maze(candidate) \
                            and candidate not in visited \
                            and candidate not in to_be_visited:
                        to_be_visited.append(candidate)
                break


def horiz_generator(maze):
    random.seed()

    # Pre-generate all possible horizontal walls, with holes in them
    for y in range(maze.height):
        maze.set_wall((0, y))
        maze.set_wall((maze.width-1, y))

        hole_position = random.randint(1, maze.width-1)
        for x in range(maze.width):
            if y % 2 == 0 and (x != hole_position or y == 0):
                maze.set_wall((x, y))
