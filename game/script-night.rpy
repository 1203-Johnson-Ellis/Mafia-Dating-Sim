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
            call night2 from _call_night2
        elif day == 3:
            call night3 from _call_night3
        elif day == 4:
            call night4 from _call_night4

        # Get the user's input

        menu:
            "Who will you set up your bed beside tonight?"

            "Felicien":
                $ F_score += 2
                $ F_numNights += 1
                $ partner = 1

            # Since I'm only writing Felicien route,
            # I'm making the other nighttime scenes inaccessible for now

            #"Domani":
            #    $ D_score += 2
            #    $ D_numNights += 1
            #    $ partner = 2

            #"Kaj":
            #    $ K_score += 2
            #    $ K_numNights += 1
            #    $ partner = 3

            #"Val":
            #    $ V_score += 2
            #    $ V_numNights += 1
            #    $ partner = 4

            #"Luci":
            #    $ L_score += 2
            #    $ L_numNights += 1
            #    $ partner = 5


    ## This label uses the `partner` variable to determine which partner the night is being spent with
    label choose_partner:
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


    ## End nighttime sequence and move to the next day

    label endNight:
        scene black
        with dissolve

        # For testing purposes
        """
        - For testing purposes, would you please tell Ellis these are your scores as of day [day] -

        Felicien: [F_score]
        {p}Domani: [D_score]
        {p}Kaj: [K_score]

        Val: [V_score]
        {p}Luci: [L_score]
        """

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
    ## Suspicion
    # This night functions differently from the others
    # The player does not get a choice in who wakes them

    label night1:
        scene bg reggio train
        with dissolve

        # Checking to see who the user has the lowest score with
        # (If there are any ties, it will default to whoever appears first on this list)

        if F_score == min(F_score, D_score, K_score, V_score, L_score):
            $ partner = 1
            jump felicien.night1
        elif D_score == min(F_score, D_score, K_score, V_score, L_score):
            $ partner = 2
            jump domani.night1
        elif K_score == min(F_score, D_score, K_score, V_score, L_score):
            $ partner = 3
            jump kaj.night1
        elif V_score == min(F_score, D_score, K_score, V_score, L_score):
            $ partner = 4
            jump val.night1
        elif L_score == min(F_score, D_score, K_score, V_score, L_score):
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
    # At the farm

    label night2:
        scene bg reggio farm
        with dissolve

        "With everyone settling in for the night, the farm is peaceful as ever. The bustle of the city is far away, leaving room for the cool night air to breeze through the branches of the trees outside."

        return


    ## Third night ##
    # In the city

    label night3:
        scene bg reggio farm
        with dissolve

        "Reggio is a pleasant city. Anyone still out at this hour is on foot, and their chatter echoes off the cobblestone streets. The buildings are dotted with dimly lit windows."

        return


    ## Fourth night ##
    # At the farm again

    label night4:
        scene bg reggio buildings
        with dissolve

        "Isn't this country air getting a little boring? Time to seek out some company to keep you occupied through the night..."

        return


    ## CHARACTER DIALOGUE ##
    # Contains the dialogue with the character of the user's choice
    # Checks how many times this character has been slept with, and calls a different scene depending
    # Once the night's dialogue is finished, returns to `choose_partner` label

    #
    ## Felicien ##
    #

    label felicien:
        # Pray, tell me why python doesn't have switch/case
        # This mass of elifs is a nightmare

        if F_numNights == 1:
            jump .night2
        elif F_numNights == 2:
            jump .night3
        elif F_numNights == 3:
            jump .night4
        else:
            # This should never happen, but it's coded in for debugging and edge cases
            "uhoh! if you see this then tell ellis that something went wrong in the nighttime counters"
        

        ## Dialogue below

        label .night1:
            # Felicien roughly does you up in bondage and threatens you at knifepoint. And if you’re good maybe next time you’ll get it

            "Felicien threat scene"

            return
        
        label .night2:
            # Get it. Felicien says ouhhhh I’m sorry I was so evil today, daddy was just a little annoyed about work you understand. Now drink my piss

            "Felicien Nighttime scene 1"

            return
        
        label .night3:
            # Tells you about killing Kaj. You and Val are his puppies. Will you help me next time~? Threesome

            "Felicien nighttime scene 2"
            #f "Yeah, don't get too cocky. *Cock* is my job. Yours is *hole*."

            return
        
        label .night4:
            # Kill Domani homoerotically which leads directly into day 5

            "Felicien nighttime scene 3"

            return


    #
    ## Domani ##
    #

    label domani:
        if D_numNights == 1:
            jump .night2
        elif D_numNights == 2:
            jump .night3
        elif D_numNights == 3:
            jump .night4
        else:
            "uhoh! if you see this then tell ellis that something went wrong in the nighttime counters"
        

        ## Dialogue below
        
        label .night1:
            # 

            "Domani threat scene"

            jump endNight
        
        label .night2:
            # 
            
            "Domani nighttime scene 1"

            return
        
        label .night3:
            # 
            
            "Domani nighttime scene 2"

            return
        
        label .night4:
            # 
            
            "Domani nighttime scene 3"

            return


    #
    ## Kaj ##
    #

    label kaj:
        if K_numNights == 1:
            jump .night2
        elif K_numNights == 2:
            jump .night3
        elif K_numNights == 3:
            jump .night4
        else:
            "uhoh! if you see this then tell ellis that something went wrong in the nighttime counters"
        

        ## Dialogue below
        
        label .night1:
            # 
            
            "Kaj threat scene"

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
        if V_numNights == 1:
            jump .night2
        elif V_numNights == 2:
            jump .night3
        elif V_numNights == 3:
            jump .night4
        else:
            "uhoh! if you see this then tell ellis that something went wrong in the nighttime counters"
        

        ## Dialogue below
        
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
                    $ V_score += 2
                    v ""
                "I want to like you, too. I don't want to see you behind bars.":
                    $ V_score += 1
                    v ""

            menu:
                "The blade presses hard against your throat."
                "option":
                    $ V_score += 2
                    v "dialogue"
                "option":
                    v "dialogue"
                "option":
                    $ V_score += 1
                    v "dialogue"

            menu:
                "Is that a drop of blood you feel dripping down your skin?"
                "option":
                    $ V_score += 1
                "option":
                    $ V_score += 0
                "option":
                    $ V_score += 2

            "Val stares at you in silence, their eyes glinting fiercely in the darkness."

            if V_score >= 3:
                v "Alright."
                "They release you, bringing the knife away from your neck and vanishing it with a gesture."
                v "You seem like a good guy. You'll forgive me for wanting to check."
                "You can't help but gasp a little, your hand going to feel the small cut left on your throat."
                a "Yeah..."

            elif V_score < 3:
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
        if L_numNights == 1:
            jump .night2
        elif L_numNights == 2:
            jump .night3
        elif L_numNights == 3:
            jump .night4
        else:
            "uhoh! if you see this then tell ellis that something went wrong in the nighttime counters"
        

        ## Dialogue below
        
        label .night1:
            # 
            
            "Luci threat scene"

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