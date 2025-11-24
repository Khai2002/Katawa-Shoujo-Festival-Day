init python:
    move_lock = False
    action_lock = False

    def unlock_free_roam():
        global move_lock, action_lock
        move_lock = False
        action_lock = False
    
    def lock_free_roam():
        global move_lock, action_lock
        move_lock = True
        action_lock = True


    def format_string(input_string):
        # Split the string by underscores
        words = input_string.split('_')
        
        # Capitalize each word and join them with spaces
        formatted_string = ' '.join(word.capitalize() for word in words)
        
        return formatted_string

    def to_camel_case(input_string):
        if not input_string:
            return ""  # Return an empty string if input is empty
        
        # Split the string into words, ignoring extra spaces
        words = [word for word in input_string.split() if word]
        
        if not words:
            return ""  # Return an empty string if no valid words are found
        
        # Convert to camelCase
        camel_case = words[0].lower()
        for word in words[1:]:
            camel_case += word.capitalize()
        
        return camel_case

    def custom_crop(image_path):
        # Crop the image to 1920x1080 (centered)
        cropped_image = Crop((0, 0, 1920, 1080), image_path)
        transformed_image = Transform(cropped_image, zoom=0.15)
        return transformed_image

    def grayscale(displayable): 
        # Use Transform to apply a grayscale effect
        return Transform(displayable, matrixcolor=SaturationMatrix(0))

    def add_border(image_path, border_color='#8F8476', border_size=5, xsize=288, ysize=162):
        # Create a bordered image using Composite
        return Composite(
            (xsize + border_size * 2, ysize + border_size * 2),  # Total size (image + border)
            (0, 0), Solid(border_color, xsize=xsize + border_size * 2, ysize=ysize + border_size * 2),  # Border
            (border_size, border_size), image_path  # Image centered inside the border
        )

# Define the hover effect
transform hover_effect:
    on hover:
        linear 0.15 zoom 1.05  # Slightly enlarge on hover
    on idle:
        linear 0.15 zoom 1  # Return to normal size

################################################################################
## Location Selector screen
################################################################################

screen location_selector(location_images, location_labels, location_available=[]):
    python:
        if len(location_available) < len(location_images):
            location_available = [1,] * len(location_images)

    hbox:
        xalign 0.5
        yalign 0
        yoffset 60
        spacing 20

        for i in range(len(location_images)):

            if location_available[i]:
                $ frame_background = "#8F8476"  # Default color
            else:
                $ frame_background = "#8e8e8e"  # Color when insensitive
            
            vbox:
                align (0.5, 0.5)  # Center the vbox

                frame:
                    background frame_background
                    padding (15, 2)
                    xalign 0.5  # Center horizontally
                    yalign 0.5  # Center vertically

                    text format_string(str(location_labels[i])):
                        size 20 
                        color "#FFFFFF"
                        align (0.5, 0.5)  # Center the text

                imagebutton:
                    
                    idle add_border(custom_crop(location_images[i]))  # Crop and scale the image
                    hover add_border(custom_crop(location_images[i]), border_color='#c7ab87')
                    insensitive Fixed(
                        grayscale(add_border(custom_crop(location_images[i]))),  # Grayscale image
                        Transform("gui/lock.png", zoom=0.13, anchor=(0.5, 0.5), pos=(0.5, 0.5)),  # Lock image centered
                        fit_first=True
                    )
                    action [Hide("location_selector"), Jump(location_labels[i])]
                    at hover_effect  # Apply the hover effect
                    keysym str(i+1)
                    sensitive location_available[i]

################################################################################
## Move Screen
################################################################################

style move_button:
    background '#8F8476' 
    padding (10, 5)      
    hover_background '#c7ab87'
    insensitive_background '#3f3a35' 
    yalign 0.0 
    xoffset 10
    yoffset 10

style custom_button_text:
    size 30
    color "#ffffff"
    hover_color "#ffffff"
    insensitive_color "#555"

screen move():
    textbutton "MOVE":
        action ToggleScreen("location_selector", 
            location_images=location_images if 'location_images' in globals() else [], 
            location_labels=location_labels if 'location_labels' in globals() else [],
            location_available=location_available if 'location_available' in globals() else [],
            transition=dissolve_fast
        )
        style "move_button"  # Apply the custom style
        text_style "custom_button_text"
        keysym "m"
        sensitive not move_lock
