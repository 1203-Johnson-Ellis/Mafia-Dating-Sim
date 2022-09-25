## Variables ##

# Score that is used to determine how much each romance option likes you

default Felicien_score = 0
default Domani_score = 0
default Kaj_score = 0
default Val_score = 0
default Luci_score = 0

default Quinn_score = 0
default Eligio_score = 0
default Elhoeva_score = 0


# Keeping track

default day = 1

default partner = 0
# ^ 1 = Felicien, 2 = Domani, 3 = Kaj, 4 = Val, 5 = Luci


# Day 1 variables

default interrogateBegin_flag = False

default FelicienInterrogated1_flag = False
default FelicienInterrogated2_flag = False
default DomaniInterrogated1_flag = False
default DomaniInterrogated2_flag = False
default KajInterrogated1_flag = False
default KajInterrogated2_flag = False
default LuciInterrogated1_flag = False
default LuciInterrogated2_flag = False

default breakOut_flag = False


# Day 2 variables

default notLingerie = False


# For character portraits

default blushing = False
default blood = True


## Link character portrait images together ##

layeredimage angiolo:
    always "angiolo_base"

    group eyes auto:
        attribute normal default
    
    group eyebrows auto:
        attribute neutral default

    group mouth auto:
        attribute open default

    if blushing:
        "angiolo_blush"


layeredimage kaj:
    group base auto:
        attribute normal default

    group face auto:
        attribute neutral default


layeredimage val:
    always "val_base"

    group eyes auto:
        attribute normal default

    group eyebrows auto:
        attribute bland default

    group mouth auto:
        attribute neutral default

    if blood:
        "val_blood"


layeredimage luci:
    always "luci_base"

    group eyes auto:
        attribute normal default
    
    group eyebrows auto:
        attribute neutral default

    group mouth auto:
        attribute unmoved default


## Trying to figure out darkening character portraits ##

image angiolo dark:
    "angiolo"
    matrixcolor BrightnessMatrix(-0.3)

# define config.speaking_attribute = "speaking"

# image angiolo speaking = At("angiolo", pulse)

# define config.speaking_attribute = "speaking"

# transform pulse:
#     zoom 1.0
#     easein 0.2 zoom 1.02
#     easeout 0.2 zoom 1.0


## Film reel grain ##

image grain:
    "bg grain"
    matrixcolor OpacityMatrix(0.25)
    xalign 1.0
    yalign 1.0
    parallel:
        yzoom 1.0
        pause 1.0
        yzoom 1.3
        pause 0.1
        yzoom 1.75
        pause 4.0
        repeat
    parallel:
        easein 24.0 yzoom 1.5
        repeat
    parallel:
        xzoom 1.0
        pause 3.0
        xzoom 1.5
        pause 0.1
        repeat
    parallel:
        easeout 30.0 xzoom 1.25
        repeat

image reel:
    "bg reel"
    yalign 0.0
    parallel:
        xalign 50.0
        easeout 9.0 xalign -65.0
        pause 3.0
        repeat


# screen film_overlay:
#     show grain
#     show reel
#     play audio "<loop 3.0>audio/projector.mp3"


## Characters ##

define a = Character(_("Angiolo"), image = "angiolo", color = "#b4b4b4")
define f = Character(_("Felicien"), color = "#b4b4b4")
define d = Character(_("Domani"), color = "#b4b4b4")
define k = Character(_("Kaj"), image = "kaj", color = "#b4b4b4")
define v = Character(_("Val"), image = "val", color = "#b4b4b4")
define l = Character(_("Luci"), image = "luci", color = "#b4b4b4")

define q = Character(_("Quinn"), color = "#b4b4b4")
define lig = Character(_("Eligio"), color = "#b4b4b4")
define e = Character(_("Elhoeva"), image = "elhoeva", color = "#b4b4b4")