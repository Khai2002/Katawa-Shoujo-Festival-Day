label school_hallway3:
    scene school_hallway3 with dissolve_fast    
    $ location_images = ['school_staircase2', 'school_scienceroom', 'school_staircase1']
    $ location_labels = ['school_staircase2', 'school_scienceroom', 'school_staircase1']
    show screen move   

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return