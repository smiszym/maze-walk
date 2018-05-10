def ascii_printer(maze):
    return "".join("".join("xx" if maze.get_wall(x, y) else "  "
                  for x in range(maze.width)) + "\n"
                  for y in range(maze.height))
