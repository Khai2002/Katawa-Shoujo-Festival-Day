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
    
    "The thought lingers longer than it should, strangely personal, and I shake my head."
    
    "Such a weird thing to think about. Better to focus on the book."

    call after_action("school_library_8h_1")

# Hisao sits in the library reading until 8h. Hanako ran into him
label school_library_8h_1:

    with shorttimeskip
    
    "The fantasy novel turns out to be lighter than I expected, the kind of story where kingdoms rise and fall in a few pages, where characters speak in grand declarations instead of real words."
    
    "I lean back into the pouf, letting the text wash over me without much care for detail."
    
    "It is pleasant enough, and more importantly, it keeps me from thinking about the noise outside."

    "The minutes pass easily. My eyes follow the lines, my mind half-drifting with them." 
    
    "Every so often I shift my weight, turning the book slightly to catch the light, settling in deeper as if the cushion might swallow me whole."

    "It is only when I look up, stretching my neck from the page, that I see her."

    "Hanako stands at the edge of the shelves, just far enough back that I almost mistake her for part of the furniture."
    
    "She is frozen in place, shoulders angled toward the door, as though she had already decided to leave before I noticed."

    "The sight jolts me, and the book slips against my thumb. Her head lifts sharply at the sound, and her eyes lock on mine."

    "Hanako is standing completely still, like a deer caught in headlights. I'm not much better."

    "She probably came here to escape all the festival traffic. And of course, I managed to pick the exact same place. It feels like I've intruded on something unspoken."

    "Neither of us says anything. The quiet stretches long enough for the sound of my heartbeat to become uncomfortably loud."

    "I'd better say something."

    "I could ask her to stay and read together, like last time… but that hadn't gone smoothly. Not at all."

        menu:

        "Ask if she wants to join":
            call school_library_8h_1a

        "Offer to leave the place to Hanako":
            call school_library_8h_1b

    jump school_library


label school_library_8h_1a:

    "I close my book gently."

    Hisao "Hey, Hanako. I didn't think I'd see you here today."

    "She glances up for a moment, hesitating."
    
    Hanako "Y… yeah…"

    Hisao "Were you looking for a place to read?"
    
    Hisao "If you want, you can sit here. I don't mind."

    "Hanako hesitates. Her eyes move from me, to the empty pouf. She looks like she's trying to solve a difficult equation with no right answer."

    "Maybe this was the wrong move. I don't want to trap her, but I don't want to make her feel unwelcome either."

    "Hanako's eyes flick downward the moment the words leave her lips."

    Hanako "I... I'll... read somewhere else..."

    "Her voice is tiny, but clear enough."

    "She bows her head slightly, then turns and moves away quietly."

    "I guess that was her answer. Still... I hope I didn't make her too uncomfortable."

    jump school_library


label school_library_8h_1b:

    "I slip a finger between the pages to hold my place and glance up at her."
    
    Hisao "Hey Hanako, I didn't expect to see you here today."
    
    "She hesitates, her words caught somewhere between thought and tongue. I speak again, trying to ease the tension."
    
    Hisao "If you'd rather have the space to yourself, I can move somewhere else."
    
    "I figure she probably didn't come here to chat with someone she barely knows. Knowing her, she wouldn't want to inconvenience me, so maybe it's better if I offer to leave."
    
    "Her eyes widen slightly, surprised at my proposition."
    
    "Her eyes flick up, a trace of surprise in them."
    
    Hanako "N…no… you don't… have to…"
    
    Hisao "It's really okay. The library's big enough. I don't mind moving."
    
    "Her hands tighten slightly on her book."
    
    Hanako "I… I don't… want to make you leave…"
    
    "Her gaze drops, hair slipping forward like a curtain hiding her face. After a moment, she gives a tentative nod."
    
    Hanako "I… I'll… sit… here. If… that's okay."
    
    "She edges closer, careful with each step, settling across from me."
    
    "I can't help the small flutter of surprise. She's actually choosing to stay and share the space with me."
    
    "Part of me wonders if it's just politeness, but I push the thought aside. She could have stepped away entirely, yet she didn't. That alone feels like a quiet reassurance."
    
    "I return to my book, turning the page gently. Out of the corner of my eye, I notice her doing the same."

    "The silence between us settles into something surprisingly comfortable. Hanako sits across from me with her book held close, her shoulders slowly easing as the minutes pass."
    
    "I read a little, glance at her, then return to the page. She does the same, though more cautiously."
    
    "It's peaceful, gentle enough that I'm careful not to break it."

    call school_library_11h_0

    jump school_library


label school_library_11h_0:

    with shorttimeskip
    $ update_clock(11, 0)
    
    "Outside, the hum of the festival rises and falls in distant waves. Time moves softly. Before I know it, the light through the windows has shifted, and my stomach gives a quiet, traitorous grumble."
    
    "Hanako's head lifts slightly. She must have heard it."
    
    Hisao "S-sorry."
    
    "Her fingers pause on her page."
    
    Hanako "Um… it's okay…"
    
    Hisao "It's already noon, huh?"
    
    "Hanako blinks, surprised. She must not have noticed time passing either."
    
    "I close my book, hesitating for a moment before speaking."
    
    Hisao "Would you… like to get lunch? The tea room should be quiet today."

    jump school_library