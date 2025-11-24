label suburb_roadcenter:
    scene suburb_roadcenter with dissolve_fast
    $ location_images = ['school_road', 'suburb_konbiniext', 'suburb_shanghaiext']
    $ location_labels = ['school_road', 'suburb_konbiniext', 'suburb_shanghaiext']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return