############################################
## HEADER COMMENTS #########################

# Author: 1203-Johnson-Ellis
# Project: Mafia-Dating-Sim

# A visual novel about dating mafia members in fantasy Sicily

# I hope code readability is okay
# In general, I have attempted to sort out dialogue from the code that makes up the scene flow

############################################
## Notes ###################################

# 1924, stuff is rough in the Kingdom of Italy with the Great War having just ended, increasing violence against anti-Fascists,
# the march on Rome putting the Fascist party into power, now this attack on the mafia beginning.
# Men of honor, Cosa Nostra
# Education and literacy by class

############################################



############################################
### GAME BEGINS ############################

# This file outlines the plot structure day-by-day
# It contains no dialogue itself, only jumps between the files that do contain dialogue

############################################

label start:
    stop music fadeout 1.0

    ## Game structure ##

    # With each call function, the game goes to the label in the corresponding file and runs through the dialogue therein
    # It also checks afterward whether the player has gotten a bad ending,
    # because otherwise the return statement in the badEnd label just allows the game to continue on to the next day/night.


    ## Day 1 ##
    # Goes to `script-day1.rpy`
    call day1
    if dead == True:
        return
        
    jump demo

    # All night labels are contained in `script-night.rpy`
    call nighttime
    if dead == True:
        return

    ## Day 2 ##
    # Goes to `script-day2.rpy`
    call day2
    if dead == True:
        return

    call nighttime
    if dead == True:
        return

    ## Day 3 ##
    # Goes to `script-day3.rpy`
    call day3
    if dead == True:
        return

    call nighttime
    if dead == True:
        return

    ## Day 4 ##
    # Goes to `script-day4.rpy`
    call day4
    if dead == True:
        return

    call nighttime
    if dead == True:
        return

    ## Day 5 ##
    # Goes to `script-day5.rpy`
    call day5
    if dead == True:
        return

    if dead == False:
        jump finale


    ## PLACEHOLDERS ##

    # Bad ending screen
    label badEnd:
        $ dead = True

        stop sound
        pause 1.0
        play sound "audio/crackle start.wav"
        play music "audio/bgm/inst wretched.mp3"

        call screen bad_end

        return
    

    #
    label demo:
        scene black with dissolve
        "Demo done. thank u for playing:)"
        return


    # Good end partnership selection
    label finale:
        play sound "audio/crackle start.wav"
        pause 1.0
        play music "audio/bgm/inst romantic.mp3"

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


        # (This is the placeholder for the aforementioned scenes. winner variable will not be needed in final form)

        label marriage:
            "You have won [winner]'s heart."
            jump marriageChoice

    return