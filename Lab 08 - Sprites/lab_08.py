import arcade
import random

scaling_player = 0.3
scaling_poop = 0.4
scaling_pizza = 0.2
screen_height = 700
screen_width = 800
pizza_count = 150
poop_count = 25


class Poop(arcade.Sprite):
    def update(self):
        self.center_y += 1
        self.center_x += -1

        if self.bottom > screen_height:
            self.center_y = random.randrange(screen_height + 1)
        if self.right < 0:
            self.center_x = random.randrange(screen_width + 1)


class Pizza(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_y += self.change_y
        self.center_x += self.change_x

        if self.bottom < 0:
            self.change_y *= -1
        elif self.top > screen_height:
            self.change_y *= -1
        if self.left < 0:
            self.change_x *= -1
        elif self.right > screen_width:
            self.change_x *= -1


class LabGame(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, "Lab 8")

        self.poop_list = None
        self.pizza_list = None
        self.player_list = None

        self.player_sprite = None
        self.score = 0

        self.pizza_coin_sound = arcade.load_sound("coin3.ogg")
        self.poop_hurt_sound = arcade.load_sound("hurt3.ogg")
        self.game_over_sound = arcade.load_sound("gameOver.ogg")

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ALMOND)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.poop_list = arcade.SpriteList()
        self.pizza_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("pumpkin.png", scaling_player)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        for i in range(pizza_count):
            pizza = Pizza("pizza.png", scaling_pizza)

            pizza.center_x = random.randrange(13, screen_width - 12)
            pizza.center_y = random.randrange(13, screen_height - 12)
            pizza.change_x = random.randrange(-3, 4)
            pizza.change_y = random.randrange(-3, 4)

            self.pizza_list.append(pizza)

        for i in range(poop_count):
            poop = Poop("poop.png", scaling_poop)

            poop.center_x = random.randrange(screen_width)
            poop.center_y = random.randrange(screen_height)

            self.poop_list.append(poop)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.pizza_list.draw()
        self.poop_list.draw()

        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)

        if len(self.pizza_list) == 0:
            arcade.draw_text("Game Over", 300, 350, arcade.color.BLACK, 40)

    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.pizza_list) != 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        if len(self.pizza_list) != 0:
            self.pizza_list.update()
            self.poop_list.update()
        else:
            self.set_mouse_visible(True)

        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.pizza_list)
        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.poop_list)

        for pizza in good_hit_list:
            pizza.kill()
            arcade.play_sound(self.pizza_coin_sound)
            self.score += 1

        for poop in bad_hit_list:
            poop.kill()
            arcade.play_sound(self.poop_hurt_sound)
            self.score -= 6


def main():
    window = LabGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
