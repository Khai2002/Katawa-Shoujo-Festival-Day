# ====================================================================
# Main scene
# ====================================================================
label school_scienceroom:
    # Setup ============= 
    hide screen action_menu

    python: 
        location_images = ['school_hallway3']
        location_labels = ['school_hallway3']

        actions = []
        prefix = "school_scienceroom"

        lock_free_roam()

    show screen move
    show screen action

    # Script ============
    scene school_scienceroom with dissolve_fast

    # Free Roam =========
    $ unlock_free_roam()
    call screen location_selector(location_images, location_labels) with dissolve_fast
    
    return

# ====================================================================
# Support Scenes 
# ====================================================================
