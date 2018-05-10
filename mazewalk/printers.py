def ascii_printer(maze):
    return "".join("".join("xx" if maze.get_wall(x, y) else "  "
                  for x in range(maze.width)) + "\n"
                  for y in range(maze.height))


def utf8_printer(maze):
    def character_for(x, y):
        if not maze.get_wall(x, y):
            return "  "
        else:
            has_north = maze.get_wall(x, y-1)
            has_south = maze.get_wall(x, y+1)
            has_west  = maze.get_wall(x-1, y)
            has_east  = maze.get_wall(x+1, y)
            if has_north and has_south and has_west and has_east:
                return "┼─"
            elif has_north and has_south and has_west:
                return "┤ "
            elif has_north and has_south and has_east:
                return "├─"
            elif has_west and has_east and has_north:
                return "┴─"
            elif has_west and has_east and has_south:
                return "┬─"
            elif has_west and has_north:
                return "╯ "
            elif has_west and has_south:
                return "╮ "
            elif has_east and has_north:
                return "╰─"
            elif has_east and has_south:
                return "╭─"
            elif has_north and has_south:
                return "│ "
            elif has_west and has_east:
                return "──"
            elif has_west:
                return "┤ "
            elif has_east:
                return "├─"
            elif has_north:
                return "┴ "
            elif has_south:
                return "┬ "
            elif not (has_north or has_south or has_west or has_east):
                return "▬▬"
            else:
                return "??"
    return "".join("".join(character_for(x, y)
                           for x in range(maze.width)) + "\n"
                           for y in range(maze.height))
