label school_sportsstoreext:
    scene school_sportsstoreext with dissolve_fast
    $ location_images = ['school_track', 'school_sportsstoreroom']
    $ location_labels = ['school_track', 'school_sportsstoreroom']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return