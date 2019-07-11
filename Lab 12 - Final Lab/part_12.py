import arcade
import math
from random import randrange as randr

screen_width = 1000
screen_height = 700

player_scaling = 0.6
snow_scaling = 0.5
tile_scaling = 0.8
coin_scaling = 1
margin_scaling = 0.9
heart_scaling = 0.14
bullet_scaling = .3
image_scaling = 1
enemy_bullet_scaling = 0.09
enemy_scaling = 0.35
gift_scaling = 0.65

movement_speed = 8
increase_gravity = -14
jump_force = 20
bullet_speed = 10


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        """Image from kenney.nl https://kenney.nl/assets/holiday-pack-2016"""
        self.texture_right = arcade.load_texture("santa.png", mirrored=True, scale=player_scaling)
        self.texture_left = arcade.load_texture("santa.png", scale=player_scaling)

        self.texture = self.texture_right


class Enemy(arcade.Sprite):

    def __init__(self, center_x, center_y):
        super().__init__()

        self.center_x = center_x
        self.center_y = center_y

        # Image from smwcentral https://www.smwcentral.net/?p=viewthread&t=89926&page=1&pid=1429385#p1429385
        self.texture_right = arcade.load_texture("mario.png", scale=enemy_scaling)
        self.texture_left = arcade.load_texture("mario.png", mirrored=True, scale=enemy_scaling)

        self.texture = self.texture_left


