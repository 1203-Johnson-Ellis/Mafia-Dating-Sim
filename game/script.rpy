label start:
    stop music fadeout 1.0

    ## Game structure ##

    # With each call function, it goes to the label in the corresponding file and runs through the dialogue therein

    # Day 1
    call day1
    call night1

    # Day 2
    call day2
    call night2

    # Day 3
    call day3
    call night3

    # Day 4
    call day4
    call night4

    # Day 5
    call day5
    call night5

    # Then goes to the finale whose label is below
    if day == 6:
        jump finale


    ## Placeholder end screens and score tests ##

    label badEnd:
        play sound "audio/start_crackle.wav"
        pause 1.0
        play music "audio/wretched.mp3"

        "You died"

        return


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


        # (This is the placeholder for the aforementioned scenes)

        label marriage:
            "You have won [winner]'s heart."
            jump marriageChoice

    return