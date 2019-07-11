import arcade
arcade.open_window(800, 800, "Lab 2")
arcade.set_background_color(arcade.color.BABY_BLUE_EYES)
arcade.start_render()


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


# Clouds
small_cloud(0, 0, 0)
small_cloud(200, -150, -10)
big_cloud(350, 0, -3)
small_cloud(600, -90, 3)

# Grass
arcade.draw_rectangle_filled(400, 0, 800, 600, arcade.color.BITTER_LIME, 0)

# Right ear
arcade.draw_circle_filled(544, 457, 30, arcade.color.BLACK)

# Left ear
arcade.draw_circle_filled(420, 457, 30, arcade.color.BLACK)

# Body
arcade.draw_ellipse_filled(482, 265, 85, 105, arcade.color.BLACK, 0)

# Belly
arcade.draw_ellipse_filled(482, 265, 60, 80, arcade.color.WHITE_SMOKE, 0)

# Face
arcade.draw_circle_filled(482, 400, 68, arcade.color.WHITE_SMOKE)

# Left eye-shadow
arcade.draw_ellipse_filled(450, 423, 22, 13, arcade.color.BLACK, 30)

# Right eye-shadow
arcade.draw_ellipse_filled(514, 423, 22, 13, arcade.color.BLACK, 330)

# Left eye
arcade.draw_ellipse_filled(456, 426, 9, 5, arcade.color.WHITE, 30)

# Right eye
arcade.draw_ellipse_filled(508, 426, 9, 5, arcade.color.WHITE, 330)

# Nose
arcade.draw_ellipse_filled(482, 390, 10, 5, arcade.color.BLACK, 0)
arcade.draw_circle_filled(482, 388, 5, arcade.color.BLACK)

# Mouth
arcade.draw_line(482, 393, 482, 373, arcade.color.BLACK, 3)
arcade.draw_arc_outline(472, 373, 10, 4, arcade.color.BLACK, 180, 360, 3)
arcade.draw_arc_outline(492, 373, 10, 4, arcade.color.BLACK, 180, 360, 3)

# Left leg
arcade.draw_ellipse_filled(433, 180, 47, 33, arcade.color.BLACK, 120)

# Right leg
arcade.draw_ellipse_filled(529, 180, 47, 33, arcade.color.BLACK, 60)

# Bamboo
arcade.draw_rectangle_filled(463, 279, 20, 183, arcade.color.APPLE_GREEN, 353)

# Right arm
arcade.draw_ellipse_filled(515, 327, 56, 23, arcade.color.BLACK, 325)

# Left arm
arcade.draw_ellipse_filled(445, 290, 42, 25, arcade.color.BLACK, 325)

arcade.finish_render()
arcade.run()
