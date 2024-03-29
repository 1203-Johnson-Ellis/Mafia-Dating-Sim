﻿############################################
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

# `jump` does not allow you to return to where you jumped from
# `call` allows you to return to where you jumped from

############################################

label start:
    stop music fadeout 1.0

    ## Game structure ##

    # With each call function, the game goes to the label in the corresponding file and runs through the dialogue therein
    # It also checks afterward whether the player has gotten a bad ending,
    # because otherwise the return statement in the badEnd label just allows the game to continue on to the next day/night.


    ## Day 1 ##
    # Goes to `script-day1.rpy`
    call day1 from _call_day1
    if playerIsDead == True:
        return
        
    #jump demo

    # All night labels are contained in `script-night.rpy`
    call nighttime from _call_nighttime
    if playerIsDead == True:
        return

    ## Day 2 ##
    # Goes to `script-day2.rpy`
    call day2 from _call_day2
    if playerIsDead == True:
        return

    call nighttime from _call_nighttime_1
    if playerIsDead == True:
        return

    ## Day 3 ##
    # Goes to `script-day3.rpy`
    call day3 from _call_day3
    if playerIsDead == True:
        return

    call nighttime from _call_nighttime_2
    if playerIsDead == True:
        return

    ## Day 4 ##
    # Goes to `script-day4.rpy`
    call day4 from _call_day4
    if playerIsDead == True:
        return

    call nighttime from _call_nighttime_3
    if playerIsDead == True:
        return

    ## Day 5 ##
    # Goes to `script-day5.rpy`
    call day5 from _call_day5
    if playerIsDead == True:
        return

    if playerIsDead == False:
        jump finale


    ## PLACEHOLDERS ##

    # Bad ending screen
    label badEnd:
        $ playerIsDead = True

        stop sound
        pause 1.0
        play sound "audio/crackle start.wav"
        play music "audio/bgm/inst wretched.mp3"

        call screen bad_end

        "Hit \"Back\" or open a new save file.\nI'm hoping to replace all bad ends at some point."


    # Good end partnership selection
    # I think I'm getting rid of this system
    label finale:
        play sound "audio/crackle start.wav"
        pause 1.0
        play music "audio/bgm/inst romantic.mp3"

        # Variables

        $ chosen = False

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

        if FScore == max(FScore, DScore, KScore, VScore, LScore):
            $ MarryFelicien = True
        if DScore == max(FScore, DScore, KScore, VScore, LScore):
            $ MarryDomani = True
        if KScore == max(FScore, DScore, KScore, VScore, LScore):
            $ MarryKaj = True
        if VScore == max(FScore, DScore, KScore, VScore, LScore):
            $ MarryVal = True
        if LScore == max(FScore, DScore, KScore, VScore, LScore):
            $ MarryLuci = True

        scene black
        with dissolve
        

        "Having spent all this time with this rambunctious gang of criminals, you now wonder..."
        "Have you become particularly attached to any of them?"

        # Choose who to marry
        # (In its final form this should give a scene corresponding to each chosen partner)

        label marriageChoice:
            if chosen == False:
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
                        if chosen == False:
                            $ winner = "nobody"
                            $ chosen = True
                            jump marriage
            else:
                "Congratulations."
                return


        # (This is the placeholder for the aforementioned scenes. winner variable will not be needed in final form)

        label marriage:
            "You have won [winner]'s heart."
            jump marriageChoice

    return