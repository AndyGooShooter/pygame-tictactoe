### DISPLAY SIZES
# the entire background image
bg_w = 1890 
bg_h = 2100
offset = 105 # offset for board

# each square
square_w = 210 
square_h = 210

# each point
point_w = 150 
point_h = 150
center_offset = 30 # offset for points to be centered in the middle of the square

# text starting point
text_w = 105
text_h = 1890

# edit this to change the overall size of the display
display_multiplier = 0.2

# final display size
master_w = bg_w * display_multiplier
master_h = bg_h * display_multiplier 

master_offset = offset * display_multiplier # offset from the top left corner of the screen

master_square_w = square_w * display_multiplier
master_square_h = square_h * display_multiplier

master_point_w = point_w * display_multiplier
master_point_h = point_h * display_multiplier

master_center_offset = center_offset * display_multiplier

master_text_w = text_w * display_multiplier
master_text_h = text_h * display_multiplier
