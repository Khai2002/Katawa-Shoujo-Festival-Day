label school_council:
    scene school_council with dissolve_fast
    $ location_images = ['school_lobby']
    $ location_labels = ['school_lobby']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return