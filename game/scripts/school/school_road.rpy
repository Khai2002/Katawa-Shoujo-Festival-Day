label school_road:
    scene school_road with dissolve_fast    
    $ location_images = ['school_gate', 'suburb_roadcenter']
    $ location_labels = ['school_gate', 'suburb_roadcenter']
    show screen move   

    call screen location_selector(location_images, location_labels) with dissolve_fast
    return