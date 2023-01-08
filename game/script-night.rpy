# This code should ask who you want to spend the night with, then give a description of the area based on what night it is,
# then give a different conversation depending on who has been chosen to sleep beside as well as how many times they have been chosen before

## Menu options ##

label nighttime:
    play sound "audio/start_crackle.wav"
    pause 1.0
    play music "audio/night.mp3"

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


## First night ##

label night1:
    # found an abandoned place for a temp hideout

    scene bg hideout
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

    scene bg somewhere
    with dissolve

    "night 4"

    jump choose_partner


## Fifth night ##

label night5:
    # either in or out of jail??

    scene bg somewhere
    with dissolve

    "night 5"

    jump choose_partner


label choose_partner:
    # Decide which partner the night is being spent with
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
    
    # Once it runs through the dialogue, it should end the current day
    jump endNight


## Character dialogue ##

label felicien:
    # Decide which night it is
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

label domani:
    # Decide which night it is
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

label kaj:
    # Decide which night it is
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

label val:
    # Decide which night it is
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

label luci:
    # Decide which night it is
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


## End nighttime sequence and move to the next day ##

label endNight:
    scene black
    with dissolve

    $ day += 1
    $ partner = 0

    return