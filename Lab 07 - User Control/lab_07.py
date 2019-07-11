import arcade
""" Lab 7 - User Control """

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
MOVEMENT_SPEED = 5


def small_cloud(a, b, c, z):
    """This function draws a cloud with four circles."""
    arcade.draw_circle_filled(100 + a, 700 + b, 40 + c, z)
    arcade.draw_circle_filled(70 + a, 740 + b, 40 + c, z)
    arcade.draw_circle_filled(120 + a, 745 + b, 40 + c, z)
    arcade.draw_circle_filled(150 + a, 720 + b, 40 + c, z)


def big_cloud(a, b, c, z):
    """This function draws a cloud with six circles."""
    arcade.draw_circle_filled(100 + a, 700 + b, 40 + c, z)
    arcade.draw_circle_filled(70 + a, 740 + b, 40 + c, z)
    arcade.draw_circle_filled(120 + a, 745 + b, 40 + c, z)
    arcade.draw_circle_filled(171 + a, 750 + b, 40 + c, z)
    arcade.draw_circle_filled(170 + a, 700 + b, 40 + c, z)
    arcade.draw_circle_filled(200 + a, 730 + b, 40 + c, z)


class NormalTree:
    def __init__(self, position_x, position_y, color_1, color_2):

        self.position_x = position_x
        self.position_y = position_y
        self.color_1 = color_1
        self.color_2 = color_2

    def draw(self):

        # Draw trunk.
        arcade.draw_rectangle_filled(-60 + self.position_x, -160 + self.position_y, 60, 160, self.color_1)

        # Draw leaves
        arcade.draw_circle_filled(-110 + self.position_x, -60 + self.position_y, 35, self.color_2)
        arcade.draw_circle_filled(-60 + self.position_x, -85 + self.position_y, 35, self.color_2)
        arcade.draw_circle_filled(-10 + self.position_x, -60 + self.position_y, 35, self.color_2)
        arcade.draw_circle_filled(15 + self.position_x, -10 + self.position_y, 35, self.color_2)
        arcade.draw_circle_filled(-135 + self.position_x, -10 + self.position_y, 35, self.color_2)
        arcade.draw_circle_filled(-160 + self.position_x, 40 + self.position_y, 35, self.color_2)
        arcade.draw_circle_filled(40 + self.position_x, 40 + self.position_y, 35, self.color_2)
        arcade.draw_circle_filled(-135 + self.position_x, 65 + self.position_y, 35, self.color_2)
        arcade.draw_circle_filled(-100 + self.position_x, 90 + self.position_y, 35, self.color_2)
        arcade.draw_circle_filled(-60 + self.position_x, 110 + self.position_y, 35, self.color_2)
        arcade.draw_circle_filled(-35 + self.position_x, 90 + self.position_y, 35, self.color_2)
        arcade.draw_circle_filled(0 + self.position_x, 70 + self.position_y, 35, self.color_2)
        arcade.draw_circle_filled(-60 + self.position_x, 15 + self.position_y, 75, self.color_2)


class DrawClouds:
    """Draw a lot of clouds."""
    def __init__(self, position_x, change_x, color):

        self.position_x = position_x
        self.change_x = change_x
        self.cloud_color = color

    def draw(self):
        small_cloud(0 + self.position_x, 0, 0, self.cloud_color)
        small_cloud(200 + self.position_x, -150, -10, self.cloud_color)
        big_cloud(350 + self.position_x, 0, -3, self.cloud_color)
        small_cloud(600 + self.position_x, -90, 3, self.cloud_color)
        small_cloud(-800 + self.position_x, 0, 0, self.cloud_color)
        small_cloud(-600 + self.position_x, -150, -10, self.cloud_color)
        big_cloud(-450 + self.position_x, 0, -3, self.cloud_color)
        small_cloud(-200 + self.position_x, -90, 3, self.cloud_color)
        small_cloud(800 + self.position_x, 0, 0, self.cloud_color)
        small_cloud(1000 + self.position_x, -150, -10, self.cloud_color)
        big_cloud(1150 + self.position_x, 0, -3, self.cloud_color)
        small_cloud(1400 + self.position_x, -90, 3, self.cloud_color)

    def update(self):
        self.position_x += self.change_x
        if self.position_x > 800:
            self.position_x = 0
        elif self.position_x < -800:
            self.position_x = 0


