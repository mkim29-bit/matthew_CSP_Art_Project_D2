import simple_graphics as sg

def draw_picture(width, height):
    """Draws a static picture."""
    
    # Fill the background
    sg.fill_background("white")
    
    # make some variables available
    colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    
    triangle_height = height/5
    triangle_width = width / 3
    
    
    # 2. Draw your clean, wide beach scene!
    sg.draw_beach_scene(width, height, "light blue", "blue", "orange")
    
    
    # call fill sky
    sg.set_fill_color("#030bfc")
    sg.fill_rectangle(0,0,600,210)
    sg.set_fill_color("#0345fc")
    sg.fill_rectangle(0,50,600,200)
    sg.set_fill_color("#036ffc")
    sg.fill_rectangle(0,80,600,190)
    sg.set_fill_color("#038cfc")
    sg.fill_rectangle(0,100,600,180)
    sg.set_fill_color("#03b5fc")
    sg.fill_rectangle(0,120,600,170)
    
    # 2. Middle Layer (The Sun)
    sg.draw_horizon_sun(width, height, "#f75019")

    sg.set_fill_color("#8B4513")
    sg.set_line_thickness(3)
    sg.draw_palm_tree(450, 350, 130, "#228B22")

    sg.set_fill_color("#8B4513")
    sg.set_line_thickness(3)
    sg.draw_palm_tree(500, 300, 100, "#228B22")
   
    # Draw a volleyball on the sand
    sg.set_outline_color("black")
    sg.set_line_thickness(2)
    sg.draw_volleyball(380, 320, 20, "white") # (x, y, radius, color)
    
    

if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)

