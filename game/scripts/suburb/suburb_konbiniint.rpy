label suburb_konbiniint:
    scene suburb_konbiniint with dissolve_fast
    $ location_images = ['suburb_konbiniext']
    $ location_labels = ['suburb_konbiniext']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return