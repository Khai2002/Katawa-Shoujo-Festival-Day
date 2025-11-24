# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Shizune = Character("Shizune", color="#72ADEE", what_suffix='"', what_prefix='"')
define Misha = Character("Misha", color="#FF809F", what_suffix='"', what_prefix='"')
define Hisao = Character("Hisao", color="#629276", what_suffix='"', what_prefix='"')
define Lilly = Character("Lilly", color="#e8e4b5",  what_suffix='"', what_prefix='"')
define Emi = Character("Emi", color="#FF8E7F", what_suffix='"', what_prefix='"')
define Hanako = Character("Hanako", color="#9339c7",  what_suffix='"', what_prefix='"')


# The game starts here.

label start:

    show screen clock_screen
    call school_dormhisao

    return
