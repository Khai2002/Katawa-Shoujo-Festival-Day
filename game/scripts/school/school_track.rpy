init python:
    avail_school_track = True
    seen_school_track_7h_0 = True
# ====================================================================
# Main scene
# ====================================================================
label school_track:
    # Setup ============= 
    hide screen action_menu

    python: 
        location_images = ['school_courtyard', 'school_track_on', 'school_sportsstoreext']
        location_labels = ['school_courtyard', 'school_track_on', 'school_sportsstoreext']
        location_available = [1, 1, 1]

        prefix = "school_track"
        actions = []

        lock_free_roam()

    show screen move
    show screen action

    # Script ============
    if seen_school_track_7h_0 and clock_hour == 7:
        call school_track_7h_0

    scene school_track with dissolve_fast

    # Free Roam =========
    $ unlock_free_roam()
    call screen location_selector(location_images, location_labels, location_available) with dissolve_fast

    return

# ====================================================================
# Support Scenes 
# ====================================================================
label school_track_7h_0:
    $ seen_school_track_7h_0 = False

    scene school_track with dissolve_fast

    "The faint scent of batter and soy sauce drifts from somewhere, carried by laughter and the metallic clank of poles being set up."
    
    "Yamaku feels different today, louder, busier, like the entire school's heart is beating faster than usual."

    "I tell myself I'm just walking, just seeing how things are coming along. But my feet don't take me toward the main courtyard or the food stalls. They lead me down the slope to the track."

    "And then I see her."

    "Emi is at the center of it all, swiftly moving between students, adjusting banners that keep slipping off the fence."
    
    "Her energy is impossible to ignore; even the sunlight seems to bend toward her. She's got that easy smile again, like she's already having fun before the festival even starts."
    
    "I slow down without realizing it. It's been… what, two days? Three? Since I stopped showing up to morning runs."
    
    "I told myself I was too busy, or too tired, or that my heart couldn't handle it. Maybe all of that's true. Maybe it's just an excuse."

    "Now I'm standing at the edge of the track, trying to look like I have a reason to be here. My stomach tightens. It feels ridiculous. We only ran together for a little while, but somehow the silence that followed feels heavier than it should."

    "Should I approach her, or walk away before she notices?"

    menu:
        "Approach Emi":
            call school_track_7h_0a

        "Walk away":
            call school_track_7h_0b

    jump school_track


label school_track_7h_0a:


    "The air is warm, dry, with a hint of dust kicked up from the track."
    
    "My chest feels tight—not the scary kind. Just nerves. The kind that comes from being stuck halfway between doing something and running away from it."

    "I'm standing here like I have any reason to be staring at the track on festival morning."

    "Emi's voice cuts across the field, bright and fast. She laughs at something one of the younger runners says, then jogs off to grab a roll of tape."

    "Watching her move so easily just reminds me how it felt trying to keep up with her."

    "Every morning she'd look back and grin, and I'd be behind her, trying to convince myself I could keep pace next time."

    "I never did. Eventually I just… stopped going."

    "A breeze pushes at my hair. I realize I'm gripping my wrist, checking my pulse with my thumb. My heart's steady. Fine. I'm fine."

    "She still hasn't noticed me. Maybe that's for the best."

    "I start walking. Slowly."

    "The gravel crunches under my shoes way louder than it should, like the universe wants to announce I'm here."

    "Emi's talking to one of her teammates, pointing at a crate of water bottles. Still no sign she's seen me."

    "I take the long way around the fence so I don't get in the way."

    "When I get closer, she's crouched down, trying to tape a banner that won't stay put."

    "Her hair falls across her cheek as she presses the tape down, humming something under her breath."

    "For a moment I just stop. Watching feels easier than speaking. I almost forget why I came here."

    "And then she looks up. Her eyes land on me."

    Emi "Hisao?"

    "Her tone isn't cold, but it's guarded, surprised."

    Hisao "Hey, Emi. Looks like you've got the track under control."

    "She straightens up, brushing dust off her knees."
    
    Emi "Yeah, someone's gotta make sure everything's ready before the relay starts. Didn't think I'd see you down here today."

    "Her words shouldn't mean anything beyond it, but they sting nontheless. Somehow, I can feel the weight of all the missed mornings hanging between us."

    menu:
        "What should I do?"

        "Ask about track club's festival activity":
            call school_track_7h_1a

        "Apologize for missing practice":
            call school_track_7h_1b

    jump school_track


