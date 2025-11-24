label school_track_on:
    scene school_track_on with dissolve_fast
    $ location_images = ['school_track']
    $ location_labels = ['school_track']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return