import simple_graphics as sg

def draw_picture(width, height):
    """Draws a static picture."""
    
    # Fill the background
    sg.fill_background("white")
    
    # make some variables available
    colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    
    triangle_height = height/5
    triangle_width = width / 3
    
    
    # 2. Draw your clean, wide beach scene! - Matthew
    sg.draw_beach_background(width, height, "light blue", "blue", "orange")
    
    
    # call fill sky - Sunny
    sg.set_fill_color("#030bfc")
    sg.set_outline_color("#030bfc")
    sg.fill_rectangle(0,0,600,210)
    sg.set_fill_color("#0345fc")
    sg.set_outline_color("#0345fc")
    sg.fill_rectangle(0,50,600,200)
    sg.set_fill_color("#036ffc")
    sg.set_outline_color("#036ffc")
    sg.fill_rectangle(0,80,600,190)
    sg.set_fill_color("#038cfc")
    sg.set_outline_color("#038cfc")
    sg.fill_rectangle(0,100,600,180)
    sg.set_fill_color("#03b5fc")
    sg.set_outline_color("#03b5fc")
    sg.fill_rectangle(0,120,600,170)
    
    #draw clouds - Sunny
    sg.set_fill_color("white")
    sg.set_outline_color("white")
    sg.fill_circle(50,80,25)
    sg.fill_circle(90,60,25)
    sg.fill_circle(120,70,25)
    sg.fill_circle(170,90,25)
    sg.fill_circle(140,95,25)
    sg.fill_circle(100,95,25)
    sg.fill_circle(150,80,25)
    sg.fill_circle(80,90,30)
    sg.fill_circle(500,110,30)
    sg.fill_circle(470,125,25)
    sg.fill_circle(550,100,25)
    sg.fill_circle(600,110,25)
    sg.fill_circle(530,90,15)
    sg.fill_circle(570,100,15)
    sg.fill_circle(550,120,25)
    sg.fill_circle(520,125,25)
    sg.fill_circle(565,125,25)
    
    # Draw a sun - Matthew
    sg.draw_horizon_sun(width, height, "#f75019")

    # Draw palm trees - Minyoo
    sg.set_fill_color("#8B4513")
    sg.set_line_thickness(3)
    sg.draw_palm_tree(450, 350, 130, "#228B22")

    sg.set_fill_color("#8B4513")
    sg.set_line_thickness(3)
    sg.draw_palm_tree(500, 300, 100, "#228B22")
   
    # Draw a volleyball on the sand - Minyoo
    sg.set_outline_color("black")
    sg.set_line_thickness(2)
    sg.draw_volleyball(380, 320, 20, "white") # (x, y, radius, color)
    
    

if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)