label school_track_7h_0b:

    "I take a half-step back, then another, letting the bustling track fade behind me."
    
    "My chest feels tight, but not just from the walk, but from the thought of her noticing me. I tell myself I'm just passing by, that maybe it's better this way."

    "The track fades into the distance, laughter and shouted instructions blending into a soft hum."
    
    "Even as I move away, a part of me regrets it."
    
    "I keep telling myself it's fine, that I can come back later, maybe when the chaos dies down. Even though it's only the beginning of the festivity."

    $ avail_school_track = False
    $ update_clock(8, 0)

    jump school_courtyard


label school_track_7h_1a:

    "I clear my throat, trying to keep my voice steady."
    
    Hisao "So… how's the track club doing? Everything ready for the festival?"

    "Emi blinks at me for a moment, then relaxes slightly, letting her posture soften."
    
    Emi "Oh, it's coming along! We're doing a relay race if you don't know. We've got the course marked out, the banners up, drinks ready."
    
    Emi "It's just a lot of little things to make sure no one trips over the tape or anything." 
    
    "She laughs lightly, a sound that's bright enough to make my chest ache a little."

    Emi "And you? You've been… quiet lately."
    
    "Her smile is gentle but pointed, like she's trying not to make me squirm too much, but she's definitely noticing."

    "I shift my weight from one foot to the other, unsure whether to brush past the awkwardness or confront it. The sun beats down lightly on the track, the hum of activity around us making the silence between words feel heavier."

    "Emi crouches to adjust the banner again, then looks back at me."
     
    Emi "Well… if you want, you could, you know, help. Even just a little. I could use a hand carrying some of these water bottles before the relay starts."

    "She's giving me a way in, a way to make up for the mornings I skipped."

    Hisao "Sure, I can help with the water bottles."

    Emi "Great! Thanks, Hisao." 
    
    "She points toward a crate near the far end of the track."
    
    Emi "Those ones over there. Can you just grab and bring them closer to the tables here?"

    "I jog over, feeling my legs complain after my long absence from running. The crate isn't too heavy, but it's enough to remind me how much I've slacked off. Still, the task is simple, and I focus on it. Lift, carry, place. Repeat."

    "Emi moves around the tables with her usual energy, giving directions and occasionally laughing at a teammate's joke. I notice she keeps glancing at me, not in an accusatory way, but to make sure I'm keeping up and not overexerting myself."

    "After a few trips, she jogs over beside me, adjusting her ponytail."
    
    Emi "Not bad, you're handling that pretty well."
    
    "She grins."

    Emi "Maybe those mornings didn't go completely to waste after all."

    "I can't help a small laugh, and my chest feels a little lighter."

    "The last water crate lands beside the table with a dull thud. I wipe the back of my hand across my forehead, breathing out slowly."
    
    "The heat's starting to press down, but there's something satisfying about the simple rhythm. For once, I don't feel completely out of place."

    "Emi steps back to admire the setup."
     
    Emi "Perfect! Thanks a lot, Hisao."

    Hisao "Yeah… figured I could do something useful for once."

    Emi "Well, you did. So thank you."

    menu:
        "What should I do?"
        
        "Mention the mornings I skipped":
            call school_track_8h_0a
        
        "Wish her a good festival":
            call school_track_8h_0b

    jump school_track


