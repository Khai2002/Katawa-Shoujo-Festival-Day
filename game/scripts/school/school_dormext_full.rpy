label school_dormext_full:
    scene school_dormext_full with dissolve_fast
    $ location_images = ['school_gardens', 'school_dormhallground', 'school_girlsdormhall']
    $ location_labels = ['school_gardens', 'school_dormhallground', 'school_girlsdormhall']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return