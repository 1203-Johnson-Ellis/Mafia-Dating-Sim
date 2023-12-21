############################################
### NIGHT ##################################

# Contains all nighttime scenes

# This code should ask who you want to spend the night with,
# then give a description of the area based on what night it is,
# then give a different conversation depending on:
    # 1. Who has been chosen to spend the night with
    # 2. How many times they have been chosen before -OR- what the day counter is

# 2 might depend on the character

############################################


#######################################
### PARTNER DETERMINATION #############
#######################################

# No dialogue in this section
# These labels work together to determine who the partner for the night will be

label nighttime:
    # Because the first night behaves differently from the others, we check for it first
    if day == 1:
        jump night1
    elif day > 1:
        # Then carry out the procedure for the other nights

        play sound "audio/crackle start.wav"
        pause 1.0
        play music "audio/bgm/inst night.mp3"

        # Give a description of the current night

        if day == 2:
            call night2
        elif day == 3:
            call night3
        elif day == 4:
            call night4

        # Get the user's input

        menu:
            "Who will you set up your bed beside tonight?"

            "Felicien":
                $ Felicien_score += 2
                $ Felicien_nights += 1
                $ partner = 1
            #"Domani":
            #    $ Domani_score += 2
            #    $ Domani_nights += 1
            #    $ partner = 2
            #"Kaj":
            #    $ Kaj_score += 2
            #    $ Kaj_nights += 1
            #    $ partner = 3
            #"Val":
            #    $ Val_score += 2
            #    $ Val_nights += 1
            #    $ partner = 4
            #"Luci":
            #    $ Luci_score += 2
            #    $ Luci_nights += 1
            #    $ partner = 5


    label choose_partner:
        # This label uses the `partner` variable to determine which partner the night is being spent with

        if partner == 1:
            call felicien from _call_felicien
        elif partner == 2:
            call domani from _call_domani
        elif partner == 3:
            call kaj from _call_kaj
        elif partner == 4:
            call val from _call_val
        elif partner == 5:
            call luci from _call_luci


    # End nighttime sequence and move to the next day

    label endNight:
        scene black
        with dissolve

        $ day += 1

        # Reset `partner` variable in case it is used elsewhere
        $ partner = 0

        return



    #######################################
    ### SCENES AND DIALOGUE ###############
    #######################################

    # The individual night and character scenes are below


    ## NIGHTTIME DESCRIPTIONS ##
    # Describes the scenery for each night and sets up for ensuing dialogue

    ## First night ##

    label night1:
        scene bg reggio train
        with dissolve

        ########################################
        ## Awoken in the night #################
        ########################################

        # Checking to see who the user has the lowest score with
        # (If there are any ties, it will default to whoever appears first on this list)

        if Felicien_score == min(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            $ partner = 1
            jump felicien.night1
        elif Domani_score == min(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            $ partner = 2
            jump domani.night1
        elif Kaj_score == min(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            $ partner = 3
            jump kaj.night1
        elif Val_score == min(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            $ partner = 4
            jump val.night1
        elif Luci_score == min(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            $ partner = 5
            jump luci.night1
        else:
            # If no lowest score can be determined, it will default to Felicien
            $ partner = 1
            jump felicien.night1

        # These `suspicion` scenes require the user to answer a number of questions in ways the character (chosen above) likes
        # Each time the user does so successfully, their score with that character increases
        # If their score is at a certain threshold by the end of the interrogation, they may continue
        # If it is below this threshold, they receive a bad ending


    ## Second night ##

    label night2:
        # At the farm

        scene bg reggio farm
        with dissolve

        "With everyone settling in for the night, the farm is peaceful as ever. The bustle of the city is far away, leaving room for the cool night air to breeze through the branches of the trees outside."

        return


    ## Third night ##

    label night3:
        # In the city

        scene bg reggio farm
        with dissolve

        "Reggio is a pleasant city. Anyone still out at this hour is on foot, and their chatter echoes off the cobblestone streets. The buildings are dotted with dimly lit windows."

        return


    ## Fourth night ##

    label night4:
        # At the farm again

        scene bg reggio buildings
        with dissolve

        "Isn't this country air getting a little boring? Time to seek out some company to keep you occupied through the night..."

        return


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
            jump .night2
        elif Felicien_nights == 2:
            jump .night3
        elif Felicien_nights == 3:
            jump .night4
        else:
            # This should never happen, but it's coded in for debugging and edge cases
            "uhoh! if you see this then tell ellis that something went wrong in the nighttime counters"

        # Once this night's dialogue is finished, return to `choose_partner` label
        
        label .night1:
            # Felicien roughly does you up in bondage and threatens you at knifepoint. And if you’re good maybe next time you’ll get it

            "felicien is threatening you"

            return
        
        label .night2:
            # Get it. Felicien says ouhhhh I’m sorry I was so evil today, daddy was just a little annoyed about work you understand. Now drink my piss

            "felicien 2"

            return
        
        label .night3:
            # Tells you about killing Kaj. You and Val are his puppies. Will you help me next time~? Threesome

            f "Yeah, don't get too cocky. *Cock* is my job. Yours is *hole*."

            return
        
        label .night4:
            # Kill Domani homoerotically which leads directly into day 5

            "felicien 4"

            return


    #
    ## Domani ##
    #

    label domani:
        # Check how many times this character has been slept with, and call a different scene depending

        if Domani_nights == 1:
            jump .night2
        elif Domani_nights == 2:
            jump .night3
        elif Domani_nights == 3:
            jump .night4
        else:
            "uhoh! if you see this then tell ellis that something went wrong in the nighttime counters"
        
        # Once this night's dialogue is finished, return to `choose_partner` label
        
        label .night1:
            # 

            "domani is threatening you"

            jump endNight
        
        label .night2:
            # 
            
            "domani 2"

            return
        
        label .night3:
            # 
            
            "domani 3"

            return
        
        label .night4:
            # 
            
            "domani 4"

            return


    #
    ## Kaj ##
    #

    label kaj:
        # Check how many times this character has been slept with, and call a different scene depending

        if Kaj_nights == 1:
            jump .night2
        elif Kaj_nights == 2:
            jump .night3
        elif Kaj_nights == 3:
            jump .night4
        else:
            "uhoh! if you see this then tell ellis that something went wrong in the nighttime counters"
        
        # Once this night's dialogue is finished, return to `choose_partner` label
        
        label .night1:
            # 
            
            "kaj is threatening you"

            jump endNight
        
        label .night2:
            # 
            
            "kaj 2"

            return
        
        label .night3:
            # 
            
            "kaj 3"

            return
        
        label .night4:
            # 
            
            "kaj 4"

            return


    #
    ## Val ##
    #

    label val:
        # Check how many times this character has been slept with, and call a different scene depending

        if Val_nights == 1:
            jump .night2
        elif Val_nights == 2:
            jump .night3
        elif Val_nights == 3:
            jump .night4
        else:
            "uhoh! if you see this then tell ellis that something went wrong in the nighttime counters"
        
        # Once this night's dialogue is finished, return to `choose_partner` label
        
        label .night1:
            "You wake with cold steel at your throat."
            v "Easy, now."

            scene bg reggio train
            show val at right
            show angiolo at left
            with dissolve

            a "Come on, man. I thought we were friends?"
            v "Yeah. Thanks for breaking us out. Now I'm going to need a reason not to bleed you out here."

            menu:
                v "Make it a good one. I really wanted to like you. But I'm not stupid."
                "You think I'd rat you out?":
                    v ""
                "Look, I meant it when I said I didn't want to be police anymore.":
                    $ Val_score += 2
                    v ""
                "I want to like you, too. I don't want to see you behind bars.":
                    $ Val_score += 1
                    v ""

            menu:
                "The blade presses hard against your throat."
                "option":
                    $ Val_score += 2
                    v "dialogue"
                "option":
                    v "dialogue"
                "option":
                    $ Val_score += 1
                    v "dialogue"

            menu:
                "Is that a drop of blood you feel dripping down your skin?"
                "option":
                    $ Val_score += 1
                "option":
                    $ Val_score += 0
                "option":
                    $ Val_score += 2

            "Val stares at you in silence, their eyes glinting fiercely in the darkness."

            if Val_score >= 3:
                v "Alright."
                "They release you, bringing the knife away from your neck and vanishing it with a gesture."
                v "You seem like a good guy. You'll forgive me for wanting to check."
                "You can't help but gasp a little, your hand going to feel the small cut left on your throat."
                a "Yeah..."

            elif Val_score < 3:
                "You see them draw the knife in a clean line and see it catching red in the moonlight. You taste blood. You choke on it."
                "But there is no pain."
                v "Can't risk it."

                scene black
                with dissolve
                jump badEnd

            jump endNight
        
        label .night2:
            # 
            
            "val 2"

            return
        
        label .night3:
            # 
            
            "val 3"

            return
        
        label .night4:
            # 
            
            "val 4"

            return


    #
    ## Luci ##
    #

    label luci:
        # Check how many times this character has been slept with, and call a different scene depending

        if Luci_nights == 1:
            jump .night2
        elif Luci_nights == 2:
            jump .night3
        elif Luci_nights == 3:
            jump .night4
        else:
            "uhoh! if you see this then tell ellis that something went wrong in the nighttime counters"
        
        # Once this night's dialogue is finished, return to `choose_partner` label
        
        label .night1:
            # 
            
            "luci is threatening you"

            jump endNight
        
        label .night2:
            # Luci humming and his tits

            l "I'm. Not. Interested. In you."
            a "Damn. Someone else beat me to the punch?"
            l "What?!"
            a "You interested in someone else, I mean?"
            l ".....................................................................................
            ........................................................................................
            ........................................................................................
            ......{w}No."
            a "Well, color me convinced."

            return
        
        label .night3:
            # 
            
            "luci 3"

            return
        
        label .night4:
            # 
            
            "luci 4"

            return