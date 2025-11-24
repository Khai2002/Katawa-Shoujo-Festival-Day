## All characters sprites goes into this file

image lilly_shizu_showdown = "event/lilly_shizu_showdown.jpg"
image saki_canon_big = "event/saki_canon_big.jpg"
image saki_canon = "event/saki_canon.jpg"
image saki_firework = "event/saki_firework.jpg"

image phone = "vfx/mobile-sprite.png"

image thanks = "event/completionbonus-transformed.jpg" 


init 1 python:
    sp_filters = ((sp_sunset,'ss'),
                (sp_night,'ni'),
                (sp_rain,'rn'),
                )
    
    def make_sprite_path(char, expr, suffix='', close=False, alter_name=None):
        
        if suffix:
            suffix = '_' + suffix
        if alter_name:
            char = alter_name
        return 'sprites/' + char + '/' + char + '_' + expr + suffix + '.png'

    
    def ks_sprite(char, expr_name, suffix_list=[], alter_name=None, scale=None, width=None, height=None, x=None, y=None, cropped_width=None, cropped_height=None, close=False):
        if close:
            close_mod = '_close'
        else:
            close_mod = ''

        regular_files = [(make_sprite_path(char,expr_name,alter_name=alter_name),expr_name+close_mod)]

        for suffix in suffix_list:
                regular_files.append((make_sprite_path(char,expr_name, suffix,alter_name=alter_name),expr_name+'_'+suffix+close_mod))
        
        
        for filename, mod_expr_name in regular_files:
            if not renpy.loadable(filename):
                continue
            else:
                checked_filename = filename

            if scale is not None:
                checked_filename = im.FactorScale(checked_filename, width=scale)
            elif width is not None and height is not None:
                checked_filename = im.Scale(checked_filename, width, height)
            
            if all(val is not None for val in [x, y, cropped_width, cropped_height]):
                checked_filename = im.Crop(checked_filename, x, y, cropped_width, cropped_height)

            renpy.image((char, mod_expr_name), checked_filename)

            for filter, filtersuffix in sp_filters:
                renpy.image((char,mod_expr_name+"_"+filtersuffix), filter(checked_filename))

    def make_sprites(char, expr_list, suffix_list=[], alter_name=None, scale=None, width=None, height=None, x=None, y=None, cropped_width=None, cropped_height=None, close=False):
        
        for expr in expr_list:
            ks_sprite(char, expr, suffix_list, alter_name, scale, width, height, x, y, cropped_width, cropped_height, close)
                


init 2 python:

    # Nurse sprites
    nurse_expr_list = [
        'concern', 
        'fabulous', 
        'grin', 
        'neutral'
    ]
    make_sprites('nurse', nurse_expr_list)

    # Mutou sprites
    mutou_expr_list = [
        'irritated', 
        'normal', 
        'smile'
    ] 
    make_sprites('mutou', mutou_expr_list)

    # Lilly sprites
    lilly_expr_list = [
        "basic_ara",
        "basic_cheerful",
        "basic_concerned",
        "basic_displeased",
        "basic_emb",
        "basic_giggle",
        "basic_listen",
        "basic_oops",
        "basic_surprised",
        "basic_weaksmile",
        "basic_planned",
        "basic_smileclosed",
        "basic_pout",
        "basic_smile",
        "basic_sleepy",
        "basic_sad",
        "basic_reminisce"
    ]
    make_sprites('lilly', lilly_expr_list)

    # Meiko sprites
    meiko_expr_list = [
        'smile',
        'happy',
        'worry',
        'wink',
        'serious'
    ]
    make_sprites("meiko", meiko_expr_list)

    # Emi sprites
    emi_expr_list  = [
        "sad_shyblush",
        "sad_shy",
        "sad_pout",
        "sad_grin",
        "sad_grit",
        "sad_depressed",
        "sad_annoyed",
        "sad_angry",
        "excited_sad",
        "excited_smile",
        "excited_joy",
        "excited_proud",
        "excited_laugh",
        "excited_happy",
        "excited_amused",
        "excited_circle",
        "basic_shock",
        "basic_hes",
        "basic_happy",
        "basic_grin",
        "basic_confused",
        "basic_closedsweat",
        "basic_closedhappy",
        "basic_closedgrin",
        "basic_annoyed",
        "basic_concentrate"
    ]
    make_sprites("emi", emi_expr_list)

    # Rin sprites
    rin_expr_list = [
        "basic_absent",
        "basic_amused",
        "basic_awayabsent",
        "basic_crying",
        "basic_deadpan",
        "basic_deadpanamused",
        "basic_deadpancontemplation",
        "basic_deadpandelight",
        "basic_deadpannormal",
        "basic_deadpansurprised",
        "basic_deadpanupset",
        "basic_delight",
        "basic_lucid",
        "basic_sad",
        "basic_surprised",
        "basic_upset",
        "negative_angry",
        "negative_annoyed",
        "negative_confused",
        "negative_disgust",
        "negative_sad",
        "negative_spaciness",
        "negative_worried",
        "relaxed_boredom",
        "relaxed_disgust",
        "relaxed_doubt",
        "relaxed_nonchalant",
        "relaxed_sleepy",
        "relaxed_surprised"
    ]
    make_sprites('rin', rin_expr_list)

    # Shizune sprites
    shizune_expr_list = [
        "no_glasses",
        "cross_wut",
        "cross_rage",
        "cross_rageclosed",
        "cross_angry",
        "behind_smile",
        "behind_sad",
        "behind_frustrated",
        "behind_frown",
        "behind_blank",
        "basic_sparkle",
        "basic_normal",
        "basic_normal2",
        "basic_happy",
        "basic_frown",
        "basic_angry",
        "adjust_smug",
        "adjust_happy",
        "adjust_frown",
        "adjust_angry",
        "adjust_blush"
    ]
    make_sprites('shizune', shizune_expr_list, alter_name='shizu')

    # Misha sprites
    misha_expr_list = [
        "hips_frown",
        "hips_grin",
        "hips_laugh",
        "hips_smile",
        "cross_frown",
        "cross_grin",
        "cross_laugh",
        "cross_smile",
        "perky_smile",
        "perky_sad",
        "perky_confused",
        "sign_confused",
        "sign_smile",
        "sign_sad"
    ]
    make_sprites('misha', misha_expr_list)