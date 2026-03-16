init python:
    seen_school_stalls2_7h_0 = False

# ====================================================================
# Main scene
# ====================================================================

label school_stalls2:
    # Setup ============= 
    hide screen action_menu

    python:
        location_images = ['school_gardens']
        location_labels = ['school_gardens']
        location_available = [1]

        prefix = "school_stalls2"
        actions = []

        lock_free_roam()


    show screen move
    show screen action

    # Script ============
    if not seen_school_stalls2_7h_0:
        call school_stalls2_7h_0

    scene school_stalls2 with dissolve_fast

    # Free Roam =========
    $ unlock_free_roam()
    call screen location_selector(location_images, location_labels, location_available) with dissolve_fast
    return

# ====================================================================
# Support Scenes 
# ====================================================================

label school_stalls2_7h_0:
    $ seen_school_stalls2_7h_0 = True

    scene school_stalls2 with dissolve_fast

    "The sound of students grows around me as I make my way toward the festival stalls."

    "By the time I reach it, most of the stalls are already in their final stages of preparation." 

    "The path stretches out in a neat line of color. Banners fluttering lightly, tabletops arranged with practiced care, and only a few stray boxes left to unpack."

    "The food stalls are the most active."

    "People move in and out, checking burners, adjusting trays, and organizing ingredients. "

    "Neat rows of candied apples catch the morning light, their glossy red sheen almost too perfect. "

    "The takoyaki stand tests its pans with small sizzles of batter, releasing a hint of warmth and savory aroma that drifts lazily through the cool air. "

    "Someone laughs as a batch comes out oddly shaped, though no one seems bothered; there's still time before the crowds arrive."

    "A short distance away, the literature club is placing the last of their used books on display. The tablecloth flutters as they smooth it out one final time. "

    "They debate the order of the genres, shift a small stack back and forth, and ultimately decide it looks fine as it is."

    "Closer to the corner, the gardening club completes their arrangement of potted plants. Tiny succulents, herbs, and flowers labeled carefully in handwritten tags. "

    "One of the members steps back, hands on hips, and nods with quiet pride before dusting off a bit of soil from the table."

    "Students and teachers weave between the booths, their voices a calm murmur of reminders and quick updates. "

    "Someone tests a microphone. "

    "Someone else drags a ladder back to the storage shed. "

    "The air feels charged, humming with a slow-building energy."

    "Everything is poised, waiting for the festival to truly begin."

    jump school_stalls2