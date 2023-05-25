############################################
## DEFINITIONS #############################

# This file defines all variables that have a scope greater than a single label
# This includes integers and booleans, as well as images, screens, and character identifiers
# Should it include screens, considering `screens.rpy`? Probably not

############################################


### VARIABLES ###


## GLOBAL ##

# Score that is used to determine how much each romance option likes you

default Felicien_score = 0
default Domani_score = 0
default Kaj_score = 0
default Val_score = 0
default Luci_score = 0

default Quinn_score = 0
default Eligio_score = 0
default Elhoeva_score = 0


# Check for whether the player has died

default dead = False


# Check for what day it is

default day = 1


# Check for which partner has been selected (used for various purposes)

default partner = 0
# 1 = Felicien, 2 = Domani, 3 = Kaj, 4 = Val, 5 = Luci


# How many nights have you spend with this character?

default Felicien_nights = 0
default Domani_nights = 0
default Kaj_nights = 0
default Val_nights = 0
default Luci_nights = 0



## NON-GLOBAL ##

## Day 1 variables ##

# Determines whether Angiolo has interrogated anyone yet. Used to trigger some flavor text

default interrogateBegin = False


# Determine which questions the user has asked each character. Used to show/hide interrogation options and prevent point grinding

default FelicienInterrogated1 = False
default FelicienInterrogated2 = False
default DomaniInterrogated1 = False
default DomaniInterrogated2 = False
default KajInterrogated1 = False
default KajInterrogated2 = False
default LuciInterrogated1 = False
default LuciInterrogated2 = False

default domaniInterrogated = False


# Determines whether Val has been spoken to, allowing the story to progress

default canBreakout = False


## Day 2 variables ##


## Day 3 variables ##


## Day 4 variables ##


## Day 5 variables ##


# For character portraits
# (I think these don't work for some reason)

default blushing = False
default blood = True



### IMAGES ###

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
    

#layeredimage felicien:
#    always "felicien"


#layeredimage domani:
#    always "domani"


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


#layeredimage elhoeva:
#    always "elhoeva"


## Background images ##

#image venice = "images/backgrounds/bg venice.png"


## Film reel grain ##

image grain:
    "images/backgrounds/bg grain.png"
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



### SCREENS ###

# Bad end

screen bad_end():
    modal True

    frame:
        xalign 0.5
        yalign 0.5

    vbox:
        xsize 1920
        ysize 1080
        add "youdied.jpg" xpos 615 ypos 100
        textbutton "Exit":
            xalign 0.67
            yalign 0
            action Return()


### CHARACTERS ###

# Main characters
define a = Character(_("Angiolo"), image = "angiolo", color = "#cc0000")
define f = Character(_("Felicien"), image = "felicien", color = "#cc0000")
define d = Character(_("Domani"), image = "domani", color = "#cc0000")
define k = Character(_("Kaj"), image = "kaj", color = "#cc0000")
define v = Character(_("Valheo"), image = "val", color = "#cc0000")
define l = Character(_("Luciano"), image = "luci", color = "#cc0000")

# Bonus romance options
define q = Character(_("Quinn"), color = "#b4b4b4")
define lig = Character(_("Eligio"), color = "#b4b4b4")
define el = Character(_("Elhoeva"), image = "elhoeva", color = "#b4b4b4")

# Nice to haves
define boss = Character(_("Big Boss Nails"), color = "#b4b4b4")
define cara = Character(_("Carabiniere"), color = "#b4b4b4")