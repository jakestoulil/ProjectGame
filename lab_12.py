""" Lab 12 """

import random
import arcade

# Constants
SPRITE_SCALING_PLAYER = 0.4
SPRITE_SCALING_ENEMY = 0.3
SPRITE_SCALING_LASER = 0.2
SPRITE_SCALING_BARRIER = 1.4

ROW_COUNT = 4
COLUMN_COUNT = 16

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 5
MOVEMENT_SPEED = 7
ENEMY_SHIP_SPEED = .3


class PlayerShip(arcade.Sprite):
    """ Player Sprite """
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.center_x = 400
        self.center_y = 55
        self.angle = 180

    def setup(self):
        self.center_x = 400
        self.center_y = 55
        self.angle = 180

    def update(self):
        super().update()


class MyAppWindow(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 12")

        # Boolean Variables
        self.game_over = False
        self.player_killed = False
        self.level_complete = False
        self.game_running = False
        self.game_beat = False
        self.game_started = False

        # Variables that will hold sprite lists
        self.all_sprites_list = None
        self.enemy_list = None
        self.bullet_list = None
        self.enemy_bullet_list = None
        self.all_bullet_list = None
        self.player_sprite_list = None
        self.background = None
        self.barrier_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.lives = 3
        self.level = 1
        self.bullets_shot = 0
        self.enemies_killed = 0
        self.bullets_dodged = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Load sounds
        # Player Shooting Sound is from Sound Bible (http://soundbible.com/709-Bottle-Rocket.html)
        self.player_shooting = arcade.sound.load_sound("sound_effects/enemy_shooting.wav")

        # Enemy Shooting Sound is from Sound Bible (http://soundbible.com/1875-Bullet-Whizzing-By.html)
        self.enemy_shooting_sound = arcade.sound.load_sound("sound_effects/player_shooting.wav")

        # Player Killed sound is from Sound Bible (http://soundbible.com/1875-Bullet-Whizzing-By.html)
        self.player_killed_sound = arcade.sound.load_sound("sound_effects/player_killed.wav")

        # Enemy Killed sound is from Sound Bible (http://soundbible.com/1919-Shotgun-Blast.html)
        self.enemy_killed_sound = arcade.sound.load_sound("sound_effects/enemy_killed.wav")
        # Level Up sound is from Sound Bible (http://soundbible.com/1639-Power-Up.html)
        self.level_up = arcade.load_sound("sound_effects/level_up.wav")

    # Level 1
    def level_1(self):
        # Draw Player Character. Image from Iconizer.net (https://icons8.com/iconizer/en/search/5/%D1%81%D0%BC%D0%B8)
        self.player_sprite = PlayerShip("Images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 55
        self.player_sprite.angle = 180
        self.player_sprite_list.append(self.player_sprite)
        self.all_sprites_list.append(self.player_sprite)

        for column in range(ROW_COUNT):
            for row in range(COLUMN_COUNT):
                # Draw enemy character. Image from Paranormal beta
                # (http://dianavermilya.github.io/paranormal-site/tutorial-spaceship.html)
                enemy = arcade.Sprite("Images/enemy_character.png", SPRITE_SCALING_ENEMY)
                enemy.center_x = 75 + row * 45
                enemy.center_y = 275 + column * 100
                enemy.angle = 180
                enemy.change_x = -ENEMY_SHIP_SPEED
                self.all_sprites_list.append(enemy)
                self.enemy_list.append(enemy)

    # Level 2
    def level_2(self):
        # Kill all the bullets
        for bullet in self.bullet_list:
            bullet.kill()

        # Draw Player Character. Image from Iconizer.net (https://icons8.com/iconizer/en/search/5/%D1%81%D0%BC%D0%B8)
        self.player_sprite = PlayerShip("Images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 55
        self.player_sprite.angle = 180
        self.player_sprite_list.append(self.player_sprite)
        self.all_sprites_list.append(self.player_sprite)

        for column in range(ROW_COUNT):
            for row in range(COLUMN_COUNT):
                # Draw enemy character. Image from Paranormal beta
                # (http://dianavermilya.github.io/paranormal-site/tutorial-spaceship.html)
                enemy = arcade.Sprite("Images/enemy_character.png", SPRITE_SCALING_ENEMY)
                enemy.center_x = 75 + row * 45
                enemy.center_y = 275 + column * 100
                enemy.angle = 180
                enemy.change_x = -ENEMY_SHIP_SPEED - 0.5
                self.all_sprites_list.append(enemy)
                self.enemy_list.append(enemy)

    # Level 3
    def level_3(self):
        # Kill all the bullets
        for bullet in self.bullet_list:
            bullet.kill()

        # Draw Player Character. Image from Iconizer.net (https://icons8.com/iconizer/en/search/5/%D1%81%D0%BC%D0%B8)
        self.player_sprite = PlayerShip("Images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 55
        self.player_sprite.angle = 180
        self.player_sprite_list.append(self.player_sprite)
        self.all_sprites_list.append(self.player_sprite)

        for column in range(ROW_COUNT):
            for row in range(COLUMN_COUNT):
                # Draw enemy character. Image from Paranormal beta
                # (http://dianavermilya.github.io/paranormal-site/tutorial-spaceship.html)
                enemy = arcade.Sprite("Images/enemy_character.png", SPRITE_SCALING_ENEMY)
                enemy.center_x = 75 + row * 45
                enemy.center_y = 275 + column * 100
                enemy.angle = 180
                enemy.change_x = -ENEMY_SHIP_SPEED - 1.0
                self.all_sprites_list.append(enemy)
                self.enemy_list.append(enemy)

    # Level 4
    def level_4(self):
        # Kill all the bullets
        for bullet in self.bullet_list:
            bullet.kill()

        # Draw Player Character. Image from Iconizer.net (https://icons8.com/iconizer/en/search/5/%D1%81%D0%BC%D0%B8)
        self.player_sprite = PlayerShip("Images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 55
        self.player_sprite.angle = 180
        self.player_sprite_list.append(self.player_sprite)
        self.all_sprites_list.append(self.player_sprite)

        for column in range(ROW_COUNT):
            for row in range(COLUMN_COUNT):
                # Draw enemy character. Image from Paranormal beta
                # (http://dianavermilya.github.io/paranormal-site/tutorial-spaceship.html)
                enemy = arcade.Sprite("Images/enemy_character.png", SPRITE_SCALING_ENEMY)
                enemy.center_x = 75 + row * 45
                enemy.center_y = 275 + column * 100
                enemy.angle = 180
                enemy.change_x = -ENEMY_SHIP_SPEED - 1.5
                self.all_sprites_list.append(enemy)
                self.enemy_list.append(enemy)

    # Level 5
    def level_5(self):
        # Kill all the bullets
        for bullet in self.bullet_list:
            bullet.kill()

        # Draw Player Character. Image from Iconizer.net (https://icons8.com/iconizer/en/search/5/%D1%81%D0%BC%D0%B8)
        self.player_sprite = PlayerShip("Images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 55
        self.player_sprite.angle = 180
        self.player_sprite_list.append(self.player_sprite)
        self.all_sprites_list.append(self.player_sprite)

        for column in range(ROW_COUNT):
            for row in range(COLUMN_COUNT):
                # Draw enemy character. Image from Paranormal beta
                # (http://dianavermilya.github.io/paranormal-site/tutorial-spaceship.html)
                enemy = arcade.Sprite("Images/enemy_character.png", SPRITE_SCALING_ENEMY)
                enemy.center_x = 75 + row * 45
                enemy.center_y = 275 + column * 100
                enemy.angle = 180
                enemy.change_x = -ENEMY_SHIP_SPEED - 2.0
                self.all_sprites_list.append(enemy)
                self.enemy_list.append(enemy)

    # Level 6
    def level_6(self):
        # Kill all the bullets
        for bullet in self.bullet_list:
            bullet.kill()

        # Draw Player Character. Image from Iconizer.net (https://icons8.com/iconizer/en/search/5/%D1%81%D0%BC%D0%B8)
        self.player_sprite = PlayerShip("Images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 55
        self.player_sprite.angle = 180
        self.player_sprite_list.append(self.player_sprite)
        self.all_sprites_list.append(self.player_sprite)

        for column in range(ROW_COUNT):
            for row in range(COLUMN_COUNT):
                # Draw enemy character. Image from Paranormal beta
                # (http://dianavermilya.github.io/paranormal-site/tutorial-spaceship.html)
                enemy = arcade.Sprite("Images/enemy_character.png", SPRITE_SCALING_ENEMY)
                enemy.center_x = 75 + row * 45
                enemy.center_y = 275 + column * 100
                enemy.angle = 180
                enemy.change_x = -ENEMY_SHIP_SPEED - 2.5
                self.all_sprites_list.append(enemy)
                self.enemy_list.append(enemy)

    # Level 7
    def level_7(self):
        # Kill all the bullets
        for bullet in self.bullet_list:
            bullet.kill()

        # Draw Player Character. Image from Iconizer.net (https://icons8.com/iconizer/en/search/5/%D1%81%D0%BC%D0%B8)
        self.player_sprite = PlayerShip("Images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 55
        self.player_sprite.angle = 180
        self.player_sprite_list.append(self.player_sprite)
        self.all_sprites_list.append(self.player_sprite)

        for column in range(ROW_COUNT):
            for row in range(COLUMN_COUNT):
                # Draw enemy character. Image from Paranormal beta
                # (http://dianavermilya.github.io/paranormal-site/tutorial-spaceship.html)
                enemy = arcade.Sprite("Images/enemy_character.png", SPRITE_SCALING_ENEMY)
                enemy.center_x = 75 + row * 45
                enemy.center_y = 275 + column * 100
                enemy.angle = 180
                enemy.change_x = -ENEMY_SHIP_SPEED - 3.0
                self.all_sprites_list.append(enemy)
                self.enemy_list.append(enemy)

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.game_over = False
        self.player_killed = False
        self.level_complete = False
        self.game_running = False
        self.game_beat = False
        self.game_started = False
        self.level = 1
        self.score = 0
        self.bullets_shot = 0
        self.enemies_killed = 0
        self.bullets_dodged = 0

        # Background image from opengameart.org (https://opengameart.org/content/space-cartoony-tiled-texture)
        self.background = arcade.load_texture("Images/background.png")

        # Set up sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.all_bullet_list = arcade.SpriteList()
        self.player_sprite_list = arcade.SpriteList()
        self.barrier_list = arcade.SpriteList()

        # Draw barriers between player and enemies. Barrier Image from Reno Depot
        # (https://www.renodepot.com/en/all-products)
        for column in range(5):
            barrier = arcade.Sprite("Images/barrier.png", SPRITE_SCALING_BARRIER)
            barrier.center_x = 100 + column * 150
            barrier.center_y = 125
            self.all_sprites_list.append(barrier)
            self.barrier_list.append(barrier)

        # Call level 1 first
        self.level_1()

    def reset(self):
        """ Function for when the player sprite gets killed """

        # Kill the bullets that are on screen when player is killed.
        for enemy_bullet in self.enemy_bullet_list:
            enemy_bullet.kill()
        for bulet in self.bullet_list:
            bulet.kill()

        # Image from Iconizer.net (https://icons8.com/iconizer/en/search/5/%D1%81%D0%BC%D0%B8)
        self.player_sprite = PlayerShip("Images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 55
        self.player_sprite.angle = 180
        self.player_sprite_list.append(self.player_sprite)
        self.all_sprites_list.append(self.player_sprite)

    def end_game(self):
        """ Function for when the game ends """

        # Kills all the enemies and bullets so the end of game stats can be seen.
        for enemy in self.enemy_list:
            enemy.kill()

        for bullet in self.all_bullet_list:
            bullet.kill()

        # Print end of game stats on-screen.

        arcade.draw_text("Game Over", 300, 500, arcade.color.WHITE, 36)

        output_score = self.score
        arcade.draw_text(f"Score: {output_score}", 100, 450, arcade.color.WHITE, 24)

        output_levels_passed = self.level - 1
        arcade.draw_text(f"Levels Completed: {output_levels_passed}", 100, 400, arcade.color.WHITE, 24)

        output_bullets_shot = self.bullets_shot
        arcade.draw_text(f"Total Bullets Shot: {output_bullets_shot}", 100, 350, arcade.color.WHITE, 24)

        output_enemies_killed = self.enemies_killed
        arcade.draw_text(f"Total Enemy Ships Killed: {output_enemies_killed}", 100, 300, arcade.color.WHITE, 24)

        output_bullets_dodged = self.bullets_dodged
        arcade.draw_text(f"Total Enemy Bullets Dodged: {output_bullets_dodged}", 100, 250, arcade.color.WHITE, 24)

        output_hit_percentage = self.enemies_killed / self.bullets_shot
        arcade.draw_text(f"Hit Percentage: {output_hit_percentage:.0%}", 100, 200, arcade.color.WHITE, 24)

    def end_game_beaten(self):
        """ Same as the method for end of game but prints "All Levels Passed" insted of "Game Over" """

        for enemy in self.enemy_list:
            enemy.kill()

        for bullet in self.all_bullet_list:
            bullet.kill()

        arcade.draw_text("Passed All Levels", 250, 500, arcade.color.WHITE, 36)

        output_score = self.score
        arcade.draw_text(f"Score: {output_score}", 100, 450, arcade.color.WHITE, 24)

        output_levels_passed = 7
        arcade.draw_text(f"Levels Completed: {output_levels_passed}", 100, 400, arcade.color.WHITE, 24)

        output_bullets_shot = self.bullets_shot
        arcade.draw_text(f"Total Bullets Shot: {output_bullets_shot}", 100, 350, arcade.color.WHITE, 24)

        output_enemies_killed = self.enemies_killed
        arcade.draw_text(f"Total Enemy Ships Killed: {output_enemies_killed}", 100, 300, arcade.color.WHITE, 24)

        output_bullets_dodged = self.bullets_dodged
        arcade.draw_text(f"Total Enemy Bullets Dodged: {output_bullets_dodged}", 100, 250, arcade.color.WHITE, 24)

        output_hit_percentage = self.enemies_killed / self.bullets_shot
        arcade.draw_text(f"Hit Percentage: {output_hit_percentage:.0%}", 100, 200, arcade.color.WHITE, 24)

    def on_draw(self):
        """ Draw everything on-screen """

        arcade.start_render()

        # Draw background
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Draw box at the bottom of the screen which shows the score, how many lives are left, and level.
        arcade.draw_lrtb_rectangle_filled(0, 800, 25, 0, arcade.color.GRAY)

        self.all_sprites_list.draw()

        arcade.draw_text(f"Score: {self.score}", 375, 5, arcade.color.BLACK, 14)
        arcade.draw_text(f"Lives Left: {self.lives}", 90, 5, arcade.color.BLACK, 14)
        arcade.draw_text(f"Level: {self.level}", 650, 5, arcade.color.BLACK, 14)

        # Draws instructions when the game is froze.
        if self.player_killed or not self.game_running:
            if not self.game_over and not self.game_beat:
                arcade.draw_text("Press left or right arrow to start", 150, 200, arcade.color.WHITE, 30)
                if not self.game_started:
                    arcade.draw_text("Welcome to Space Shooters", 175, 400, arcade.color.WHITE, 30)
                    arcade.draw_text("Press the space bar to shoot", 175, 310, arcade.color.WHITE, 30)

        # Draws what level player is about to start after completing previous level.
        if self.level_complete and not self.game_beat:
            arcade.draw_text(f"Level {self.level}", 350, 200, arcade.color.WHITE, 30)

        # Calls game_over function when the game ends.
        if self.game_over:
            self.end_game()

        # Calls game_beat function when the player has completed all of the levels.
        if self.game_beat:
            self.end_game_beaten()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """

        # Moves the player sprite left and right
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
            self.player_killed = False
            self.game_running = True
            self.level_complete = False
            self.game_started = True
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
            self.player_killed = False
            self.game_running = True
            self.level_complete = False
            self.game_started = True

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

        # Shoots a bullet when the player hits the space bar.
        if key == arcade.key.SPACE and not self.player_killed:
            # Image from examples.phaser.io (https://examples.phaser.io/assets/particlestorm/particles/?C=S;O=D)
            bullet = arcade.Sprite("Images/laser.png", SPRITE_SCALING_LASER)

            # Position the bullet
            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top
            bullet.change_y += BULLET_SPEED
            self.bullets_shot += 1

            # Gunshot sound
            arcade.play_sound(self.player_shooting)

            # Add the bullet to the appropriate lists
            self.all_sprites_list.append(bullet)
            self.all_bullet_list.append(bullet)
            self.bullet_list.append(bullet)

    def update(self, delta_time):
        """ Movement and game logic """

        # Freezes game
        if not self.game_over and not self.player_killed and not self.level_complete and self.game_running and not \
                self.game_beat and self.game_started:

            self.all_sprites_list.update()

            # Enemies shoot at player
            for enemy in self.enemy_list:
                if random.randrange(2000) == 0:
                    # Draws the enemy sprite.
                    # Image from examples.phaser.io (https://examples.phaser.io/assets/particlestorm/particles/?C=S;O=D)
                    enemy_bullet = arcade.Sprite("images/laser.png", SPRITE_SCALING_LASER)
                    enemy_bullet.center_x = enemy.center_x
                    enemy_bullet.top = enemy.bottom
                    enemy_bullet.change_y = -2
                    arcade.play_sound(self.enemy_shooting_sound)
                    self.enemy_bullet_list.append(enemy_bullet)
                    self.all_bullet_list.append(enemy_bullet)
                    self.all_sprites_list.append(enemy_bullet)

            # Get rid of the bullet when it flies off-screen
            for bullet in self.all_bullet_list:
                if bullet.bottom < 25:
                    bullet.kill()
                    self.bullets_dodged += 1

                if bullet.bottom > SCREEN_HEIGHT:
                    bullet.kill()

            for bullet in self.bullet_list:

                # Check this bullet to see if it hit an enemy
                hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

                # If it did, get rid of the bullet
                if len(hit_list) > 0:
                    bullet.kill()

                # For every enemy we hit, add to the score, play the sound, and remove the enemy.
                for enemy in hit_list:
                    enemy.kill()
                    arcade.sound.play_sound(self.enemy_killed_sound)
                    self.enemies_killed += 1
                    self.score += 25

                # If the bullet flies off-screen, remove it.
                if bullet.bottom > SCREEN_HEIGHT:
                    bullet.kill()

            for bullet in self.all_bullet_list:
                # Check to see if bullet hit a barrier
                barrier_hit_list = arcade.check_for_collision_with_list(bullet, self.barrier_list)

                # If a bullet hit a barrier, kill the bullet.
                if len(barrier_hit_list) > 0:
                    bullet.kill()
                    self.bullets_dodged += 1

            for enemy in self.enemy_list:
                # Check to see if the enemy hit the barrier.
                enemy_hit_barrier = arcade.check_for_collision_with_list(enemy, self.barrier_list)

                # If the player hits the barrier then stop the game, kill the enemy, and the player loses a life.
                if len(enemy_hit_barrier) > 0:
                    enemy.kill()
                    arcade.sound.play_sound(self.enemy_killed_sound)
                    self.player_sprite.kill()
                    if self.lives > 0:
                        self.lives -= 1
                        self.score -= 100
                        self.player_killed = True
                        self.reset()

                    else:
                        self.player_killed = True
                        self.game_over = True

            for enemy_bullet in self.enemy_bullet_list:
                # Check to see if the enemy bullet hits the player.
                enemy_hit_list = arcade.check_for_collision_with_list(enemy_bullet, self.player_sprite_list)

                # If the enemy bullet hits the player, then we will kill the bullet, kill the player, and the player
                # loses a life.
                if len(enemy_hit_list) > 0:
                    enemy_bullet.kill()
                    self.player_sprite.kill()
                    arcade.sound.play_sound(self.player_killed_sound)
                    if self.lives > 0:
                        self.lives -= 1
                        self.score -= 100
                        self.player_killed = True
                        self.reset()

                    else:
                        self.player_killed = True
                        self.game_over = True

            for enemy in self.enemy_list:
                # Move the enemy to the sides and down the screen.
                enemy.center_x += enemy.change_x

                if enemy.center_x <= 50:
                    enemy.change_x *= -1
                    enemy.center_y -= 50

                if enemy.center_x >= 750:
                    enemy.change_x *= -1
                    enemy.center_y -= 50

            # If the player completes a level, move them to the next level
            if len(self.enemy_list) == 0 and self.level == 1:
                self.level_complete = True
                arcade.sound.play_sound(self.level_up)
                self.player_sprite.kill()
                self.level += 1
                self.level_2()
                for bullet in self.all_bullet_list:
                    bullet.kill()

            if len(self.enemy_list) == 0 and self.level == 2:
                self.level_complete = True
                arcade.sound.play_sound(self.level_up)
                self.player_sprite.kill()
                self.level += 1
                self.level_3()
                for bullet in self.all_bullet_list:
                    bullet.kill()

            if len(self.enemy_list) == 0 and self.level == 3:
                self.level_complete = True
                arcade.sound.play_sound(self.level_up)
                self.player_sprite.kill()
                self.level += 1
                self.level_4()
                for bullet in self.all_bullet_list:
                    bullet.kill()

            if len(self.enemy_list) == 0 and self.level == 4:
                self.level_complete = True
                arcade.sound.play_sound(self.level_up)
                self.player_sprite.kill()
                self.level += 1
                self.level_5()
                for bullet in self.all_bullet_list:
                    bullet.kill()

            if len(self.enemy_list) == 0 and self.level == 5:
                self.level_complete = True
                arcade.play_sound(self.level_up)
                self.player_sprite.kill()
                self.level += 1
                self.level_6()
                for bullet in self.all_bullet_list:
                    bullet.kill()

            if len(self.enemy_list) == 0 and self.level == 6:
                self.level_complete = True
                arcade.play_sound(self.level_up)
                self.player_sprite.kill()
                self.level += 1
                self.level_7()
                for bullet in self.all_bullet_list:
                    bullet.kill()

            # If the player completes level 7, then they have beaten the game, so end the game.
            if len(self.enemy_list) == 0 and self.level == 7:
                self.level_complete = True
                arcade.sound.play_sound(self.level_up)
                self.player_sprite.kill()
                self.level += 1
                for bullet in self.all_bullet_list:
                    bullet.kill()
                self.game_beat = True


def main():
    window = MyAppWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
