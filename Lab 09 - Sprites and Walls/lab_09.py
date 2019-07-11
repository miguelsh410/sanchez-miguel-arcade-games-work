import arcade

screen_width = 800
screen_height = 700

player_scaling = 0.2
block_scaling = 0.4
barrier_scaling = 0.3875
pow_block_scaling = 0.4
coin_scaling = 0.1

viewport_margin = 68

movement_speed = 7


class BlockGame(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, "Scrolling screen")

        # Sound to be played if player collects the coin.
        self.coin_sound = arcade.load_sound("coin3.ogg")

        self.score = 0
        self.score_x = 5
        self.score_y = 5

        self.block_list = None
        self.player_list = None
        self.coin_list = None

        self.player_sprite = None

        self.physics_engine = None

        self.view_left = 0
        self.view_bottom = 0

    def setup(self):

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.view_left = 0
        self.view_bottom = 0

        self.player_list = arcade.SpriteList()
        self.block_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("mario.png", player_scaling)
        self.player_sprite.center_x = 98
        self.player_sprite.center_y = 98
        self.player_list.append(self.player_sprite)

        # mario.png is the sprite for the character.
        # coin.png is the sprite that the player should collect.
        # barrier.png, block.png, and pow_block.png are walls.

        """The next four loops are just boundaries so that the character
        does not escape from the game."""
        for h in range(36, 1300, 68):
            pow_block = arcade.Sprite("pow_block.png", pow_block_scaling)
            pow_block.center_y = 32
            if h % 2 == 0:
                pow_block.center_x = h
                self.block_list.append(pow_block)

        for h in range(32, 900, 64):
            pow_block = arcade.Sprite("pow_block.png", pow_block_scaling)
            pow_block.center_x = 35
            if h % 2 == 0:
                pow_block.center_y = h
                self.block_list.append(pow_block)

        for h in range(36, 1300, 68):
            pow_block = arcade.Sprite("pow_block.png", pow_block_scaling)
            pow_block.center_y = 868
            pow_block.center_x = h
            self.block_list.append(pow_block)

        for h in range(34, 900, 64):
            pow_block = arcade.Sprite("pow_block.png", pow_block_scaling)
            pow_block.center_x = 1326
            if h % 2 == 0:
                pow_block.center_y = h
                self.block_list.append(pow_block)

        """Loops for blocks and coins that are inside the boundaries."""
        for h in range(160, 800, 118):
            block = arcade.Sprite("block.png", block_scaling)
            coin = arcade.Sprite("coin.png", coin_scaling)
            if h % 2 == 0:
                block.center_x = h
                block.center_y = h
                coin.center_x = h
                coin.center_y = h + 55
                self.block_list.append(block)
                self.coin_list.append(coin)

        coordinate_list = [[220, 160],
                           [280, 160],
                           [460, 160],
                           [640, 160],
                           [700, 160],
                           [760, 160],
                           [940, 160],
                           [1000, 160],
                           [1180, 160],
                           [1240, 160]]

        for coordinate in coordinate_list:
            block = arcade.Sprite("block.png", block_scaling)
            coin = arcade.Sprite("coin.png", coin_scaling)
            barrier = arcade.Sprite("barrier.png", barrier_scaling)
            block.center_x = coordinate[0]
            block.center_y = coordinate[1]
            barrier.center_x = 400
            barrier.center_y = 160
            if coordinate[0] % 8 == 0:
                coin.center_x = coordinate[0]
                coin.center_y = coordinate[1] + 55
                self.coin_list.append(coin)
            self.block_list.append(block)
            self.block_list.append(barrier)

        for h in range(278, 1250, 51):
            block = arcade.Sprite("block.png", block_scaling)
            coin = arcade.Sprite("coin.png", coin_scaling)
            block.center_x = h
            block.center_y = 278
            coin.center_x = h
            coin.center_y = 333
            self.block_list.append(block)
            self.coin_list.append(coin)

        for h in range(120, 336, 60):
            block = arcade.Sprite("block.png", block_scaling)
            coin = arcade.Sprite("coin.png", coin_scaling)
            block.center_y = 396
            if h % 3 == 0:
                block.center_x = h
                self.block_list.append(block)
                if h % 16 == 0:
                    coin.center_x = h
                    coin.center_y = 451
                    self.coin_list.append(coin)

        individual_coin = arcade.Sprite("coin.png", coin_scaling)
        individual_coin.center_y = 396
        individual_coin.center_x = 348
        self.coin_list.append(individual_coin)

        for h in range(564, 1250, 50):
            block = arcade.Sprite("block.png", block_scaling)
            coin = arcade.Sprite("coin.png", coin_scaling)
            barrier = arcade.Sprite("barrier.png", barrier_scaling)
            block.center_y = 514
            if h % 7 == 0:
                block.center_x = h
                coin.center_x = h
                coin.center_y = 569
                self.block_list.append(block)
                self.coin_list.append(coin)
            elif h % 8 == 0:
                block.center_x = h
                self.block_list.append(block)
            if h != block.center_x and h % 4 == 0:
                barrier.center_x = h
                barrier.center_y = 514
                self.block_list.append(barrier)

        for h in range(830, 1300, 80):
            block = arcade.Sprite("block.png", block_scaling)
            block.center_y = 750
            block.center_x = h
            self.block_list.append(block)
        for h in range(130, 750, 80):
            barrier = arcade.Sprite("barrier.png", barrier_scaling)
            if h % 2 == 0 and h != 210:
                barrier.center_x = h
                barrier.center_y = 750
                self.block_list.append(barrier)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.block_list)

    def on_draw(self):
        arcade.start_render()
        self.block_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        output = "Score: " + str(self.score)
        arcade.draw_text(output, self.score_x, self.score_y, arcade.color.GREEN_YELLOW, 14)
        if len(self.coin_list) == 0:
            arcade.draw_text("Game Over", self.score_x + 240, self.score_y + 350, arcade.color.BABY_BLUE, 60)

    def update(self, delta_time):
        if len(self.coin_list) != 0:
            self.physics_engine.update()

        coins_hit = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coins_hit:
            coin.kill()
            arcade.play_sound(self.coin_sound)
            self.score += 1

        changed = False

        left_bndry = self.view_left + viewport_margin
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True

        right_bndry = self.view_left + screen_width - viewport_margin
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True

        top_bndry = self.view_bottom + screen_height - viewport_margin
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True

        bottom_bndry = self.view_bottom + viewport_margin
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        if changed:
            arcade.set_viewport(self.view_left,
                                screen_width + self.view_left - 1,
                                self.view_bottom,
                                screen_height + self.view_bottom - 1)
            self.score_y = self.view_bottom + 5
            self.score_x = self.view_left + 5

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = movement_speed
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -movement_speed
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -movement_speed
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = movement_speed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    window = BlockGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
