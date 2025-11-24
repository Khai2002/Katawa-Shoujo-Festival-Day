init python:
    seen_school_library_7h_0 = True

# ====================================================================
# Main scene
# ====================================================================
label school_library:
    # Setup ============= 
    python: 
        location_images = ['school_hallway2']
        location_labels = ['school_hallway2']

        actions = [
            Action(name="Browse some books", time_cost=1)
        ]
        prefix = "school_library"

        lock_free_roam()

    show screen move
    show screen action

    # Script ============
    if clock_hour == 7 and seen_school_library_7h_0:
        call school_library_7h_0

    scene school_library with dissolve_fast

    # Free Roam =========
    $ unlock_free_roam()
    call screen location_selector(location_images, location_labels) with dissolve_fast
    return


# ====================================================================
# Support Scenes 
# ====================================================================
label school_library_7h_0:
    $ seen_school_library_7h_0 = False

    scene school_library with dissolve_fast

    "The library feels so different from outside."
    
    "While the festival is starting to buzz, it's still as quiet and comforting as ever in here."
    
    "A nice little refuge when you don't want too much noise."
    
    "Funny thing is, it's completely empty. I guess it's still too early for anyone else to show up."

    "I'm not even sure why I came. Maybe I'm just putting off going downstairs. 
    Everyone's still setting things up, and it'd feel weird to just wander around with nothing to do."

    jump school_library

label school_library_7h_browseSomeBooks:

    "I wander through the shelves, letting my hand trail along the spines without much intent."
    
    "I already have a small stack of borrowed books in my room, but somehow it feels easier to keep looking than to head down to the festival."
    
    "Eventually, a slim fantasy novel from the new arrivals shelf catches my attention. It is short, and the cover looks just interesting enough."
    
    "Enough to pass the time."

    "Book in hand, I make my way toward the back and sink into one of the poufs."
    
    "As I settle in, my eyes drift to the one tucked into the corner nearby."
    
    "That was where Hanako sat the other day, before I startled her off."

    "The cushion still seems pressed down, its fabric sagging ever so slightly, and I find myself wondering if it is because she sat there so often."
    
    "The thought lingers longer than it should, strangely personal, and I shake my head at myself."
    
    "Such a weird thing to think about. Better to focus on the book."

    call after_action("school_library_8h_1")

# Hisao sits in the library reading until 8h. Hanako ran into him
label school_library_8h_1:
    
    "The fantasy novel turns out to be lighter than I expected, the kind of story where kingdoms rise and fall in a few pages, where characters speak in grand declarations instead of real words."
    
    "I lean back into the pouf, letting the text wash over me without much care for detail."
    
    "It is pleasant enough, and more importantly, it keeps me from thinking about the noise outside."

    "The minutes pass easily. My eyes follow the lines, my mind half-drifting with them." 
    
    "Every so often I shift my weight, turning the book slightly to catch the light, settling in deeper as if the cushion might swallow me whole."

    "It is only when I look up, stretching my neck from the page, that I see her."

    "Hanako stands at the edge of the shelves, just far enough back that I almost mistake her for part of the furniture."
    
    "She is frozen in place, shoulders angled toward the door, as though she had already decided to leave before I noticed."

    "The sight jolts me, and the book slips against my thumb. Her head lifts sharply at the sound, and her eyes lock on mine."
    
    "We both startle, like two people caught in the same misstep."

    "For a heartbeat, the air between us feels painfully loud."

    jump school_library
