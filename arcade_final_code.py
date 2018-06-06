"""
Load a map stored in csv format, as exported by the program 'Tiled.'

Artwork from: http://kenney.nl
Tiled available from: http://www.mapeditor.org/

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_tiled_map
"""

import arcade
import os
import random
import game_button_and_led




SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALING)

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40
RIGHT_MARGIN = 650

# Physics
MOVEMENT_SPEED = 7.5
JUMP_SPEED = 19
GRAVITY = 1.2


def get_map(filename):
    """
    This function loads an array based on a map stored as a list of
    numbers separated by commas.
    """
    map_file = open(filename)
    map_array = []
    for line in map_file:
        line = line.strip()
        map_row = line.split(",")
        for index, item in enumerate(map_row):
            map_row[index] = int(item)
        map_array.append(map_row)
    return map_array


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.all_sprites_list = None
        self.box_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("images/character.png",
                                           SPRITE_SCALING)

        # Starting position of the player
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.all_sprites_list.append(self.player_sprite)

        

        # Creates a list which generates the map
                
        map_test = []
        one = []
        two = []
        three = []
        four = []
        five = []
        six = []
        seven = []


        

        for i in range(400):
            one.append(-1)
            two.append(-1)
            three.append(-1)
            four.append(-1)
            five.append(-1)
            seven.append(2)

        six.append(-1)
        six.append(-1)
        six.append(-1)
        six.append(-1)
        six.append(-1)
        six.append(-1)
        six.append(-1)
        six.append(-1)
        for i in range(100):
            a = random.randint(4, 8)
            for f in range(a):
                six.append(-1)
            six.append(0)
            

        map_test.append(one)
        map_test.append(two)
        map_test.append(three)
        map_test.append(four)
        map_test.append(five)
        map_test.append(six)
        map_test.append(seven)
        map_array = map_test

                
        # Right edge of the map in pixels
        self.end_of_map = len(map_array[0]) * GRID_PIXEL_SIZE

        for row_index, row in enumerate(map_array):
            for column_index, item in enumerate(row):

                # For this map, the numbers represent:
                # -1 = empty
                # 0  = box
                # 1  = grass left edge
                # 2  = grass middle
                # 3  = grass right edge
                # 4 = stone half
                if item == -1:
                    continue
                elif item == 0:
                    box = arcade.Sprite("images/boxCrate_double.png", SPRITE_SCALING)
                    box.right = column_index * 64
                    box.top = (7 - row_index) * 64
                    self.all_sprites_list.append(box)
                    self.box_list.append(box)
                    
                elif item == 1:
                    wall = arcade.Sprite("images/grassLeft.png", SPRITE_SCALING)
                elif item == 2:
                    wall = arcade.Sprite("images/grassMid.png", SPRITE_SCALING)
                elif item == 3:
                    wall = arcade.Sprite("images/grassRight.png", SPRITE_SCALING)
                elif item == 4:
                    wall = arcade.Sprite("images/stoneHalf.png", SPRITE_SCALING)

                if item > 1:
                    wall.right = column_index * 64
                    wall.top = (7 - row_index) * 64
                    self.all_sprites_list.append(wall)
                    self.wall_list.append(wall)

        self.physics_engine = \
            arcade.PhysicsEnginePlatformer(self.player_sprite,
                                           self.wall_list,
                                           gravity_constant=GRAVITY)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Set the view port boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

        self.game_over = False

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_sprite.draw()
        self.all_sprites_list.draw()

        distance = self.player_sprite.right/20
        distance = round(distance)
        
        output = "Distance: {}".format(distance)

        arcade.draw_text(output, self.view_left + 620, self.view_bottom + 550, arcade.color.WHITE, 14)
        if self.game_over:
            arcade.draw_text("Game Over", self.view_left + 300, self.view_bottom + 300, arcade.color.WHITE, 30)
        


        

    
    def on_key_press(self, key, modifiers):
        """
        Called whenever the key is pressed.
        """

        
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """


        if game_button_and_led.button_is_pressed():
            # make it jump
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED

        
        if self.player_sprite.right >= self.end_of_map:
            self.game_over = True
            

            

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        if not self.game_over:
            self.physics_engine.update()

        # --- Manage Scrolling ---

        # Track if we need to change the view port

        changed = False

        # Scroll left
        left_bndry = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True

        # Scroll right
        right_bndry = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True

        # Scroll up
        top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True

        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            changed = True

        # If we need to scroll, go ahead and do it.
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)\

        self.player_sprite.change_x = MOVEMENT_SPEED

        boxes_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.box_list)

        for box in boxes_hit_list:
            self.game_over = True

        if self.game_over:
            arcade.draw_text("Game Over", 400, 300, arcade.color.WHITE, 20)
            game_button_and_led.ledd()



def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
