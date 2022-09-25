## Menu options ##

label nighttime:
    play sound "audio/start_crackle.wav"
    pause 1.0
    play music "audio/night.mp3"

    menu:
        "Who will you set up your bed beside?"
        "Felicien":
            $ Felicien_score += 2

            if day == 1:
                jump night1_Felicien
            elif day == 2:
                jump night2_Felicien
            elif day == 3:
                jump night3_Felicien
            elif day == 4:
                jump night4_Felicien
            elif day == 5:
                jump night5_Felicien
        "Domani":
            $ Domani_score += 2

            if day == 1:
                jump night1_Domani
            elif day == 2:
                jump night2_Domani
            elif day == 3:
                jump night3_Domani
            elif day == 4:
                jump night4_Domani
            elif day == 5:
                jump night5_Domani
        "Kaj":
            $ Kaj_score += 2

            if day == 1:
                jump night1_Kaj
            elif day == 2:
                jump night2_Kaj
            elif day == 3:
                jump night3_Kaj
            elif day == 4:
                jump night4_Kaj
            elif day == 5:
                jump night5_Kaj
        "Val":
            $ Val_score += 2

            if day == 1:
                jump night1_Val
            elif day == 2:
                jump night2_Val
            elif day == 3:
                jump night3_Val
            elif day == 4:
                jump night4_Val
            elif day == 5:
                jump night5_Val
        "Luci":
            $ Luci_score += 2

            if day == 1:
                jump night1_Luci
            elif day == 2:
                jump night2_Luci
            elif day == 3:
                jump night3_Luci
            elif day == 4:
                jump night4_Luci
            elif day == 5:
                jump night5_Luci


## First night ##

label night1:
    # settling in for the night

    scene bg hideout
    with dissolve

    jump nighttime
    
    label night1_Felicien:
        "Felicien night 1"

        jump endNight

    label night1_Domani:
        "Domani night 1"

        jump endNight

    label night1_Kaj:
        "Kaj night 1"

        jump endNight

    label night1_Val:
        "Val night 1"

        jump endNight

    label night1_Luci:
        "Luci night 1"

        jump endNight


## Second night ##

label night2:
    # sleeping on the rooftops and stargazing

    scene bg rooftops
    with dissolve

    jump nighttime
    
    label night2_Felicien:
        "Felicien night 2"

        jump endNight

    label night2_Domani:
        "Domani night 2"

        jump endNight

    label night2_Kaj:
        "Kaj night 2"

        jump endNight

    label night2_Val:
        "Val night 2"

        jump endNight

    label night2_Luci:
        "Luci night 2"

        jump endNight


## Third night ##

label night3:
    # They got a hotel(?) room but you have to share a bed

    scene bg hotel room
    with dissolve

    jump nighttime
    
    label night3_Felicien:
        "Felicien night 3"

        jump endNight

    label night3_Domani:
        "Domani night 3"

        jump endNight

    label night3_Kaj:
        "Kaj night 3"

        jump endNight

    label night3_Val:
        "Val night 3"

        jump endNight

    label night3_Luci:
        "Luci night 3"

        jump endNight


## Fourth night ##

label night4:
    # idk

    scene bg somewhere
    with dissolve

    jump nighttime
    
    label night4_Felicien:
        "Felicien night 4"

        jump endNight

    label night4_Domani:
        "Domani night 4"

        jump endNight

    label night4_Kaj:
        "Kaj night 4"

        jump endNight

    label night4_Val:
        "Val night 4"

        jump endNight

    label night4_Luci:
        "Luci night 4"

        jump endNight


## Fifth night ##

label night5:
    # ?

    scene bg somewhere
    with dissolve

    jump nighttime
    
    label night5_Felicien:
        "Felicien night 5"

        jump endNight

    label night5_Domani:
        "Domani night 5"

        jump endNight

    label night5_Kaj:
        "Kaj night 5"

        jump endNight

    label night5_Val:
        "Val night 5"

        jump endNight

    label night5_Luci:
        "Luci night 5"

        jump endNight


## End nighttime sequence and move to the next day ##

label endNight:
    scene black
    with dissolve

    $ day += 1
    $ partner = 0

    return