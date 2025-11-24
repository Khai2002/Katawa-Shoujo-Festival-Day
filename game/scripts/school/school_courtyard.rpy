# ====================================================================
# Main scene
# ====================================================================
label school_courtyard:
    # Setup ============= 
    hide screen action_menu

    python:
        location_images = ['school_gate', 'school_backexit', 'school_gardens', 'school_lobby', 'school_nursehall', 'school_track']
        location_labels = ['school_gate', 'school_backexit', 'school_gardens', 'school_lobby', 'school_nursehall', 'school_track']
        location_available = [1, 1, 1, 1, 1, avail_school_track]

        prefix = "school_courtyard"
        actions = []

        lock_free_roam()

    show screen move
    show screen action

    # Script ============
    scene school_courtyard with dissolve_fast
    
    # Free Roam =========
    $ unlock_free_roam()
    call screen location_selector(location_images, location_labels, location_available) with dissolve_fast
    
    return

# ====================================================================
# Support Scenes 
# ====================================================================