class FinalGame(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, "Scrolling screen")

        # All sounds from kenney.nl
        self.coin_sound = arcade.load_sound("coin3.ogg")
        self.hurt_sound = arcade.load_sound("hurt3.ogg")
        self.jump_sound = arcade.load_sound("jump1.ogg")
        self.kill_enemy_sound = arcade.load_sound("fall5.ogg")
        self.life_sound = arcade.load_sound("upgrade4.ogg")
        self.shoot_sound = arcade.load_sound("laser2.ogg")

        self.score = 0
        self.score_x = 5
        self.score_y = 5

        self.level = 0
        self.life = None

        self.player_list = None
        self.block_list = None
        self.coin_list = None
        self.snow_list = None
        self.life_list = None
        self.bullet_list = None
        self.enemy_bullet_list = None
        self.enemies_list = None
        self.instructions_list = None

        self.viewport_margin = 140

        self.player_sprite = None
        self.snow_flakes = None

        self.physics_engine = None

        self.frame_count = 0

        self.view_left = 0
        self.view_bottom = 0

        self.set_mouse_visible(False)

    def reset(self):
        """This will help reset player position and clear lists to avoid errors and
        draw new blocks for each new level."""
        self.block_list = arcade.SpriteList()
        self.life_list = arcade.SpriteList()
        self.enemies_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.instructions_list = arcade.SpriteList()
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.block_list)
        self.physics_engine.gravity_constant = 1.5
        self.player_sprite.center_x = 130
        self.player_sprite.center_y = 90
        self.wall_boundary()

    def wall_boundary(self):
        """The next four loops are just boundaries so that the character
                        does not escape from the game."""
        for h in range(36, 1300, 68):
            """Image from kenney.nl https://kenney.nl/assets/holiday-pack-2016"""
            window = arcade.Sprite("window.png", margin_scaling)
            window.center_y = 32
            if h % 2 == 0:
                window.center_x = h
                self.block_list.append(window)

        for h in range(32, 900, 64):
            window = arcade.Sprite("window.png", margin_scaling)
            window.center_x = 35
            if h % 2 == 0:
                window.center_y = h
                self.block_list.append(window)

        for h in range(36, 1300, 68):
            window = arcade.Sprite("window.png", margin_scaling)
            window.center_y = 868
            window.center_x = h
            self.block_list.append(window)

        for h in range(34, 900, 64):
            window = arcade.Sprite("window.png", margin_scaling)
            window.center_x = 1326
            if h % 2 == 0:
                window.center_y = h
                self.block_list.append(window)

    def start_screen(self):
        self.reset()
        # Image from kenney.nl https://kenney.nl/assets/holiday-pack-2016
        coin = arcade.Sprite("gift.png", gift_scaling)
        coin.center_y = 95
        coin.center_x = 900
        self.coin_list.append(coin)

        # Image from 101 Computing https://www.101computing.net/pygame-how-to-control-your-sprite/
        arrows = arcade.Sprite("arrows.png", .5)
        arrows.center_x = 500
        arrows.center_y = 405
        self.instructions_list.append(arrows)

        candy = arcade.Sprite("candy_cane.png", 1.5)
        candy.center_x = 500
        candy.center_y = 240
        self.instructions_list.append(candy)

        self.level = .5

    def level_1(self):
        self.reset()
        self.score = 0
        """Loops for blocks and coins that are inside the boundaries."""
        for h in range(160, 800, 118):
            """Both images from kenney.nl https://kenney.nl/assets/holiday-pack-2016"""
            block = arcade.Sprite("tile_1.png", tile_scaling)
            coin = arcade.Sprite("candy_cane.png", coin_scaling)
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
            block = arcade.Sprite("tile_1.png", tile_scaling)
            coin = arcade.Sprite("candy_cane.png", coin_scaling)
            block.center_x = coordinate[0]
            block.center_y = coordinate[1]
            if coordinate[0] % 8 == 0:
                coin.center_x = coordinate[0]
                coin.center_y = coordinate[1] + 55
                self.coin_list.append(coin)
            self.block_list.append(block)

        for h in range(278, 1302, 52):
            block = arcade.Sprite("tile_1.png", tile_scaling)
            coin = arcade.Sprite("candy_cane.png", coin_scaling)
            block.center_x = h
            block.center_y = 278
            coin.center_x = h
            coin.center_y = 333
            self.block_list.append(block)
            self.coin_list.append(coin)

        for h in range(120, 336, 60):
            block = arcade.Sprite("tile_1.png", tile_scaling)
            coin = arcade.Sprite("candy_cane.png", coin_scaling)
            block.center_y = 396
            if h % 3 == 0:
                block.center_x = h
                self.block_list.append(block)
                if h % 16 == 0:
                    coin.center_x = h
                    coin.center_y = 451
                    self.coin_list.append(coin)

        individual_coin = arcade.Sprite("candy_cane.png", coin_scaling)
        individual_coin.center_y = 396
        individual_coin.center_x = 348
        self.coin_list.append(individual_coin)

        for h in range(564, 1250, 50):
            block = arcade.Sprite("tile_1.png", tile_scaling)
            coin = arcade.Sprite("candy_cane.png", coin_scaling)
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

        for h in range(830, 1300, 80):
            block = arcade.Sprite("tile_1.png", tile_scaling)
            block.center_y = 750
            block.center_x = h
            self.block_list.append(block)

    def pre_level_2(self):
        self.reset()
        life = arcade.Sprite("heart.png", .25)
        life.center_x = 500
        life.center_y = 400
        self.instructions_list.append(life)

        coin = arcade.Sprite("gift.png", gift_scaling)
        coin.center_y = 95
        coin.center_x = 900
        self.coin_list.append(coin)

    def level_2(self):
        self.reset()
        self.score -= 1
        for h in range(160, 800, 118):
            block = arcade.Sprite("tile_1.png", tile_scaling)
            coin = arcade.Sprite("candy_cane.png", coin_scaling)
            if h % 2 == 0:
                block.center_x = h
                block.center_y = h
                coin.center_x = h
                coin.center_y = h + 55
                self.block_list.append(block)
                self.coin_list.append(coin)
        for h in range(830, 1300, 80):
            block = arcade.Sprite("tile_1.png", tile_scaling)
            block.center_y = 750
            block.center_x = h
            self.block_list.append(block)
        for h in range(130, 690, 80):
            block_2 = arcade.Sprite("tile_2.png", tile_scaling)
            if h == 130:
                block_2.center_y = 632
                block_2.center_x = h
                self.block_list.append(block_2)
            elif h % 2 == 0 and h != 210:
                block_2.center_x = h
                block_2.center_y = 750
                self.block_list.append(block_2)
        """Image from WorldArtsMe http://worldartsme.com/chocolate-heart-clipart.html#"""
        life = arcade.Sprite("heart.png", heart_scaling)
        life.center_x = 130
        life.center_y = 687
        self.life_list.append(life)

        coin = arcade.Sprite("candy_cane.png", coin_scaling)
        coin.center_x = 1265
        coin.center_y = 95
        self.coin_list.append(coin)

    def pre_level_3(self):
        self.reset()
        # Image from Kupiter https://www.kupiter.org/q190761704
        spacebar = arcade.Sprite("spacebar.png", .26)
        spacebar.center_x = 500
        spacebar.center_y = 450
        self.instructions_list.append(spacebar)

        enemy = arcade.Sprite("mario.png", enemy_scaling)
        enemy.center_x = 500
        enemy.center_y = 250
        self.instructions_list.append(enemy)

        coin = arcade.Sprite("gift.png", gift_scaling)
        coin.center_y = 95
        coin.center_x = 900
        self.coin_list.append(coin)

    def level_3(self):
        self.reset()
        self.score -= 1

        coordinate_list = [[220, 166],
                           [280, 166],
                           [460, 166],
                           [640, 166],
                           [940, 166],
                           [1000, 166],
                           [1180, 166],
                           [1240, 166],
                           [748, 166],
                           [800, 297],
                           [700, 297],
                           [1070, 297],
                           [426, 297],
                           [1230, 428],
                           [266, 428]]

        for coordinate in coordinate_list:
            if coordinate[1] % 2 == 0:
                block = arcade.Sprite("tile_2.png", tile_scaling)
            else:
                block = arcade.Sprite("tile_1.png", tile_scaling)
            coin = arcade.Sprite("candy_cane.png", coin_scaling)
            block.center_x = coordinate[0]
            block.center_y = coordinate[1]
            if coordinate[0] % 5 == 0:
                coin.center_x = coordinate[0]
                coin.center_y = coordinate[1] + 55
                self.coin_list.append(coin)
            self.block_list.append(block)

        for h in range(466, 567, 100):
            block = arcade.Sprite("tile_1.png", tile_scaling)
            coin = arcade.Sprite("candy_cane.png", coin_scaling)
            if h % 2 == 0:
                block.center_x = h
                block.center_y = h + 65
                coin.center_x = h
                coin.center_y = h + 120
                self.block_list.append(block)
                self.coin_list.append(coin)

        for h in range(666, 1239, 52):
            block = arcade.Sprite("tile_2.png", tile_scaling)
            block.center_y = 631
            block.center_x = h + 30
            self.block_list.append(block)
            if h == 1238:
                life = arcade.Sprite("heart.png", heart_scaling)
                life.center_x = h
                life.center_y = 686
                self.life_list.append(life)
                enemy = Enemy(h, 693)
                self.enemies_list.append(enemy)

        enemy = Enemy(1230, 490)
        self.enemies_list.append(enemy)

        enemy = Enemy(266, 490)
        self.enemies_list.append(enemy)

    def pre_level_4(self):
        self.reset()

        coin = arcade.Sprite("gift.png", gift_scaling)
        coin.center_y = 105
        coin.center_x = 500
        self.coin_list.append(coin)

    def level_4(self):
        self.score -= 1
        self.block_list = arcade.SpriteList()
        self.life_list = arcade.SpriteList()
        self.enemies_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.block_list)
        self.physics_engine.gravity_constant = 1.5
        self.player_sprite.center_x = 180
        self.player_sprite.center_y = 90

        for h in range(36, 2600, 68):
            """Image from kenney.nl https://kenney.nl/assets/holiday-pack-2016"""
            window = arcade.Sprite("window.png", margin_scaling)
            window.center_y = 32
            if h % 2 == 0:
                window.center_x = h
                self.block_list.append(window)

        for h in range(32, 1633, 64):
            window = arcade.Sprite("window.png", margin_scaling)
            window.center_x = 35
            if h % 2 == 0:
                window.center_y = h
                self.block_list.append(window)

        for h in range(36, 2600, 68):
            window = arcade.Sprite("window.png", margin_scaling)
            window.center_y = 1632
            window.center_x = h
            self.block_list.append(window)

        for h in range(34, 1633, 64):
            window = arcade.Sprite("window.png", margin_scaling)
            window.center_x = 2552
            if h % 2 == 0:
                window.center_y = h
                self.block_list.append(window)

        # Blocks inside boundaries.
        for h in range(90, 2500, 52):
            if h % 3 == 0:
                block = arcade.Sprite("tile_2.png", tile_scaling)
                block.center_x = h + 5
                block.center_y = 125
                self.block_list.append(block)
                coin = arcade.Sprite("candy_cane.png", coin_scaling)
                coin.center_x = h + 5
                coin.center_y = 180
                self.coin_list.append(coin)
            elif h % 3 != 0:
                block = arcade.Sprite("tile_1.png", tile_scaling)
                block.center_x = h + 5
                block.center_y = 240
                self.block_list.append(block)
                coin = arcade.Sprite("candy_cane.png", coin_scaling)
                coin.center_x = h + 5
                coin.center_y = 95
                self.coin_list.append(coin)
            if h % 9 == 0:
                block = arcade.Sprite("window.png", tile_scaling)
                block.center_x = h + 5
                block.center_y = 422
                self.block_list.append(block)
                enemy = Enemy(h + 5, 484)
                self.enemies_list.append(enemy)
            if h == 2430:
                life = arcade.Sprite("heart.png", heart_scaling)
                life.center_x = h + 5
                life.center_y = 477
                self.life_list.append(life)
        block = arcade.Sprite("tile_2.png", tile_scaling)
        block.center_x = 2352
        block.center_y = 350
        self.block_list.append(block)

        for h in range(90, 2500, 52):
            if h != 2430:
                block = arcade.Sprite("tile_1.png", tile_scaling)
                block.center_x = h + 5
                block.center_y = 553
                self.block_list.append(block)
                coin = arcade.Sprite("candy_cane.png", coin_scaling)
                coin.center_x = h + 5
                coin.center_y = 608
                self.coin_list.append(coin)

            if h % 9 == 0:
                block = arcade.Sprite("window.png", tile_scaling)
                block.center_x = h + 5
                block.center_y = 709
                self.block_list.append(block)
                enemy = Enemy(h + 5, 771)
                self.enemies_list.append(enemy)

    def pre_level_5(self):
        self.reset()

        coin = arcade.Sprite("gift.png", gift_scaling)
        coin.center_y = 95
        coin.center_x = 900
        self.coin_list.append(coin)

    def level_5(self):
        self.score -= 1
        self.block_list = arcade.SpriteList()
        self.life_list = arcade.SpriteList()
        self.enemies_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.block_list)
        self.physics_engine.gravity_constant = 1.5
        self.player_sprite.center_x = 220
        self.player_sprite.center_y = 756

        coordinate_list = [[220, 666],
                           [168, 718],
                           [168, 770],
                           [168, 822],
                           [272, 666],
                           [381, 666],
                           [433, 500],
                           # First enemy block
                           [626, 866],
                           [626, 500],
                           [745, 604],
                           [797, 735],
                           [1015, 448],
                           # Second enemy block
                           [1280, 656],
                           [1280, 448],
                           [1545, 448],
                           [1810, 448],
                           # Third enemy block
                           [1810, 656],
                           [2080, 448],
                           [2132, 579],
                           [1966, 683],
                           [2340, 371],
                           [2444, 371],
                           [2600, 371]]

        for coordinate in coordinate_list:
            if coordinate[0] % 3 == 0:
                block = arcade.Sprite("tile_2.png", tile_scaling)
            elif coordinate[0] % 2 == 0:
                block = arcade.Sprite("window.png", tile_scaling)
            else:
                block = arcade.Sprite("tile_1.png", tile_scaling)
            coin = arcade.Sprite("candy_cane.png", coin_scaling)
            block.center_x = coordinate[0]
            block.center_y = coordinate[1]
            if coordinate[0] % 5 == 0 and coordinate[0] != 1280:
                coin.center_x = coordinate[0]
                coin.center_y = coordinate[1] + 55
                self.coin_list.append(coin)
            self.block_list.append(block)

        enemy = Enemy(628, 928)
        self.enemies_list.append(enemy)

        enemy = Enemy(1280, 718)
        self.enemies_list.append(enemy)

        enemy = Enemy(1810, 718)
        self.enemies_list.append(enemy)

        life = arcade.Sprite("heart.png", heart_scaling)
        life.center_x = 628
        life.center_y = 921
        self.life_list.append(life)

        life = arcade.Sprite("heart.png", heart_scaling)
        life.center_x = 1810
        life.center_y = 711
        self.life_list.append(life)

    def setup(self):

        arcade.set_background_color(arcade.color.BABY_BLUE)

        self.view_left = 0
        self.view_bottom = 0

        self.player_list = arcade.SpriteList()
        self.block_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.snow_list = arcade.SpriteList()
        self.life_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.enemies_list = arcade.SpriteList()
        self.instructions_list = arcade.SpriteList()

        self.score = 0
        self.level = .5
        self.life = 22

        self.player_sprite = Player()
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        for i in range(15):
            """Image from kenney.nl https://kenney.nl/assets/holiday-pack-2016"""
            self.snow_flakes = arcade.Sprite("snow.png", snow_scaling)

            self.snow_flakes.center_x = randr(screen_width)
            self.snow_flakes.center_y = randr(screen_height)
            self.snow_flakes.change_x = 0.6
            self.snow_flakes.change_y = -2.63

            self.snow_list.append(self.snow_flakes)

        self.start_screen()

    def on_draw(self):
        arcade.start_render()
        self.block_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.snow_list.draw()
        self.life_list.draw()
        self.bullet_list.draw()
        self.enemies_list.draw()
        self.enemy_bullet_list.draw()
        self.instructions_list.draw()

        output = "Score: " + str(self.score)
        level = "Level: " + str(int(self.level))
        life = "Lives: " + str(self.life)
        if self.level != .5 and self.level != 1.5 and self.level != 2.5 and self.level != 3.5 and self.level != 4.5 \
                and self.life != 0 and self.level != 5.5:
            arcade.draw_text(level, self.score_x, self.score_y + 30, arcade.color.BLACK, 14)
            arcade.draw_text(output, self.score_x, self.score_y + 15, arcade.color.BLACK, 14)
        if self.level != 1 and self.level != .5 and self.level != 1.5 and self.level != 2.5 and self.level != 3.5 \
                and self.level != 4.5 and self.life != 0 and self.level != 5.5:
            arcade.draw_text(life, self.score_x, self.score_y, arcade.color.BLACK, 14)
        if self.life == 0:
            arcade.draw_text("Game Over", self.score_x + 270, self.score_y + 550, arcade.color.BLACK, 60)
            arcade.draw_text("Final score was " + str(self.score) + " points.", self.score_x + 270, self.score_y + 480,
                             arcade.color.BLACK, 25)
            arcade.draw_text("You died at level " + str(int(self.level)), self.score_x + 320, self.score_y + 410,
                             arcade.color.BLACK, 25)
            arcade.draw_text("Press ENTER to restart.", self.score_x + 320, self.score_y + 320, arcade.color.BLACK, 25)
        elif len(self.coin_list) == 0 and self.level == 5.5:
            arcade.draw_text("You won!", self.score_x + 270, self.score_y + 350, arcade.color.BLACK, 60)
            arcade.draw_text("Final score was " + str(self.score) + " points.", self.score_x + 270, self.score_y + 280,
                             arcade.color.BLACK, 25)
            arcade.draw_text("Press ENTER to play again.", self.score_x + 300, self.score_y + 200, arcade.color.BLACK,
                             25)

        if self.level == .5:
            instructions = "Use the arrows in your\nkeyboard to move."
            instructions_2 = "Eat the candy to score points."

            arcade.draw_text(instructions, 300, 550, arcade.color.BLACK, 30)
            arcade.draw_text(instructions_2, 300, 300, arcade.color.BLACK, 25)
            arcade.draw_text("Take gift\nto start.", 863, 150, arcade.color.BLACK, 14)
        elif self.level == 1.5:
            instructions = "Eat the chocolate to\ngain three lives."

            arcade.draw_text(instructions, 295, 535, arcade.color.BLACK, 35)
            arcade.draw_text("Take gift\nto continue.", 863, 150, arcade.color.BLACK, 14)
        elif self.level == 2.5:
            instructions = "Use spacebar to shoot."
            instructions_2 = "Enemies will try to kill you. Be careful!"

            arcade.draw_text(instructions, 295, 535, arcade.color.BLACK, 35)
            arcade.draw_text(instructions_2, 290, 335, arcade.color.BLACK, 25)
            arcade.draw_text("Take gift\nto continue.", 863, 150, arcade.color.BLACK, 14)
        elif self.level == 3.5:
            arcade.draw_text("Take gift\nto continue.", 463, 160, arcade.color.BLACK, 14)
        elif self.level == 4.5:
            instructions = "This is the last level.\n It is slightly different.\n Be careful, it is harder " \
                           "than it looks.\n As an advice I will say that you\nbetter don't fall."

            arcade.draw_text(instructions, 100, 535, arcade.color.BLACK, 35)
            arcade.draw_text("Take gift\nto continue.", 863, 150, arcade.color.BLACK, 14)

    def update(self, delta_time):
        #self.snow_list.update()
        if len(self.coin_list) != 0 and self.level <= 5 and self.life != 0:
            self.physics_engine.update()
            self.bullet_list.update()
            self.enemies_list.update()
            self.enemy_bullet_list.update()

        for snow in self.snow_list:
            if snow.top < self.view_bottom or snow.left > self.view_left + screen_width:
                snow.center_y = randr(self.view_bottom + screen_height, self.view_bottom + screen_height + 151)
                snow.center_x = randr(self.view_left + screen_width)

        if self.level == 5:
            self.viewport_margin = 300
        else:
            self.viewport_margin = 140

        self.frame_count += 1

        if self.player_sprite.center_y < -3500 and self.level == 5:
            self.player_sprite.center_x = 220
            self.player_sprite.center_y = 756
            self.life -= 1
            arcade.play_sound(self.hurt_sound)

        coins_hit = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        life_hit = arcade.check_for_collision_with_list(self.player_sprite, self.life_list)

        for coin in coins_hit:
            coin.kill()
            arcade.play_sound(self.coin_sound)
            self.score += 1

        for life in life_hit:
            life.kill()
            arcade.play_sound(self.life_sound)
            self.life += 3

        for bullet in self.bullet_list:
            enemies_hit = arcade.check_for_collision_with_list(bullet, self.enemies_list)
            if len(enemies_hit) > 0:
                bullet.kill()
            for enemy in enemies_hit:
                enemy.kill()
                self.score += 2
                arcade.play_sound(self.kill_enemy_sound)
            if bullet.right < self.view_left or bullet.left > self.view_left + screen_width:
                bullet.kill()

        for enemy in self.enemies_list:
            start_x = enemy.center_x
            start_y = enemy.center_y

            dest_x = self.player_sprite.center_x
            dest_y = self.player_sprite.center_y

            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            if self.frame_count % 60 == 0:
                bullet = arcade.Sprite("fire.png", enemy_bullet_scaling)
                bullet.center_x = start_x
                bullet.center_y = start_y

                bullet.angle = math.degrees(angle) + 45

                bullet.change_x = math.cos(angle) * bullet_speed
                bullet.change_y = math.sin(angle) * bullet_speed

                self.enemy_bullet_list.append(bullet)

            # Mirror enemies depending on the x position of the player.
            if self.player_sprite.center_x > enemy.center_x:
                enemy.texture = enemy.texture_right
            elif self.player_sprite.center_x < enemy.center_x:
                enemy.texture = enemy.texture_left

            for bullet in self.enemy_bullet_list:
                if bullet.bottom > self.view_bottom + screen_height or bullet.top < self.view_bottom or bullet.left > \
                        self.view_left + screen_width or bullet.right < self.view_left:
                    bullet.kill()
                player_hit = arcade.check_for_collision_with_list(bullet, self.player_list)
                if len(player_hit) > 0:
                    bullet.kill()
                for player in player_hit:
                    self.score -= 1
                    self.life -= 1
                    arcade.play_sound(self.hurt_sound)
                if bullet.right < self.view_left or bullet.left > self.view_left + screen_width:
                    bullet.kill()

        # Mirror santa image to make him go left and right.
        if self.player_sprite.change_x < 0:
            self.player_sprite.texture = self.player_sprite.texture_left
        if self.player_sprite.change_x > 0:
            self.player_sprite.texture = self.player_sprite.texture_right

        changed = False

        left_bndry = self.view_left + self.viewport_margin
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True

        right_bndry = self.view_left + screen_width - self.viewport_margin
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True

        top_bndry = self.view_bottom + screen_height - self.viewport_margin
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True

        bottom_bndry = self.view_bottom + self.viewport_margin
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

        """Code to advance one level each time the player eats all the candy."""
        if len(self.coin_list) == 0 and self.level == .5:
            self.level += .5
            self.level_1()
        elif len(self.coin_list) == 0 and self.level == 1:
            self.level += .5
            self.pre_level_2()
        elif len(self.coin_list) == 0 and self.level == 1.5:
            self.level += .5
            self.level_2()
        elif len(self.coin_list) == 0 and self.level == 2:
            self.level += .5
            self.pre_level_3()
        elif len(self.coin_list) == 0 and self.level == 2.5:
            self.level += .5
            self.level_3()
        elif len(self.coin_list) == 0 and self.level == 3:
            self.level += .5
            self.pre_level_4()
        elif len(self.coin_list) == 0 and self.level == 3.5:
            self.level += .5
            self.level_4()
        elif len(self.coin_list) == 0 and self.level == 4:
            self.level += .5
            self.pre_level_5()
        elif len(self.coin_list) == 0 and self.level == 4.5:
            self.level += .5
            self.level_5()
        elif len(self.coin_list) == 0 and self.level == 5:
            self.level += .5

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            arcade.play_sound(self.jump_sound)
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = jump_force
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = increase_gravity
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -movement_speed
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = movement_speed

        if key == arcade.key.SPACE and self.player_sprite.texture == self.player_sprite.texture_right \
                and self.level > 2:
            bullet = arcade.Sprite("large_tree.png", bullet_scaling)
            bullet.angle = 270
            bullet.change_x = bullet_speed
            bullet.center_y = self.player_sprite.center_y
            bullet.left = self.player_sprite.right
            self.bullet_list.append(bullet)
            arcade.play_sound(self.shoot_sound)
        elif key == arcade.key.SPACE and self.player_sprite.texture == self.player_sprite.texture_left \
                and self.level > 2:
            bullet = arcade.Sprite("large_tree.png", bullet_scaling)
            bullet.angle = 90
            bullet.change_x = -bullet_speed
            bullet.center_y = self.player_sprite.center_y
            bullet.right = self.player_sprite.left
            self.bullet_list.append(bullet)
            arcade.play_sound(self.shoot_sound)

        if self.life == 0 and key == arcade.key.ENTER:
            self.life = 22
            self.level = .5
            self.score = 0
            self.coin_list = arcade.SpriteList()
            self.start_screen()
        elif len(self.coin_list) == 0 and self.level == 5.5 and key == arcade.key.ENTER:
            self.life = 22
            self.level = .5
            self.score = 0
            self.coin_list = arcade.SpriteList()
            self.start_screen()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    window = FinalGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
