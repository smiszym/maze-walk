class Maze:
    def __init__(self, width: int, height: int, generator_func=None):
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

        # Generate the walls
        if generator_func is not None:
            generator_func(self)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
