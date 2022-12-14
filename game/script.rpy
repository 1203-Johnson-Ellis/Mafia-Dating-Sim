# 1924, stuff is rough in the Kingdom of Italy with the Great War having just ended, increasing violence against anti-Fascists,
# the march on Rome putting the Fascist party into power, now this attack on the mafia beginning.
# Men of honor, Cosa Nostra
# Education and literacy by class

label start:
    stop music fadeout 1.0

    ## Game structure ##

    # With each call function, it goes to the label in the corresponding file and runs through the dialogue therein
    # It also checks afterward whether the player has gotten a bad ending,
    # because otherwise the return statement in the badEnd label just allows the game to continue on to the next day/night.

    # Day 1
    call day1
    if dead == True:
        return

    call night1
    if dead == True:
        return

    # Day 2
    call day2
    if dead == True:
        return

    call night2
    if dead == True:
        return

    # Day 3
    call day3
    if dead == True:
        return

    call night3
    if dead == True:
        return

    # Day 4
    call day4
    if dead == True:
        return

    call night4
    if dead == True:
        return

    # Day 5
    call day5
    if dead == True:
        return

    call night5
    if dead == True:
        return

    # Then goes to the finale whose label is below
    if day == 6:
        jump finale


    ## Placeholder end screens and score tests ##

    # Bad ending screen
    label badEnd:
        $ dead = True

        stop sound
        pause 1.0
        screen black
        with fade
        play sound "audio/start_crackle.wav"
        play music "audio/wretched.mp3"
        "You died"
        #show screen ctc
        #with fade(3.0)

        # figure out how screens work

    return

    # Good end partnership selection
    label finale:
        play sound "audio/start_crackle.wav"
        pause 1.0
        play music "audio/romantic.mp3"

        # Variables

        $ chosen_flag = False

        $ MarryFelicien = False
        $ MarryDomani = False
        $ MarryKaj = False
        $ MarryVal = False
        $ MarryLuci = False

        $ FelicienWedded = False
        $ DomaniWedded = False
        $ KajWedded = False
        $ ValWedded = False
        $ LuciWedded = False


        # Score calculations for determining eligible marriage options

        if Felicien_score == max(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            $ MarryFelicien = True
        if Domani_score == max(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            $ MarryDomani = True
        if Kaj_score == max(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            $ MarryKaj = True
        if Val_score == max(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            $ MarryVal = True
        if Luci_score == max(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            $ MarryLuci = True

        scene black
        with dissolve
        

        "Having spent all this time with this rambunctious gang of criminals, you now wonder..."
        "Have you become particularly attached to any of them?"

        # Choose who to marry
        # (In its final form this should give a scene corresponding to each chosen partner)

        label marriageChoice:
            if chosen_flag == False:
                menu:
                    "My heart calls out to..."
                    "Felicien" if MarryFelicien == True and FelicienWedded == False:
                        $ winner = "Felicien"
                        $ FelicienWedded = True
                        jump marriage
                    "Domani" if MarryDomani == True and DomaniWedded == False:
                        $ winner = "Domani"
                        $ DomaniWedded = True
                        jump marriage
                    "Kaj" if MarryKaj == True and KajWedded == False:
                        $ winner = "Kaj"
                        $ KajWedded = True
                        jump marriage
                    "Val" if MarryVal == True and ValWedded == False:
                        $ winner = "Val"
                        $ ValWedded = True
                        jump marriage
                    "Luci" if MarryLuci == True and LuciWedded == False:
                        $ winner = "Luci"
                        $ LuciWedded = True
                        jump marriage
                    "I'm set":
                        if chosen_flag == False:
                            $ winner = "nobody"
                            $ chosen_flag = True
                            jump marriage
                        else:
                            "Congratulations."
                            return
            else:
                return


        # (This is the placeholder for the aforementioned scenes. winner variable will not be needed in final form)

        label marriage:
            "You have won [winner]'s heart."
            jump marriageChoice

    return