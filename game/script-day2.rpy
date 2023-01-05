label day2:

    label suspicion:
        # waking up to be interrogated by whoever trusts you the least

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
        
        label Felicien_suspicious:
            "Felicien hates you"

            jump recovery

        label Domani_suspicious:
            "Domani hates you"

            jump recovery

        label Kaj_suspicious:
            "Kaj hates you"

            jump recovery

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
            jump recovery

        label Luci_suspicious:
            "Luci hates you"

            jump recovery


    label recovery:
        # as in. recovering items
        f "We're going to go get our lingerie back."
        l "No."
        f "I didn't ask. We're going to go steal it etc etc--"
        k "Why steal it? We're already in trouble with the law."
        d "We could buy some more?"
        f "Certainly we could buy more. Since the two of you are so against stealing it, why don't you go and do that?"
        l "We do not {i}need{/i} lingerie. We are being hunted by the carabinieri."

        label recoveryMenu:
            # Domani ends up coming along for both of the first two options
            menu:
                "Steal the lingerie back with Felicien and Val.":
                    a "I think stealing would be more fun."
                    jump lingerieThievery

                "Pick out new lingerie with Luci and Kaj.":
                    a "Yeah, good plan."
                    jump lingerieDressUp

                "Are these my only options?" if notLingerie == False:
                    a "Luci's right. This is stupid."
                    $ Luci_score += 1
                    $ Felicien_score -= 1
                    f "Well, aren't the two of you so bright."
                    $ notLingerie = True
                    jump recoveryMenu

                "Break into the police station" if notLingerie == True:
                    "sdf"
                    # felicien and val go without you
                    jump policeStation

    label lingerieThievery:
        "dialogue"
        jump hunt

    label lingerieDressUp:
        # dress up game

        "You go to the lingerie store."
        

        jump hunt

    label policeStation:
        "dialogue"
        jump hunt

    label hunt:
        # you're going back to the hideout when you get hunted down by your boss

        "Quinn is getting you"
        # chase scene on the canals

        # if he catches you
            # jump badEnd
        # else
        # can choose to hide in the strip club where you meet Eligio
        # or have a close call against a wall with someone's hand over your mouth. I'm thinking Felicien

        # on the run
        v "Sorry, man. This can't be what you thought you were signing up for."

        v "So. You're born into the mafia."
        "They tick off on their fingers."
        v "You don't kill, you don't do the job your boss gives you, you can't help in a medical emergency, and --"
        "They look him up and down."
        v "-- I doubt you could hold your own in a fight. So what're you good for?"

return