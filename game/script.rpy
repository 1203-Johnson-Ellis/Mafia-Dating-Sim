############################################
## HEADER COMMENTS #########################

# Author: Regent
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


    ## Day 1 ##
    # Goes to `script-intro.rpy`
    call day1 from _call_day1
        
    #jump demo

    # All night labels are contained in `script-night.rpy`
    call nighttime from _call_nighttime

    ## Day 2 ##
    # Use partner variable from the previous night to determine which scene to call
    if partner == 1:
        call felicien_route from _call_felicien_route
    elif partner == 2:
        call domani_route from _call_domani_route
    elif partner == 3:
        call kaj_route from _call_kaj_route
    #elif partner == 4:
    #    call val_route from _call_val_route
    elif partner == 5:
        call luci_route from _call_luci_route


    return