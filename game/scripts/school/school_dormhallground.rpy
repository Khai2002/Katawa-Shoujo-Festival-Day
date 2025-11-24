label school_dormhallground:
    scene school_dormhallground with dissolve_fast
    $ location_images = ['school_dormext_full', 'school_dormhallway']
    $ location_labels = ['school_dormext_full', 'school_dormhallway']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return