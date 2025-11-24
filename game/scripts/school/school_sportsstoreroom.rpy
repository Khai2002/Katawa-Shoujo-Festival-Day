label school_sportsstoreroom:
    scene school_sportsstoreroom with dissolve_fast
    $ location_images = ['school_sportsstoreext']
    $ location_labels = ['school_sportsstoreext']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return