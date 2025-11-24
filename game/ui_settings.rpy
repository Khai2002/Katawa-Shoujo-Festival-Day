## All setting and transition goes into this file
image fw_blank = Solid("#00000000")
image fw_flash = Solid("#2b2b2b66")
image darkgrey = Solid("#0D0D0D")
image soft = Solid("#F5D4A1")
image thanksBG = Solid("#898989")

define easefromcenter = MoveTransition(0.5, enter=center, enter_time_warp=_warper.easeout)

transform twoleft:
        xpos 300
        yalign 1.0
        ypos 1.0

transform twoleftemi:
        xpos 650
        yalign 1.0
        ypos 1.0
    
transform tworight:
        yalign 1.0
        xpos 1100
        ypos 1.0

transform tworightsaki:
        yalign 1.0
        xpos 950
        ypos 1.0

transform threeleft:
        xpos 100
        yalign 1.0
        ypos 1.0
    
transform threeright:
        yalign 1.0
        xpos 1300
        ypos 1.0

define flash = Fade(.10, 0, .20, color="#b8b0b0")

define openeye = ImageDissolve("vfx/tr_eyes.png", 1.0, 64, ramptype="cube")
define shuteye = ImageDissolve("vfx/tr_eyes.png", 1.0, 64, ramptype="mcube", reverse=True)

define clockwipe = ImageDissolve(im.Tile("vfx/tr-clockwipe.png"), 2.0, 8)
image kslogo heart = "vfx/bt-logolarge-heartonly.png"
image kslogo words = "vfx/bt-logolarge.png"

define delayblinds = ImageDissolve("vfx/tr-delayblinds.png", 1.0)

# Crown Animation

define crowdtrans = Dissolve(0.3, alpha=True)

transform crowdgen(img1, img2, img3):
        img1
        block:
                1.0 
                img2  with crowdtrans 
                1.0 
                img3  with crowdtrans 
                1.0 
                img1  with crowdtrans 
                repeat

image crowd = crowdgen("vfx/crowd1.png","vfx/crowd2.png","vfx/crowd3.png")
image crowd_ss = crowdgen(sunset("vfx/crowd1.png"),sunset("vfx/crowd2.png"),sunset("vfx/crowd3.png"))
image crowd_ni = crowdgen(night("vfx/crowd1.png"),night("vfx/crowd2.png"),night("vfx/crowd3.png"))
image crowd_fb = crowdgen(past("vfx/crowd1.png"),past("vfx/crowd2.png"),past("vfx/crowd3.png"))
image crowd_ni_fb = crowdgen(past_night("vfx/crowd1.png"),past_night("vfx/crowd2.png"),past_night("vfx/crowd3.png"))

init python:

        def night(img_in):
                return im.MatrixColor(img_in, im.matrix.tint(0.6, 0.6, 0.7) * im.matrix.saturation(0.6))

        def sp_night(img_in):
                return im.MatrixColor(img_in, im.matrix.tint(0.9, 0.92, 1.0) * im.matrix.brightness(-0.05))

        def sunset(img_in):
                return im.MatrixColor(img_in, im.matrix.tint(1.1, 0.95, 0.85) * im.matrix.brightness(0.1) * im.matrix.saturation(1.2))

        def sp_sunset(img_in):
                return im.MatrixColor(img_in, im.matrix.tint(1.02, 0.95, 0.9) * im.matrix.brightness(0.05) * im.matrix.saturation(1.1))

        def past(img_in):
                return im.MatrixColor(img_in, im.matrix.saturation(0.15) * im.matrix.tint(1.0, .94, .76))

        def rain(img_in):
                return im.MatrixColor(img_in, im.matrix.saturation(0.4) * im.matrix.tint(0.95, 0.95, 1.0) * im.matrix.brightness(-0.1))

        def sp_rain(img_in):
                return im.MatrixColor(img_in, im.matrix.saturation(0.6) * im.matrix.tint(0.96, 0.96, 1.0) * im.matrix.brightness(-0.05))

        def past_night(img_in):
                return im.MatrixColor(img_in, im.matrix.tint(0.6, 0.6, 0.7) * im.matrix.saturation(0.6) * im.matrix.saturation(0.15) * im.matrix.tint(1.0, .94, .76))


define fw_dis_fast = Dissolve(0.04, alpha=True)
define fw_dis_medium = Dissolve(0.2, alpha=True)
define fw_dis_slow = Dissolve(3.0, alpha=True)
define fw_sparkle_out = ImageDissolve(im.Tile("vfx/tr-pronoise.png"), 3.0, 32, alpha=True)

transform fw_constructor(my_image):
        "fw_blank" 
        choice 15:
                0.2 
        choice:
                "fw_flash"  with fw_dis_fast 
                0.2 
        choice:
                my_image  with fw_dis_medium 
                "fw_blank"  with fw_dis_slow 
                6.0 
        choice:
                my_image  with fw_dis_medium 
                "fw_blank"  with fw_sparkle_out 
                6.0 
        repeat



image fireworks = LiveComposite((1920, 1080),
(0,0), fw_constructor("vfx/fw1.png"),
(0,0), fw_constructor("vfx/fw2.png"),
(0,0), fw_constructor("vfx/fw3.png"),
(0,0), fw_constructor("vfx/fw4.png"),
(0,0), fw_constructor("vfx/fw5.png"),
(0,0), fw_constructor("vfx/fw6.png"),
(0,0), fw_constructor("vfx/fw7.png"),
(0,0), fw_constructor("vfx/fw8.png"),
(0,0), fw_constructor("vfx/fw9.png"))

transform fw_constructor_nosparkle(my_image):
        "fw_blank" 
        choice 15:
                0.2 
        choice:
                "fw_flash"  with fw_dis_fast 
                0.2 
                my_image  with fw_dis_medium 
                "fw_blank"  with fw_dis_slow 
                6.0 
        repeat