label day3:
    # choose someone to explore town with

    "explore town"

    menu:
        "Who do you want to ask to go on the town with you?"
        "Felicien":
            jump exploreFelicien
        "Domani":
            jump exploreDomani
        "Kaj":
            jump exploreKaj
        "Val":
            jump exploreVal
        "Luci":
            jump exploreLuci


    label exploreFelicien:
        # if you choose Felicien he leads you on a hunt to eat someone he is hungry he needs a meal before you go....
        $ partner = 1

        show angiolo at left
        show felicien at right

        "Felicien time"

        # Elhoeva confronts you on the way back to the gang
        scene bg alley
        show elhoeva at center

        e "I am here."


    label exploreDomani:
        # go to the grocery store to get cooking/baking ingredients

        show angiolo at left
        show domani at right

        "Domani time"

        scene bg alley
        show elhoeva at center

        e "I am here."


    label exploreKaj:
        show angiolo at left
        show kaj at right

        "Kaj time"

        scene bg alley
        show elhoeva at center

        e "I am here."


    label exploreVal:
        ## WRITE
        show angiolo at left
        show val at right

        "Val time"

        scene bg alley
        show elhoeva at center

        e "I am here."


    label exploreLuci:
        show angiolo at left
        show luci at right
        "Luci time"

        scene bg alley
        show elhoeva at center

        e "I am here."


    label gangMeet:
        # does this if/else statement work

        if partner == 1:
            "Felicien"
        elif Felicien_score >= 5 and partner != 1:
            f "Where the hell have you been?"
            a "Uh, at the store."
            a "We got cooking ingredients."
            f "Cooking ingredients? What a great idea!"
            f "If we had a fucking kitchen. But we don't. We're kitchenless and exposed waiting for {i}you{/i} to get back before we can pick up and leave."
            f "We're escaping from the law, remember? Not going on vacation."
            a "So... Are we going somewhere with a kitchen next, or..."
            f "That's just the question, isn't it?"
            menu:
                "We can find a hotel with a kitchenette.":
                    "dfg"
                "We could stay with the mafia kid.":
                    "dfg"
                "Luci's family? his brother or his father?":
                    "dfg"
                "Val's family?":
                    "dfg"
                "Do you guys want to start up another front?":
                    v "You don't want to flirt or you don't know how?"
                    v "Have you ever flirted in your life?"
                    v "Here, give it a shot. Flirt with me."
                    v "Seems like a golden opportunity if you think I'm so attractive."
                "That's it. I've got nothing else.":
                    "dfg"
        elif Felicien_score < 5 and partner != 1:
            "When you get back to the place on the rooftops where the others had been waiting, there is no one there."

    # Need an individual scene with someone in here somewhere. Probably either Kaj or Domani

    return