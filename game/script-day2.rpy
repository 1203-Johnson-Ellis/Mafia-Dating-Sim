######################################
### DAY 2 ############################

# Contains all scenes and dialogue for day 2

######################################


label day2:

    ########################################
    ## Awoken in the night #################
    ########################################

    label suspicion:

        # Checking to see who the user has the lowest score with
        # (If there are any ties, it will default to whoever appears first on this list)
        # (If no lowest score can be determined, it will default to Felicien)

        if Felicien_score == min(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            jump Felicien_suspicious
        elif Domani_score == min(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            jump Domani_suspicious
        elif Kaj_score == min(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            jump Kaj_suspicious
        elif Val_score == min(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            jump Val_suspicious
        elif Luci_score == min(Felicien_score, Domani_score, Kaj_score, Val_score, Luci_score):
            jump Luci_suspicious
        else:
            jump Felicien_suspicious
        

        # These `suspicion` scenes require the user to answer a number of questions in ways the character (chosen above) likes
        # Each time the user does so successfully, their score with that character increases
        # If their score is at a certain threshold by the end of the interrogation, they may continue
        # If it is below this threshold, they receive a bad ending


        #
        ## FELICIEN ##
        #

        label Felicien_suspicious:
            "Felicien hates you"

            jump ferry


        #
        ## DOMANI ##
        #
        label Domani_suspicious:
            "Domani hates you"

            jump ferry


        #
        ## KAJ ##
        #

        label Kaj_suspicious:
            "Kaj hates you"

            jump ferry


        #
        ## VAL ##
        #

        label Val_suspicious:
            "You wake with cold steel at your throat."
            v "Easy, now."

            scene bg hideout
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

            jump ferry


        #
        ## LUCI ##
        #

        label Luci_suspicious:
            "Luci hates you"

            jump ferry


    ########################################
    ## FERRY RIDE ##########################
    ########################################

    label ferry:

    # Ferry ride and spin the bottle? Whoever you have the lowest current score with is who you spin.
    # Arrival in Reggio. Some time in the city, monument.
    # Then meet back up and head to the clementine farm
    # Encounter Luci humming alone in his room.

return