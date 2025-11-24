label school_gardens:
    scene school_gardens with dissolve_fast
    $ location_images = ['school_courtyard', 'school_gardens2', 'school_dormext_full', 'school_stalls1', 'school_stalls2']
    $ location_labels = ['school_courtyard', 'school_gardens2', 'school_dormext_full', 'school_stalls1', 'school_stalls2']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return