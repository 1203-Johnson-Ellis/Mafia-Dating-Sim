############################################
### NIGHT ##################################

# Contains all nighttime scenes

# This code should ask who you want to spend the night with, then give a description of the area based on what night it is,
# then give a different conversation depending on:
    # 1. Who has been chosen to sleep beside 
    # 2. How many times they have been chosen before

############################################


#######################################
### PARTNER DETERMINATION #############
#######################################

# No dialogue in this section
# These labels work together to determine who the partner for the night will be

label nighttime:
    play sound "audio/crackle start.wav"
    pause 1.0
    play music "audio/bgm/inst night.mp3"

    # This label gets the user's input

    menu:
        "Who will you set up your bed beside?"

        "Felicien":
            $ Felicien_score += 2
            $ Felicien_nights += 1
            $ partner = 1
        "Domani":
            $ Domani_score += 2
            $ Domani_nights += 1
            $ partner = 2
        "Kaj":
            $ Kaj_score += 2
            $ Kaj_nights += 1
            $ partner = 3
        "Val":
            $ Val_score += 2
            $ Val_nights += 1
            $ partner = 4
        "Luci":
            $ Luci_score += 2
            $ Luci_nights += 1
            $ partner = 5
    
    # It then jumps to a description corresponding to the current night

    if day == 1:
        jump night1
    elif day == 2:
        jump night2
    elif day == 3:
        jump night3
    elif day == 4:
        jump night4
    elif day == 5:
        jump night5


label choose_partner:

    # This label uses the `partner` variable to determine which partner the night is being spent with
    # It is called after the description for the current night has been run through

    if partner == 1:
        call felicien
    elif partner == 2:
        call domani
    elif partner == 3:
        call kaj
    elif partner == 4:
        call val
    elif partner == 5:
        call luci
    
    # Once the partner dialogue has finished, it will return to this label
    # So we end the current day

    jump endNight



#######################################
### SCENES AND DIALOGUE ###############
#######################################

# The individual night and character scenes are below


## NIGHTTIME DESCRIPTIONS ##
# Describes the scenery for each night
# This depends on what day it is

## First night ##

label night1:
    # found an abandoned place for a temp hideout

    scene bg reggio train
    with dissolve

    "night 1"

    jump choose_partner


## Second night ##

label night2:
    # at the farm

    scene bg rooftops
    with dissolve

    "night 2"

    jump choose_partner


## Third night ##

label night3:
    # at the farm again? in the clementine orchard?

    scene bg hotel room
    with dissolve

    "night 3"

    jump choose_partner


## Fourth night ##

label night4:
    # in the city

    #scene bg somewhere
    with dissolve

    "night 4"

    jump choose_partner


## Fifth night ##

label night5:
    # either in or out of jail??

    #scene bg somewhere
    with dissolve

    "night 5"

    jump choose_partner


## CHARACTER DIALOGUE ##
# Dialogue with the character of the user's choice
# This depends on how many nights the user has spent with this character previously

#
## Felicien ##
#

label felicien:

    # Check how many times this character has been slept with, and call a different scene depending
    # Pray, tell me why python doesn't have switch/case
    # This mass of elifs is a nightmare

    if Felicien_nights == 1:
        call felicienNight1
    elif Felicien_nights == 2:
        call felicienNight2
    elif Felicien_nights == 3:
        call felicienNight3
    elif Felicien_nights == 4:
        call felicienNight4
    elif Felicien_nights == 5:
        call felicienNight5
    else:
        # This should never happen, but it's coded in for debugging and edge cases
        "wtf you doing boy?"

    # Once this night's dialogue is finished, return to `choose_partner` label

    return
    
    label felicienNight1:
        "felicien 1"

        return
    
    label felicienNight2:
        "felicien 2"

        return
    
    label felicienNight3:
        "felicien 3"

        return
    
    label felicienNight4:
        "felicien 4"

        return

    label felicienNight5:
        "felicien 5"

        return


#
## Domani ##
#

label domani:

    # Check how many times this character has been slept with, and call a different scene depending

    if Domani_nights == 1:
        call domaniNight1
    elif Domani_nights == 2:
        call domaniNight2
    elif Domani_nights == 3:
        call domaniNight3
    elif Domani_nights == 4:
        call domaniNight4
    elif Domani_nights == 5:
        call domaniNight5
    else:
        "wtf you doing boy?"
    
    # Once this night's dialogue is finished, return to `choose_partner` label

    return
    
    label domaniNight1:
        "domani 1"

        return
    
    label domaniNight2:
        "domani 2"

        return
    
    label domaniNight3:
        "domani 3"

        return
    
    label domaniNight4:
        "domani 4"

        return

    label domaniNight5:
        "domani 5"

        return


#
## Kaj ##
#

label kaj:

    # Check how many times this character has been slept with, and call a different scene depending

    if Kaj_nights == 1:
        call kajNight1
    elif Kaj_nights == 2:
        call kajNight2
    elif Kaj_nights == 3:
        call kajNight3
    elif Kaj_nights == 4:
        call kajNight4
    elif Kaj_nights == 5:
        call kajNight5
    else:
        "wtf you doing boy?"
    
    # Once this night's dialogue is finished, return to `choose_partner` label

    return
    
    label kajNight1:
        "kaj 1"

        return
    
    label kajNight2:
        "kaj 2"

        return
    
    label kajNight3:
        "kaj 3"

        return
    
    label kajNight4:
        "kaj 4"

        return

    label kajNight5:
        "kaj 5"

        return


#
## Val ##
#

label val:

    # Check how many times this character has been slept with, and call a different scene depending

    if Val_nights == 1:
        call valNight1
    elif Val_nights == 2:
        call valNight2
    elif Val_nights == 3:
        call valNight3
    elif Val_nights == 4:
        call valNight4
    elif Val_nights == 5:
        call valNight5
    else:
        "wtf you doing boy?"
    
    # Once this night's dialogue is finished, return to `choose_partner` label

    return
    
    label valNight1:
        "val 1"

        return
    
    label valNight2:
        "val 2"

        return
    
    label valNight3:
        "val 3"

        return
    
    label valNight4:
        "val 4"

        return

    label valNight5:
        "val 5"

        return


#
## Luci ##
#

label luci:

    # Check how many times this character has been slept with, and call a different scene depending

    if Luci_nights == 1:
        call luciNight1
    elif Luci_nights == 2:
        call luciNight2
    elif Luci_nights == 3:
        call luciNight3
    elif Luci_nights == 4:
        call luciNight4
    elif Luci_nights == 5:
        call luciNight5
    else:
        "wtf you doing boy?"
    
    # Once this night's dialogue is finished, return to `choose_partner` label

    return
    
    label luciNight1:
        "luci 1"

        return
    
    label luciNight2:
        "luci 2"

        return
    
    label luciNight3:
        "luci 3"

        return
    
    label luciNight4:
        "luci 4"

        return

    label luciNight5:
        "luci 5"

        return



#######################################
### FINISH ############################
#######################################

# End nighttime sequence and move to the next day

label endNight:
    scene black
    with dissolve

    $ day += 1

    # Reset `partner` variable in case it is used elsewhere
    $ partner = 0

    return