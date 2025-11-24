label school_stalls2:
    scene school_stalls2 with dissolve_fast
    $ location_images = ['school_gardens']
    $ location_labels = ['school_gardens']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return