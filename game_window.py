
import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


class MyGame(arcade.Window):


    def __init__(self, width, height):
        super().__init__(width, height)


        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

  

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)



