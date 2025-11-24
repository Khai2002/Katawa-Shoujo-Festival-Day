label school_miyagi:
    scene school_miyagi with dissolve_fast    
    $ location_images = ['school_hallway2']
    $ location_labels = ['school_hallway2']
    show screen move   

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return