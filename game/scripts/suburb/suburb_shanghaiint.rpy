label suburb_shanghaiint:
    scene suburb_shanghaiint with dissolve_fast
    $ location_images = ['suburb_shanghaiext']
    $ location_labels = ['suburb_shanghaiext']
    show screen move

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return