label school_track_7h_1b:

    "I rub the back of my neck, eyes dropping for a second before I can meet hers again."

    Hisao "Yeah, about that."

    Hisao "I guess I sort of disappeared. I'm sorry, Emi. I should've at least told you."

    "She blinks, then lets out a sigh."

    Emi "I mean, I kinda figured. I just wish you'd told me instead of vanishing like some kind of morning ghost."

    "There is warmth underneath her words, it is as if she has already forgiven me."

    Hisao "I didn't want to make it a big deal, didn't want to tell you that I was giving up."

    Emi "You still kind of did, though."

    Hisao "Yeah. Guilty."

    "She let the air between us rest for a moment before cheering up to her usual self."
    
    Emi "Well, if you're really sorry, maybe you can make it up to me right now."

    Emi "Consider it penance for flunking out on me."

    Hisao "Sure. What do you need?"

    "She points toward the crate beside her with easily five dozen water bottles stacked inside."
    
    Emi "I need to move this to the relay booth, and I'm short a helper."
    
    Emi "You can handle that, I suppose?"

    "The grin she gives me is pure mischief, and for the first time in weeks, the awkwardness between us actually starts to dissolve."

    "I jog over, feeling my legs complain after my long absence from running. The crate isn't too heavy, but it's enough to remind me how much I've slacked off. Still, the task is simple, and I focus on it. Lift, carry, place. Repeat."

    "Emi moves around the tables with her usual energy, giving directions and occasionally laughing at a teammate's joke. I notice she keeps glancing at me, not in an accusatory way, but to make sure I'm keeping up and not overexerting myself."

    "After a few trips, she jogs over beside me, adjusting her ponytail."
    
    Emi "Not bad, you're handling that pretty well."
    
    "She grins."

    Emi "Maybe those mornings didn't go completely to waste after all."

    "I can't help a small laugh, and my chest feels a little lighter."

    "The last water crate lands beside the table with a dull thud. I wipe the back of my hand across my forehead, breathing out slowly."
    
    "The heat's starting to press down, but there's something satisfying about the simple rhythm. For once, I don't feel completely out of place."

    "Emi steps back to admire the setup."
     
    Emi "Perfect! Thanks a lot, Hisao."

    Hisao "Guess I just needed a task that didn't involve chasing after you."

    "She laughs with that same quick, bright laugh that used to echo across the track in the mornings."

    jump school_track_8h_0a


label school_track_8h_0a:

    $ update_clock(8, 0)

    Hisao "Well, I hope that makes up for me disappearing on practice. Carrying water has to count for something, right?"

    "Emi's smile softens. For a moment, the noise of the festival prep fades into the background. She studies me quietly."

    Emi "You didn't have to make anything up. I figured you had your reasons."
    
    "Her voice is light, but there's a thread of honesty in it."
    
    Emi "Still… I'm glad you came down here."
    
    "Dusting her hands off. She lets out a sigh of relief."

    Emi "Tell you what. Once the race starts, the club's got everything covered. You wanna grab lunch later? The stalls near the main courtyard should be open by then."

    "Her eyes flick toward me, playful but a little shy."
    
    Emi "I'll even let you pick where, as long as it's not something boring, and not too unhealthy."

    Hisao "Yeah. I'd like that."

    "Emi's smile is soft this time, not the blinding kind she flashes on the track, but something quieter."
    
    Emi "Alright then. Lunch it is."

    "She looks toward the field where a few of her teammates are still fussing over banners."
    
    Emi "I've still got a few things to finish here. Meet me by the main courtyard later near the food stalls?"

    Hisao "Yeah, I'll be there."

    "Her eyes meet mine for a moment, and it's enough. A small acknowledgment that the distance between us isn't as wide as it felt this morning."
    
    "She nods once, almost to herself, then turns back to her team."

    "I stand there for a few seconds longer, watching her work. The same energy that once made me feel exhausted just trying to keep up now feels… comforting, somehow."

    jump school_track


label school_track_8h_0b:

    $ update_clock(8, 0)

    "I hesitate, standing there a second too long."
    
    "There's a faint urge in my chest to say more, to tell her I'm sorry for vanishing from our runs, or that I miss the sound of her footsteps pulling me forward. But the words stay stuck somewhere behind my ribs."

    Hisao "Anyway, good luck with the festival, Emi. Hope it goes well."

    "I smile as I bid her goodbye"

    "She gives a small nod, already half-turning back to her work."
    
    Emi "Thanks. You too, Hisao."

    "I start to walk away, my footsteps crunching softly against the gravel path. The track fades behind me, replaced by the distant hum of festival music and laughter rolling in from the school grounds."

    "I glance back once, Emi's already crouched again, taping down another edge of the banner. Same energy as always. Same unshakable focus."

    "I let out a slow breath and keep walking."

    jump school_courtyard

