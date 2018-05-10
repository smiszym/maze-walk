from . import printers

class Maze:
    def __init__(self, width: int, height: int,
                 generator_func=None,
                 printer_func=printers.ascii_printer):
        """
        Creates a maze with the specified dimensions. Both dimensions
        must be odd integers. generator_func is used to generate walls
        in the maze; if none is specified, a maze with no walls is created.
        """

        if not isinstance(width, int) or not isinstance(height, int):
            raise ValueError("Maze dimensions must be integers")

        if width < 3 or height < 3:
            raise ValueError("Maze dimensions must be at least 3x3")

        if width % 2 != 1 or height % 2 != 1:
            raise ValueError("Maze dimensions must be odd integers")

        self._width = width
        self._height = height
        self._walls = [[False for x in range(width)] for y in range(height)]
        self._printer_func = printer_func

        # Generate the walls
        if generator_func is not None:
            generator_func(self)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def get_wall(self, x, y):
        if x < 0 or y < 0 or x >= self._width or y >= self._height:
            return False
        return self._walls[y][x]

    def set_wall(self, x, y, is_present=True):
        self._walls[y][x] = is_present

    def __str__(self):
        return self._printer_func(self)
