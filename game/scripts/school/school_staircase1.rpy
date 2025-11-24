label school_staircase1:
    scene school_staircase1 with dissolve_fast
    $ location_images = ['school_hallway3', 'school_roof']
    $ location_labels = ['school_hallway3', 'school_roof']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return