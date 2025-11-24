init -10 python:
    clock_hour = 7
    clock_minute = 0

init python:
    def update_clock(new_clock_hour, new_clock_minute):
        global clock_hour, clock_minute
        
        clock_hour = new_clock_hour
        clock_minute = new_clock_minute

screen clock_screen():
    # Use a frame container to add a background
    frame:
        xalign 1.0  # Align the anchor point to the right edge of the screen
        yalign 0.0  # Align the anchor point to the top edge of the screen
        xanchor 1.0  # Set the anchor point to the right side of the frame
        yanchor 0.0  # Set the anchor point to the top of the frame
        padding (20, 5, 20, 5)
        background '#8F8476'

        # Use xoffset and yoffset to add padding
        xoffset -10  # Move the frame 20 pixels left from the anchor point
        yoffset 10   # Move the frame 10 pixels down from the anchor point

        # Display the time in HH:MM format
        text "{:02d}:{:02d}".format(clock_hour, clock_minute):
            size 30
            color "#FFFFFF"  # White text color