class PandaBear:
    def __init__(self, position_x, position_y, change_x, change_y, color):

        self.hurt_sound = arcade.load_sound("hurt5.ogg")

        # Position, change, and color of panda.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def draw(self):
        # Right ear
        arcade.draw_circle_filled(62 + self.position_x, 277 + self.position_y, 30, self.color)

        # Left ear
        arcade.draw_circle_filled(-62 + self.position_x, 277 + self.position_y, 30, self.color)

        # Body
        arcade.draw_ellipse_filled(0 + self.position_x, 85 + self.position_y, 85, 105, self.color, 0)

        # Belly
        arcade.draw_ellipse_filled(0 + self.position_x, 85 + self.position_y, 60, 80, arcade.color.WHITE_SMOKE, 0)

        # Face
        arcade.draw_circle_filled(0 + self.position_x, 220 + self.position_y, 68, arcade.color.WHITE_SMOKE)

        # Left eye-shadow
        arcade.draw_ellipse_filled(-32 + self.position_x, 243 + self.position_y, 22, 13, self.color, 30)

        # Right eye-shadow
        arcade.draw_ellipse_filled(32 + self.position_x, 243 + self.position_y, 22, 13, self.color, 330)

        # Left eye
        arcade.draw_ellipse_filled(-26 + self.position_x, 246 + self.position_y, 9, 5, arcade.color.WHITE, 30)

        # Right eye
        arcade.draw_ellipse_filled(26 + self.position_x, 246 + self.position_y, 9, 5, arcade.color.WHITE, 330)

        # Nose
        arcade.draw_ellipse_filled(0 + self.position_x, 210 + self.position_y, 10, 5, self.color, 0)
        arcade.draw_circle_filled(0 + self.position_x, 208 + self.position_y, 5, self.color)

        # Mouth
        arcade.draw_line(0 + self.position_x, 213 + self.position_y, 0 + self.position_x, 193 + self.position_y,
                         self.color, 3)
        arcade.draw_arc_outline(-10 + self.position_x, 193 + self.position_y, 10, 4, self.color, 180, 360, 3)
        arcade.draw_arc_outline(10 + self.position_x, 193 + self.position_y, 10, 4, self.color, 180, 360, 3)

        # Left leg
        arcade.draw_ellipse_filled(-49 + self.position_x, 0 + self.position_y, 47, 33, self.color, 120)

        # Right leg
        arcade.draw_ellipse_filled(47 + self.position_x, 0 + self.position_y, 47, 33, self.color, 60)

        # Right arm
        arcade.draw_ellipse_filled(33 + self.position_x, 147 + self.position_y, 56, 23, self.color, 325)

        # Left arm
        arcade.draw_ellipse_filled(-37 + self.position_x, 110 + self.position_y, 42, 25, self.color, 325)

    def update(self):

        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x > SCREEN_WIDTH - 92:
            self.position_x = SCREEN_WIDTH - 92
            arcade.play_sound(self.hurt_sound)
        elif self.position_x < 92:
            self.position_x = 92
            arcade.play_sound(self.hurt_sound)

        if self.position_y < 44:
            self.position_y = 44
            arcade.play_sound(self.hurt_sound)
        elif self.position_y > 493:
            self.position_y = 493
            arcade.play_sound(self.hurt_sound)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.upgrade_sound = arcade.load_sound("upgrade1.ogg")

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.DARK_KHAKI)

        # Create a panda
        self.black_panda = PandaBear(100, 120, 0, 0, arcade.color.BLACK)

        # Moving clouds
        self.moving_clouds = DrawClouds(0, 0, arcade.color.WHITE)

        # Tree
        self.panda_tree = NormalTree(0, 0, arcade.color.BROWN, arcade.color.GREEN_YELLOW)

    def on_draw(self):
        arcade.start_render()

        # Grass
        arcade.draw_rectangle_filled(400, 0, 800, 600, arcade.color.BITTER_LIME, 0)

        # Clouds
        self.moving_clouds.draw()

        # Panda
        self.black_panda.draw()

        # Tree
        self.panda_tree.draw()

    def update(self, delta_time):
        self.black_panda.update()

        self.moving_clouds.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.black_panda.change_x = -MOVEMENT_SPEED
            self.moving_clouds.change_x = MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.black_panda.change_x = MOVEMENT_SPEED
            self.moving_clouds.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.black_panda.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.black_panda.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.black_panda.change_x = 0
            self.moving_clouds.change_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.black_panda.change_y = 0
            self.moving_clouds.change_x = 0

    def on_mouse_motion(self, x, y, dx, dy):
        self.panda_tree.position_x = x
        self.panda_tree.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):

        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.upgrade_sound)
            self.panda_tree.color_1 = arcade.color.DARK_BROWN
            self.panda_tree.color_2 = arcade.color.ORANGE_RED
            self.moving_clouds.cloud_color = arcade.color.GRAY_BLUE
            arcade.set_background_color(arcade.color.BLACK_BEAN)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.upgrade_sound)
            self.panda_tree.color_1 = arcade.color.BROWN
            self.panda_tree.color_2 = arcade.color.GREEN_YELLOW
            self.moving_clouds.cloud_color = arcade.color.WHITE
            arcade.set_background_color(arcade.color.DARK_KHAKI)


def main():
    window = MyGame()
    arcade.run()


main()
