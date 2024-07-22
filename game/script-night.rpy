############################################
### NIGHT ##################################

# Contains all nighttime scenes

# This code should ask who you want to spend the night with,
# then give a description of the area based on what night it is,
# then give a conversation with the partner chosen

############################################


#######################################
### PARTNER DETERMINATION #############
#######################################

# No dialogue in this section
# These labels work together to determine who the partner for the night will be

label nighttime:
    play sound "audio/crackle start.wav"
    pause 1.0
    play music "audio/bgm/inst night.mp3"

    scene bg reggio buildings
    with dissolve

    "Reggio is a pleasant city. Anyone still out at this hour is on foot, and their chatter echoes off the cobblestone streets. The buildings are dotted with dimly lit windows."

    # Get the user's input

    menu:
        "Who will you set up your bed beside tonight?"

        "Felicien":
            $ FScore += 2
            $ partner = 1

        "Domani":
            $ DScore += 2
            $ partner = 2

        "Kaj":
            $ KScore += 2
            $ partner = 3

        "Val":
            $ VScore += 2
            $ partner = 4

        "Luci":
            $ LScore += 2
            $ partner = 5


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

        Felicien: [FScore]
        {p}Domani: [DScore]
        {p}Kaj: [KScore]

        Val: [VScore]
        {p}Luci: [LScore]
        """

        $ day += 1

        return



    #######################################
    ### CHARACTER DIALOGUE ################
    #######################################

    # Contains the dialogue with the character of the user's choice
    # Once the night's dialogue is finished, returns to `choose_partner` label

    #
    ## Felicien ##
    #

    label felicien:
        # Felicien roughly does you up in bondage and threatens you at knifepoint. And if you’re good maybe next time you’ll get it
        # Get it. Felicien says ouhhhh I’m sorry I was so evil today, daddy was just a little annoyed about work you understand. Now drink my piss

        "you walk in on them"
        f "Yeah, don't get too cocky. *Cock* is my job. Yours is *hole*."
        "an dthen have a threesome"

        return


    #
    ## Domani ##
    #

    label domani:
        # 

        "Domani scene"

        return


    #
    ## Kaj ##
    #

    label kaj:
        # 
        
        "kaj 2"

        return


    #
    ## Val ##
    #

    label val:
        # 
        
        a "Hey."
        v "Hey."
        a "I'm bored. These guys kinda suck. Wanna hang out?"
        v "Yeah, sure. What did you have in mind?"
        a "I dunno, we could like-- I found some booze."
        v "Oh, sweet. Come on in."
        "he comes on in and he plops down and pours them drinks"
        a "*sighhhhhhhh* These guys are really tiring, aren't they?"
        v "just starts going off"
        v "something smart about the ferry"
        a "Huh? You know about ferries?"
        "and then they LotR"
        v "*has a swig* blah blhl ahlb lhanalgnbh"
        a "*leans back* Tell me moooore;)"
        menu:
            "make a move":
                "yeah dick sucking"
            "don't":
                v "no moves"

        return


    #
    ## Luci ##
    #

    label luci:
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