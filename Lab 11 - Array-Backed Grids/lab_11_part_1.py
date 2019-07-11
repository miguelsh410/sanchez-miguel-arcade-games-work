import arcade

WIDTH = 45
HEIGHT = 45
MARGIN = 6

ROW_COUNT = 15
COLUMN_COUNT = 15

SCREEN_WIDTH = COLUMN_COUNT * (WIDTH + MARGIN) + MARGIN
SCREEN_HEIGHT = ROW_COUNT * (HEIGHT + MARGIN) + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.grid = []

        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        for row in range(COLUMN_COUNT):
            for column in range(ROW_COUNT):
                color = arcade.color.BLACK

                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN

                arcade.draw_rectangle_filled((WIDTH / 2) + column * (WIDTH + MARGIN) + MARGIN,
                                             (HEIGHT / 2) + row * (HEIGHT + MARGIN) + MARGIN, WIDTH, HEIGHT,
                                             color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        row = y // (HEIGHT + MARGIN)
        column = x // (WIDTH + MARGIN)

        print(column, row)

        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

        if row < ROW_COUNT - 1:
            if self.grid[row + 1][column] == 0:
                self.grid[row + 1][column] = 1
            else:
                self.grid[row + 1][column] = 0

        if column < COLUMN_COUNT - 1:
            if self.grid[row][column + 1] == 0:
                self.grid[row][column + 1] = 1
            else:
                self.grid[row][column + 1] = 0

        if row > 0:
            if self.grid[row - 1][column] == 0:
                self.grid[row - 1][column] = 1
            else:
                self.grid[row - 1][column] = 0

        if column > 0:
            if self.grid[row][column - 1] == 0:
                self.grid[row][column - 1] = 1
            else:
                self.grid[row][column - 1] = 0


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
