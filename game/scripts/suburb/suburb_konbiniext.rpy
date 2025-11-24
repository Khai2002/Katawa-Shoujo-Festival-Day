label suburb_konbiniext:
    scene suburb_konbiniext with dissolve_fast
    $ location_images = ['suburb_roadcenter', 'suburb_konbiniint']
    $ location_labels = ['suburb_roadcenter', 'suburb_konbiniint']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return