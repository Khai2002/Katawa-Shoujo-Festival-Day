label school_staircase2:
    scene school_staircase2 with dissolve_fast
    $ location_images = ['school_lobby', 'school_hallway2', 'school_hallway3']
    $ location_labels = ['school_lobby', 'school_hallway2', 'school_hallway3']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return