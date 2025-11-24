label school_hallway2:
    scene school_hallway2 with dissolve_fast    
    $ location_images = ['school_staircase2', 'school_library', 'school_miyagi']
    $ location_labels = ['school_staircase2', 'school_library', 'school_miyagi']
    show screen move   

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return