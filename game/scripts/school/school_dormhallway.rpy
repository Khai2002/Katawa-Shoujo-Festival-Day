init python:
    seen_school_dormhallway_7h_0 = False
    seen_school_dormhallway_11h_0 = False

# ====================================================================
# Main scene
# ====================================================================
label school_dormhallway:
    # Setup ============= 
    hide screen action_menu

    python: 
        location_images = ['school_dormhallground', 'school_dormhisao']
        location_labels = ['school_dormhallground', 'school_dormhisao']
        
        actions = []
        prefix = "school_dormhallway"

        lock_free_roam() 
        
    show screen move
    show screen action

    # Script ============
    if not seen_school_dormhallway_7h_0 and clock_hour == 7:
        call school_dormhallway_7h_0
    
    if not seen_school_dormhallway_11h_0 and clock_hour == 11:
        call school_dormhallway_11h_0

    scene school_dormhallway with dissolve_fast

    # Free Roam =========
    $ unlock_free_roam()
    call screen location_selector(location_images, location_labels) with dissolve_fast
    
    return

# ====================================================================
# Support Scenes 
# ====================================================================

label school_dormhallway_7h_0:
    
    $ seen_school_dormhallway_7h_0 = True

    scene school_dormhallway with dissolve_fast

    "I push open my dorm door and step into the hallway."

    "On the far side, someone is leading visitors around, probably family members."

    "They lean against a door, chatting enthusiastically, making the whole corridor feel alive."
    
    "Maybe a little too alive for an early morning."

    "I glance toward the room opposite mine and wonder what kind of weird plans Kenji might have today."

    "I don't have anyone to hang out with, so maybe I could ask him. Then again, it doesn't look like he's in the mood for any festival activity."

    "No light passes through the crack under his door. The room is pitch black. He must still be asleep, blinds pulled tight."

    "I think about knocking, but quickly realize it might not be such a great idea."

    "Some people are better left undisturbed. I'll try to find someone else to spend the day with."

    jump school_dormhallway


label school_dormhallway_11h_0:

    $ seen_school_dormhallway_11h_0 = True

    scene school_dormhallway with dissolve_fast

    "I push open my dorm door and step into the hallway."

    "Contrasting the festival outside, the hallway is still and silent, the only sound the faint buzz of voices and music seeping through the walls."

    "I take a step forward, and then a sudden frantic rustling breaks out in the room opposite mine."

    "It's coming from Kenji's room. Hard to tell what he's doing. Something that involves shifting furniture, or possibly fighting it."

    "I pause in front of his door, hesitating."

    "I could knock. Maybe see what he's planning today."

    "Part of me is curious. Part of me remembers how conversations with him tend to spiral into places I can't quite follow."

    "Still, with the festival outside and nothing on my agenda, the idea doesn't sound entirely terrible."

    jump school_dormhallway