init python:
    seen_school_dormhisao_7h_0 = False

    has_taken_a_bath = False
    has_taken_pills = False
    has_looked_out_the_window = False

    avail_school_dormhallway = True

# ====================================================================
# Main scene
# ====================================================================
label school_dormhisao:
    # Setup ============= 
    hide screen action_menu

    python:
        location_images = ['school_dormhallway']
        location_labels = ['school_dormhallway']
        location_available = [avail_school_dormhallway]

        prefix = "school_dormhisao"
        actions = [
            Action(name="Look out the window", available_fn=lambda: clock_hour == 7 and not has_looked_out_the_window),
            Action(name="Take a bath", available_fn=lambda: clock_hour == 7 and not has_taken_a_bath),
            Action(name="Take my pills", available_fn=lambda: clock_hour == 7 and not has_taken_pills)
            ]

        lock_free_roam()

    show screen move
    show screen action

    # Script ============
    if not seen_school_dormhisao_7h_0: 
        call school_dormhisao_7h_0
    
    scene school_dormhisao with dissolve_fast

    # Free Roam =========
    $ unlock_free_roam()
    call screen location_selector(location_images, location_labels, location_available) with dissolve_fast

    return

# ====================================================================
# Support Scenes 
# ====================================================================

label school_dormhisao_7h_0:
    $ seen_school_dormhisao_7h_0 = True

    scene school_dormhisao_blurred with dissolve

    play music daylight fadein 0.5

    "I'm woken up by the frantic noise of students downstairs."
    
    "It's still early morning, they must be trying to finish up their preparation before the first guests arrive."   

    "I should be down there helping too, but the special privilege of a newly transferred student granted me a pass."

    "The energetic chatters still refuse to cease, only ever mounting in volume."

    "Turning in bed, I wonder whether I should wake up already, or try to sleep in since it's Sunday."

    menu:
        "Wake up":
            call school_dormhisao_7h_0a

        "Sleep in":
            $ update_clock(11, 0)
            call school_dormhisao_11h_0

    jump school_dormhisao

label school_dormhisao_7h_0a:

    scene school_dormhisao with dissolve

    "Gathering all my strength, I plops up on the bed, flinging my blanket to the side."

    "Peering over the window, I see a group of students carrying packs of canned drinks while happily chatting, another one is struggling to move his trolley filled to the brim with confectionaries."
    
    "Another girl in wheelchair is being pushed around by who seems to be her parents, excitedly pointing at various dorm buildings and stalls alike."

    "Wiping my eyes, I ponder what to do today."

    "Unlike me, everybody I 'know' probably have a good idea of what they want to do."

    "Rin is most likely at her mural. Lilly's occupied with her class stall all day long."
    
    "I'm gonna cross Emi sooner or later in the festival. Shizune and Misha are gonna running the whole thing so it shouldn't be that hard to find them either."
    
    "As for Hanako, she's not a festival person. Most likely she'll be in her room or bunker up in the library for some peace and quiet."

    "I might want to do like Hanako. I really don't know if I'm going to enjoy myself at the festival."

    "Whatever it is, I guess I should just get it over with. Morning routine and all."

    jump school_dormhisao

label school_dormhisao_7h_lookOutTheWindow:

    "Leaning against the window frame, I look down at the mess of activity below."
    
    "The courtyard's already packed, students running back and forth with boxes, decorations, and snacks."
    
    "A couple of stalls look almost ready, while others are still half-finished."

    "The group with the canned drinks has now split up, passing them around like it's some kind of treasure."
    
    "The guy with the overloaded trolley is still struggling, every bump threatening to spill half his cargo. The girl in the wheelchair points at one of the food stalls, her parents laughing as they follow her lead."

    "It's lively, even from up here. For a Sunday morning, it feels like the whole school's been flipped upside down."
    
    "I watch for a minute longer, then step back from the window. The festival looks like it's going to be impossible to avoid, no matter what I decide to do."
    
    $ has_looked_out_the_window = True

    call after_action("school_dormhisao")

label school_dormhisao_7h_takeABath:

    "A hot shower sounds like the most reasonable idea I've had all morning."

    "I grab my towel, try not to trip over my own shoes, and step out into the hallway. The air smells faintly of cleaning detergent and… fried dough? The festival's leaking into everything already."

    "The bathroom is mercifully empty. Just the soft buzz of the lights and the distant hum of activity outside."

    "I twist the tap. Water sputters, then evens out into a steady stream of warmth."

    "As I step under it, the world quiets down. My heartbeat settles into something calm and predictable. Steam curls around me, blurring the tiled walls until they look like they belong to some other school entirely."

    "It's strangely comforting. A pause before the festival chaos."

    "By the time I finish and towel off, I feel a little more awake… and a little more like I can handle whatever today throws at me."

    $ has_taken_a_bath = True

    call after_action("school_dormhisao")

label school_dormhisao_7h_takeMyPills:

    "I reach for my medicine on the bedside table, the little bottle feeling strangely heavy in my hand."

    "The pills are small, but swallowing them never feels quite as easy as it should."

    "I take a sip of water, tilt my head back, and let them slide down."

    "Another day, another reminder that my heart isn't as simple as I wish it were."

    "With the medicine taken, I feel a faint sense of relief. It's nothing dramatic, but it's enough to start the day."

    $ has_taken_pills = True
    
    call after_action("school_dormhisao")

label school_dormhisao_11h_0:

    scene school_dormhisao with dissolve

    "I wake up feeling a little lightheaded."
     
    "I wasn't able to sleep soundly, being rudely interrupted every so often by the chattering down the yard."
    
    "I wish they could have been a bit more considerate by not talking too loud this early in the day."
    
    "I say that, but it's already past ten."
    
    "It is probably me who is odd, still refusing to quit my bed even though the festival is already in full swing"

    "Trudging to my desk, I throw back a handful of my morning meds and down them in one go with a gulp of water."
    
    "Now that's taken care of, I ponder how to spend the day."

    "I'm not too keen on being all alone, but haven't made any plans to hang out with anyone today."
    
    "They must all have their friend groups, or busy with their classes' stalls; such is the disappointing truth of a transfer student."
    
    "I struggle to find any reasons to go out."

    menu:
        "At least go out for lunch":
            call school_dormhisao_11h_0a

        "Stay home":
            $ avail_school_dormhallway = False
            call school_dormhisao_11h_0b


    jump school_dormhisao

label school_dormhisao_11h_0a:

    "Then again, it'd be a waste not to join in the festivities downstairs."
    
    "Though it pains me to admit, this whole week has just been me closing myself off to every opportunity to get to know people."
    
    "At this pace, the festival would pass me by yet again."

    "I have to try out some food at least; they'd make for a welcoming change to the bland cafeteria meal."
    
    "Let's go with that!"
    
    "I'll take any reason to get me out of my room at this point."

    jump school_dormhisao

label school_dormhisao_11h_0b:

    "I still have some books that I've been meaning to start. It's a shame that I'd miss out on the festival, but I just want to relax today."
    
    "It's my first Sunday in Yamaku, let's not overdo it."
    
    "I'm not obligated to join in with others, and I should spend the day how I want."

    jump school_dormhisao


# ====================================================================
    