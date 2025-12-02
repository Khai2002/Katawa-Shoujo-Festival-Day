init python:
    seen_school_dormext_full_7h_0 = False

    has_inspected_the_mural = False

# ====================================================================
# Main scene
# ====================================================================
label school_dormext_full:
    # Setup ============= 
    hide screen action_menu

    python:
        location_images = ['school_gardens', 'school_dormhallground', 'school_girlsdormhall']
        location_labels = ['school_gardens', 'school_dormhallground', 'school_girlsdormhall']
        location_available = [1, 1, 0]

        actions = [
            Action(name="Inspect the mural", available_fn=lambda: clock_hour == 7 and not has_inspected_the_mural)
        ]
        prefix = "school_dormext_full"

        lock_free_roam() 
    
    show screen move
    show screen action

    # Script ============
    if not seen_school_dormext_full_7h_0: 
        call school_dormext_full_7h_0

    scene school_dormext_full with dissolve_fast

    # Free Roam =========
    $ unlock_free_roam()
    call screen location_selector(location_images, location_labels, location_available) with dissolve_fast
    
    return


# ====================================================================
# Support Scenes 
# ====================================================================
label school_dormext_full_7h_0:

    $ seen_school_dormext_full_7h_0 = True

    scene school_dormext_full with dissolve
    
    "The moment I step outside, the noise overwhelms me."

    "Students, parents, people I have never seen before, all talking at once, laughing, calling out. It is far livelier than the Yamaku I am used to."
 
    "Stalls are going up, banners flutter, and something metallic clatters on the pavement as someone drops a box."

    "The whole place hums with this charged festival-day buzz."

    "People hurry past, chatting cheerfully, almost too loudly."

    "The contrast hits me as I stop at the stone railing, hands resting on it, watching them like an outsider."

    "It is frustrating."

    "This whole week I have been stuck in my own self-pity, too wrapped up in my problems to look forward to today. It feels undeserved, this bright, busy festival."

    "Without context, it might look like good timing, as if the school arranged all this to welcome me into my new life."
    
    "But it does not feel like a welcome. It feels like a twisting knife."

    "The school is inviting, the people friendly, but I still have not accepted any of it. A part of me is still grieving the life that vanished in a faulty heartbeat."

    "Everything is moving around me."

    "Yet, I am still, and alone."

    "..."

    "This will not do."

    "I draw a deep breath and steady myself."

    "I have missed out, turned down every invitation that came my way. I cannot keep doing that if I expect to have anything resembling a social life here."

    "If I cannot bring myself to take part in something as simple as this festival, then I may as well accept being a permanent recluse."

    "I need to figure out something to do."
    
    "I rub my head, my conscience filled with a kind of thin, ethereal determination that feels as if it might vanish if I stay here too long."

    jump school_dormext_full


label school_dormext_full_7h_inspectTheMural:

    $ has_inspected_the_mural = True

    "As I come down the stairs, I drift toward a small crowd gathered in front of the dorm wall."

    "They are studying Rin's newly finished mural, so I fall in beside them and take a look myself."

    "Before I got a good glance at the mural, I notice a few paint cans sitting on a tarp that has been pushed carelessly to the side, still smelling of turpentine and late-night effort."
    
    "Rin, the architect of all this, is nowhere in sight. She is probably asleep. She must be. "
    
    "Yesterday afternoon half the wall was barely colored in, and now the whole thing stretches from end to end, still radiating the sharp sweetness of drying paint."

    "Knowing her, she finished this under a streetlamp sometime in the small hours."

    scene mural normal with dissolve
    
    "The mural itself is an hodgepodge of human limbs and shapes, repeated again and again, mutating into strange, distorted variations, almost like a body horror. "
    
    "At first glance they look rough, almost tossed onto the wall without thought, but the more I look, the more intention I can see in every awkward curve and smudge."
    
    "The wall is so wide I have to keep turning my head to take it all in. It refuses to settle into a single image. "
    
    "The pieces seem unrelated, yet somehow they hold together, forming something that is definitely a whole, even if I cannot name what that whole is supposed to be."
    
    "I reckon only the artist could explain what is in front of me."
    
    "But it is compelling. And strangely beautiful."

    jump school_dormext_full