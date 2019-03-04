import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions




def draw_cloud():
    """ draw cloud """
    arcade.draw_circle_filled(300, 500, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(350, 500, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(400, 500, 45, arcade.color.WHITE)




def draw_rolling_hills():
    """ draw rolling hills """
    arcade.draw_circle_filled(100, 100, 200, arcade.color.ANDROID_GREEN)
    arcade.draw_circle_filled(300, 50, 150, arcade.color.ANDROID_GREEN)
    arcade.draw_circle_filled(500, 80, 100, arcade.color.ANDROID_GREEN)
    arcade.draw_circle_filled(600, 100, 180, arcade.color.ANDROID_GREEN)
    arcade.draw_circle_filled(800, 80, 150, arcade.color.ANDROID_GREEN)








def main():


    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # call your draw functions

    draw_cloud()
    draw_rolling_hills()






    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()