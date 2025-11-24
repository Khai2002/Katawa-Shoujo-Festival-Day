# Music
define canon = "audio/Canon In D.ogg"

define afternoon = "bgm/Afternoon.ogg"
define ah_eh_i_oh_you = "bgm/Ah_Eh_I_Oh_You.ogg"
define air_guitar = "bgm/Air_Guitar.ogg"
define aria_de_letoile = "bgm/Aria_de_l'Etoile.ogg"
define breathlessly = "bgm/Breathlessly.ogg"
define caged_heart = "bgm/Caged_Heart.ogg"
define cold_iron = "bgm/Cold_Iron.ogg"
define comfort = "bgm/Comfort.ogg"
define concord = "bgm/Concord.ogg"
define daylight = "bgm/Daylight.ogg"
define ease = "bgm/Ease.ogg"
define everyday_fantasy = "bgm/Everyday_Fantasy.ogg"
define friendship = "bgm/Friendship.ogg"
define flipperies = "bgm/Fripperies.ogg"
define generic_happy_music = "bgm/Generic_Happy_Music.ogg"
define high_tension = "bgm/High_Tension.ogg"
define hokabi = "bgm/Hokabi.ogg"
define innocence = "bgm/Innocence.ogg"
define letting_my_heart_speak = "bgm/Letting_my_Heart_Speak.ogg"
define lullaby_of_open_eyes = "bgm/Lullaby_of_Open_Eyes.ogg"
define moment_of_decision = "bgm/Moment_of_Decision.ogg"
define nocturne = "bgm/Nocturne.ogg"
define out_of_the_loop = "bgm/Out_of_the_Loop.ogg"
define painful_history = "bgm/Painful_History.ogg"
define parity = "bgm/Parity.ogg"
define passing_of_time = "bgm/Passing_of_Time.ogg"
define raindrops_and_puddles = "bgm/Raindrops_and_Puddles.ogg"
define red_velvet = "bgm/Red_Velvet.ogg"
define romance_in_andante_II = "bgm/Romance_in_Andante_II.ogg"
define romance_in_andante = "bgm/Romance_in_Andante.ogg"
define school_days = "bgm/School_Days.ogg"
define shadow_of_the_truth = "bgm/Shadow_of_the_Truth.ogg"
define standing_tall = "bgm/Standing_Tall.ogg"
define stride = "bgm/Stride.ogg"
define the_student_council = "bgm/The_Student_Council.ogg"
define to_become_one = "bgm/To_Become_One.ogg"
define wiosna = "bgm/Wiosna.ogg"
define carefree_days = "bgm/Carefree_Days.ogg"


# SFX
define paper = "sfx/paper.ogg"
define slide = "sfx/slide.ogg"
define slide2 = "sfx/slide2.ogg"
define thunder = "sfx/thunder.ogg"
define alarm = "sfx/alarm.ogg"
define fireworks_sound = "sfx/fireworks.ogg"
define crowd_outdoors = "sfx/crowd_outdoors.ogg"
define crowd_cheer = "sfx/crowd_cheer.ogg"
define carillon = "sfx/carillon.ogg"
define crowd_indoors = "sfx/crowd_indoors.ogg"
define door_open = "sfx/dooropen.ogg"
define watersplash = "sfx/watersplash.ogg"
define switch = "sfx/switch.ogg"

image bg mural_start = "vfx/mural_start.jpg"
image bg mural_unfinished = "vfx/mural_unfinished.jpg"
image bg mural_part = At("vfx/mural.jpg", Transform(xalign=0.0))
image mural all = "vfx/mural_wide.jpg"
image bg mural = "vfx/mural.jpg"
# image bg mural_ss = sunset("vfx/mural.jpg")
# image mural pan = At("vfx/mural.jpg",Fullpan(60.0, dir="left"))

init python:
    delayblinds = ImageDissolve("vfx/tr-delayblinds.png", 1.0)
    delayblindsfade = MultipleTransition([False,delayblinds,Solid("#000"),delayblinds,True])

    shorttimeskip = delayblindsfade


