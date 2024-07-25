############################################
## DEFINITIONS #############################

# This file defines all variables that have a scope greater than a single label
# This includes integers and booleans, as well as images, screens, and character identifiers
# Should it include screens, considering `screens.rpy`? Probably not
# I will want to go through and ensure all declared vars are actually used

############################################


### VARIABLES ###


## GLOBAL ##

# Score that is used to determine how much each romance option likes you
# May remove unless I find use for it in whether certain options appear and stuff

default FScore = 0
default DScore = 0
default KScore = 0
default VScore = 0
default LScore = 0

default QuinnScore = 0
default EligioScore = 0
default ElhoevaScore = 0


# Check for whether the player has died

default playerIsDead = False


# Check for what day it is

default day = 1


# Check for which partner has been selected (used for various purposes)

default partner = 0
# 1 = Felicien, 2 = Domani, 3 = Kaj, 4 = Val, 5 = Luci


# How many nights have you spend with this character?

default FNightsCompleted = 0
default DNightsCompleted = 0
default KNightsCompleted = 0
default VNightsCompleted = 0
default LNightsCompleted = 0


# Inventory

default playerInventory = set()


# Determines what items the player has picked up (even if not currently in inventory)

default FDaggerPickedUp = False
default FDildoPickedUp = False

default DMaskPickedUp = False
default DGunsPickedUp = False

default VKnivesPickedUp = False
default VPhotoPickedUp = False

default LGunPickedUp = False
default LCashPickedUp = False


# Determines what items the player has given back to their owner

default FDaggerReturned = False
default FDildoReturned = False

default DMaskReturned = False
default DGunsReturned = False

default VKnivesReturned = False
default VPhotoReturned = False

default LGunReturned = False
default LCashReturned = False



## NON-GLOBAL ##
# Can these be freed after the day is done?

## -Day 1 variables- ##

# Determines whether Angiolo has interrogated anyone yet. Used to trigger some flavor text

default beganInterrogations = False


# Determines which questions the user has asked each character. Used to show/hide interrogation options and prevent point grinding

default FQ1Asked = False
default FQ2Asked = False

default DQ1Asked = False
default DQ2Asked = False
default DInterrogated = False

default LQ1Asked = False
default LQ2Asked = False


# Determines whether Val has been spoken to, allowing the story to progress

default canBreakout = False


## -Day 2 variables- ##



# For character portraits
# (These don't work for some reason)

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


## Film reel grain ##

# Defines the visuals of the grain

image grain:
    # Image used
    "images/backgrounds/bg grain.png"

    # Opacity
    matrixcolor OpacityMatrix(0.25)

    # Initial placement
    #zorder 10
    # wait why is that commented out it might be extremely convenient
    xalign 1.0
    yalign 1.0

    # Animation
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


# Defines the visuals of the film reel that scrolls past

image reel:
    # Image used
    "bg reel"

    # Initial placement
    #zorder 11
    yalign 0.0

    # Animation
    parallel:
        xalign 50.0
        easeout 9.0 xalign -65.0
        pause 3.0
        repeat



### VARIABLE PORTRAIT SHOWS ###

# Since I can't get the above vars to work

label val_right:
    show val at right


### DIALOGUE ###

# Automation for all dialogue to pause after punctuation
# Will probably want to adjust values to be slower
# I wouldn't think it would be affected by set text speed, but test?

init python:
    def slow_punctuation(str_to_test):
        str_to_test = str_to_test

        # Defines what text should be replaced
        return str_to_test.replace(
            ", ", "{cps=20}, {/cps}").replace( # 2 characters ", " takes 0.1 second
            "... ", "{cps=6}...{/cps} ").replace( # 4 characters "... " takes 0.5 second-ish
            ". ", "{cps=6}. {/cps}").replace( # 2 characters ". " takes 0.3 second-ish
            "? ", "{cps=6}. {/cps} ").replace(
            "! ", "{cps=6}! {/cps} ")
    
    # Automates the text replacement
    config.say_menu_text_filter = slow_punctuation



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