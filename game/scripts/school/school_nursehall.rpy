label school_nursehall:
    scene school_nursehall with dissolve_fast
    $ location_images = ['school_nurseoffice', 'school_courtyard']
    $ location_labels = ['school_nurseoffice', 'school_courtyard']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return