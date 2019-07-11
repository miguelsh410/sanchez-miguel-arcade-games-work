import arcade

screen_width = 800
screen_height = 800


def small_cloud(a, b, c):
    """This function draws a cloud with four circles."""
    arcade.draw_circle_filled(100 + a, 700 + b, 40 + c, arcade.color.WHITE)
    arcade.draw_circle_filled(70 + a, 740 + b, 40 + c, arcade.color.WHITE)
    arcade.draw_circle_filled(120 + a, 745 + b, 40 + c, arcade.color.WHITE)
    arcade.draw_circle_filled(150 + a, 720 + b, 40 + c, arcade.color.WHITE)


def big_cloud(a, b, c):
    """This function draws a cloud with six circles."""
    arcade.draw_circle_filled(100 + a, 700 + b, 40 + c, arcade.color.WHITE)
    arcade.draw_circle_filled(70 + a, 740 + b, 40 + c, arcade.color.WHITE)
    arcade.draw_circle_filled(120 + a, 745 + b, 40 + c, arcade.color.WHITE)
    arcade.draw_circle_filled(171 + a, 750 + b, 40 + c, arcade.color.WHITE)
    arcade.draw_circle_filled(170 + a, 700 + b, 40 + c, arcade.color.WHITE)
    arcade.draw_circle_filled(200 + a, 730 + b, 40 + c, arcade.color.WHITE)


def draw_clouds(a):
    """Draw a lot of clouds."""
    small_cloud(0 + a, 0, 0)
    small_cloud(200 + a, -150, -10)
    big_cloud(350 + a, 0, -3)
    small_cloud(600 + a, -90, 3)
    small_cloud(800 + a, 0, 0)
    small_cloud(1000 + a, -150, -10)
    big_cloud(1150 + a, 0, -3)
    small_cloud(1400 + a, -90, 3)
    small_cloud(-800 + a, 0, 0)
    small_cloud(-600 + a, -150, -10)
    big_cloud(-450 + a, 0, -3)
    small_cloud(-200 + a, -90, 3)


def panda_bear(a, b):
    """This function will draw a panda."""
    # Right ear
    arcade.draw_circle_filled(62 + a, 277 + b, 30, arcade.color.BLACK)

    # Left ear
    arcade.draw_circle_filled(-62 + a, 277 + b, 30, arcade.color.BLACK)

    # Body
    arcade.draw_ellipse_filled(0 + a, 85 + b, 85, 105, arcade.color.BLACK, 0)

    # Belly
    arcade.draw_ellipse_filled(0 + a, 85 + b, 60, 80, arcade.color.WHITE_SMOKE, 0)

    # Face
    arcade.draw_circle_filled(0 + a, 220 + b, 68, arcade.color.WHITE_SMOKE)

    # Left eye-shadow
    arcade.draw_ellipse_filled(-32 + a, 243 + b, 22, 13, arcade.color.BLACK, 30)

    # Right eye-shadow
    arcade.draw_ellipse_filled(32 + a, 243 + b, 22, 13, arcade.color.BLACK, 330)

    # Left eye
    arcade.draw_ellipse_filled(-26 + a, 246 + b, 9, 5, arcade.color.WHITE, 30)

    # Right eye
    arcade.draw_ellipse_filled(26 + a, 246 + b, 9, 5, arcade.color.WHITE, 330)

    # Nose
    arcade.draw_ellipse_filled(0 + a, 210 + b, 10, 5, arcade.color.BLACK, 0)
    arcade.draw_circle_filled(0 + a, 208 + b, 5, arcade.color.BLACK)

    # Mouth
    arcade.draw_line(0 + a, 213 + b, 0 + a, 193 + b, arcade.color.BLACK, 3)
    arcade.draw_arc_outline(-10 + a, 193 + b, 10, 4, arcade.color.BLACK, 180, 360, 3)
    arcade.draw_arc_outline(10 + a, 193 + b, 10, 4, arcade.color.BLACK, 180, 360, 3)

    # Left leg
    arcade.draw_ellipse_filled(-49 + a, 0 + b, 47, 33, arcade.color.BLACK, 120)

    # Right leg
    arcade.draw_ellipse_filled(47 + a, 0 + b, 47, 33, arcade.color.BLACK, 60)

    # Bamboo
    arcade.draw_rectangle_filled(-19 + a, 99 + b, 20, 183, arcade.color.APPLE_GREEN, 353)

    # Right arm
    arcade.draw_ellipse_filled(33 + a, 147 + b, 56, 23, arcade.color.BLACK, 325)

    # Left arm
    arcade.draw_ellipse_filled(-37 + a, 110 + b, 42, 25, arcade.color.BLACK, 325)


def on_draw(delta_time):
    """Draw everything."""
    arcade.start_render()

    # Grass
    arcade.draw_rectangle_filled(400, 0, 800, 600, arcade.color.BITTER_LIME, 0)

    # Clouds
    on_draw.clouds_x -= on_draw.delta_x * delta_time
    draw_clouds(on_draw.clouds_x)

    # Panda
    on_draw.panda_x += on_draw.delta_x * delta_time
    on_draw.panda_y += on_draw.delta_y * delta_time

    panda_bear(on_draw.panda_x, on_draw.panda_y)

    if on_draw.panda_x > 708 or on_draw.panda_x < 92:
        on_draw.delta_x *= -1
    if on_draw.panda_y > 180 or on_draw.panda_y < 180:
        on_draw.delta_y *= -1


on_draw.panda_x = 482
on_draw.panda_y = 180
on_draw.delta_x = 80
on_draw.delta_y = 40
on_draw.clouds_x = 0


def main():
    arcade.open_window(screen_width, screen_width, "Lab 2")
    arcade.set_background_color(arcade.color.BABY_BLUE_EYES)
    arcade.schedule(on_draw, 1/500)
    arcade.run()


main()
