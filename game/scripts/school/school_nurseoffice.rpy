label school_nurseoffice:
    scene school_nurseoffice with dissolve_fast
    $ location_images = ['school_nursehall']
    $ location_labels = ['school_nursehall']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return