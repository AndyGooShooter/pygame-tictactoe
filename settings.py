### DISPLAY SIZES
# the entire background image
bg_h = 1890 
bg_w = 2100
offset = 105 # offset for board

# each square
square_h = 210 
square_w = 210

# each point
point_h = 30 
point_w = 30

display_multiplier = 0.2 # edit this to change the overall size of the display

# final display size
master_h = bg_h * display_multiplier 
master_w = bg_w * display_multiplier
master_offset = offset * display_multiplier # offset from the top left corner of the screen
master_square_h = square_h * display_multiplier
master_square_w = square_w * display_multiplier