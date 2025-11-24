label suburb_shanghaiext:
    scene suburb_shanghaiext with dissolve_fast
    $ location_images = ['suburb_roadcenter', 'suburb_shanghaiint']
    $ location_labels = ['suburb_roadcenter', 'suburb_shanghaiint']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return