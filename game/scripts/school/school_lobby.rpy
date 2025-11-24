label school_lobby:
    scene school_lobby with dissolve_fast    
    $ location_images = ['school_courtyard', 'school_cafeteria', 'school_council', 'school_staircase2']
    $ location_labels = ['school_courtyard', 'school_cafeteria', 'school_council', 'school_staircase2']
    show screen move   

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return