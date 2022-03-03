import arcade
  
# Creating MainGame class       
class MainGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 600,
                         title="Text in Arcade")
  
  
    # Creating on_draw() function to draw on the screen
    def on_draw(self):
        arcade.start_render()
          
        # Drawing the text using draw_text()
        # draw_text function is used to draw 
        # text to the screen using Pyglet’s label.
        arcade.draw_text("GeeksforGeeks",120.0,300.0,
                         arcade.color.GREEN,40,80,'left')
  
# Calling MainGame class       
MainGame()
arcade.run()