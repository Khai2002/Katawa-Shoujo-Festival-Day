label school_roof:
    scene school_roof with dissolve_fast    
    $ location_images = ['school_staircase1']
    $ location_labels = ['school_staircase1']
    show screen move   

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return