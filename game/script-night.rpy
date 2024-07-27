############################################
### NIGHT ##################################

# Contains all nighttime scenes

# This code should ask who you want to spend the night with,
# then give a conversation with the chosen partner

############################################


#######################################
### PARTNER DETERMINATION #############
#######################################

# Player decides who the partner for the night will be

label nighttime:
    play sound "audio/crackle start.wav"
    pause 1.0
    play music "audio/bgm/inst night.mp3"

    scene bg reggio buildings
    with dissolve

    "Reggio is a pleasant city. Anyone still out at this hour is on foot, and their chatter echoes off the cobblestone streets. The buildings are dotted with dimly lit windows."
    """
    Felicien said something halfhearted about fighting over it before disappearing off with Val, but neither Kaj nor Domani had the balls to do anything when Luci claimed the room for his own.
    """

    # Get the user's input and jump to the corresponding conversation
    # Afterward, it will then return here and move forth to the endNight label

    menu:
        "Who will you set up your bed beside tonight?"

        "Felicien":
            $ FScore += 2
            $ partner = 1
            call felicien_night from _call_felicien_night

        "Domani":
            $ DScore += 2
            $ partner = 2
            call domani_night from _call_domani_night

        "Kaj":
            $ KScore += 2
            $ partner = 3
            call kaj_night from _call_kaj_night

        #"Val":
        #    $ VScore += 2
        #    $ partner = 4

        "Luci":
            $ LScore += 2
            $ partner = 5
            call luci_night from _call_luci_night


    ## End nighttime sequence and move to the next day

    label endNight:
        scene black
        with dissolve

        # For testing purposes
        #"""
        #- For testing purposes, would you please tell Ellis these are your scores as of day [day] -

        #Felicien: [FScore]
        #{p}Domani: [DScore]
        #{p}Kaj: [KScore]

        #Val: [VScore]
        #{p}Luci: [LScore]
        #"""

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

    label felicien_night:
        # Felicien roughly does you up in bondage and threatens you at knifepoint. And if you’re good maybe next time you’ll get it

        "As you approach the door, you hear a voice from the other side."
        v "Some smartass line"
        f "Yeah, don't get too cocky. *Cock* is my job. Yours is *hole*."
        """
        Oh my god. Are we about to walk in on them right now?

        You open the door.

        Oh my god. Felicien has his pretty pink strap-on in Val's ass. They have a blindfold on and a chain around their neck that he's tugging on.
        
        Felicien jerks her head up and stares piercingly at you. Then he carefully pulls out and arranges himself to sit neatly on the side of the bed.
        """
        f "Wanna join?"
        a "... Hell yeah, I do."
        "He gestures you into the room, and you shut the door behind you. You come over to the bed."
        # show image
        f "Kneel."
        "You kneel at her feet. He towers over you, all with that toy at attention."
        "She stands and struts around behind you where you can't see, but you hear him rummaging around."
        a "Yowch!"
        "She's roughly tying your arms together with thick leather straps."
        f "If you want to be my bitch so bad, you'll shut the fuck up."
        """
        When he's satisfied, he comes back into your field of view, dragging Val along by their chain. She jerks your head up in her hand and holds it there so you're forced to look into her face.
        """
        f "My obedient little puppies. You'll do whatever I say, won't you?"
        "Val is nodding. You follow suit, and even bark your agreement."
        "He smiles at you and pats your head."
        f "Good doggy. Now, stand up."
        """
        You do. She traces her long-nailed finger down your shirt, directly to your rising boner, and the hesitation lasts an eternity.

        That's when he wrenches your pants down in one motion, unleashing your own throbbing dick.

        Then, she goes in between the two of you, takes Val's hips in her long-fingered hands, and shoves her dick back into their ass.
        """
        f "Come, mutt."
        "You go behind him. Her ass is magnificent, perfectly round. You feel his pussy with a finger, and it comes away utterly dry. She growls."
        f "Don't waste my fucking time. Put it in."
        """
        You put it in. He refuses to let you do any of the work, instead demanding you hold still while she thrusts into Val and then back against you.

        You can't help it. You sqiurm and pant, and his pussy gets moist and then wet as she works into you. Completely delicious.

        She cums into Val's ass, and then immediately turns and swats you away.
        """
        f "Alright, dipshit, it's time to sleep."
        "Good fucking god. He's hot as hell, and it was that easy to get in his pants."

        return


    #
    ## Domani ##
    #

    label domani_night:
        # This scene might have innuendos but is sexless
        # Maybe one version for if you returned his mask and another if you didn't

        "Domani scene"
        # If you returned it you get a touching scene where he reveals himself to you in all his flaws

        # If you didn't you get a scene about setting boundaries and allow him to keep his mask on forever

        return


    #
    ## Kaj ##
    #

    label kaj_night:
        # This scene is sexless and sex-repulsed forsure
        # Bonding about wanting something more... not wanting to be tied down to this stuff.....
        
        "Kaj scene"

        return


    #
    ## Val ##
    #

    label val_night:
        # Might cut this since they get the bullet hole sex scene?
        # And then no Val route since idk what to do for it anyway
        
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

    label luci_night:
        # This will need rewriting and editing

        """
        As you approach, you think you hear his voice from the other side. It sounds... like he's singing?

        You carefully open the door -- don't want him yelling at you -- and poke your head in.
        """
        # show image
        """
        Wowza!!

        Okay, he's super hot. You think about shutting the door again, but he's humming that tune, and the moonlight on his tits is positively drool-worthy.

        Something's weird, all this is making you heady, but you couldn't care less. It's hot.

        He looks up. Fuck.
        """
        l "BLUSHING."
        l "GET. OUT>."
        a "Woah! Sorry!! I'm just, admiring-"
        "He tosses a shirt on in one smooth motion, comes over, and slams the door in your face."
        "..."

        "Knock knock knock ..."
        a "Um, heeyy, I was just looking for somewhere to sleep..."
        l "I'm. Not. Interested. In you."
        a "Damn. Someone else beat me to the punch?"
        l "What?!"
        a "You interested in someone else, I mean?"
        l ".....................................................................................
        ........................................................................................
        ........................................................................................
        ......{w}No."
        a "Really? Anyone I know?"
        l "No!"
        "He huffs."
        l "It is not your business. Leave."
        a "Look, I don't wanna be out in the open now that I'm on the run, and Felicien is occupied. This is my only other option."
        l "..."
        l "... Get your bedding."
        a "I don't have any."
        l "..."
        "The silence sounds pained."
        "The door swings open. He's already got his back to you, walking away toward the bed. He's now wearing some skimpy, slutty little pajamas."
        "He sits stiffly on the bed, arms folded. He's always like a tense little box, taking up no more space than necessary."
        l "You will have one pillow and one bedsheet on the floor. And you will Stay there."
        a "Can do, mister."
        "He hands you down your bedding and you get all arranged and stuff."
        """
        And then it's nighttime and you stay up and talk to him about stuff. ??? I guess about his backstory maybe unless that's better left to subtext

        Maybe not about his exile but about his family home life and how he grew up and stuff
        
        Or maybe he'd rather talk about the present situation instead
        
        Like what he expects to happen next and then things will go way off the rails tomorrow and he'll be shocked and angry and you can work together to bring things back on track
        
        He's like 'we will simply go and lay low for a while until the polizia are off my father's back'
        
        That is not a conversation.
        
        You are so logical and straightforward Luci. Why are you so hot what's that about
        
        My family ... breeds with sirens. So we're magic.
        """

        return