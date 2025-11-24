label school_backexit:
    scene school_backexit with dissolve_fast
    $ location_images = ['school_courtyard']
    $ location_labels = ['school_courtyard']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return