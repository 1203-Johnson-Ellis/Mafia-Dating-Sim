label day1:
    # Setting the scene

    play audio "<loop 3.0>audio/projector.mp3"
    scene bg questura desk
    show quinn at right
    show angiolo at left
    show grain
    show reel
    with dissolve


    ## Dialogue begins ##

    "You are working at your desk in la Questura di Venizia when the door opens."
    "You look up."
    a "Hey, boss."
    q "Hello, Angiolo. I have a job I'd like you to handle."
    a @ flat "Right..."
    q "We have a handful of eyewitnesses from a shooting today. It was at their establishment, and some of them may be culprits."
    q "To make things messier, said establishment is suspected to be a front for the mafia. Would you interrogate them?"
    a "Whatever you say."
    "He hands you a list of suspects."

    play sound "audio/start_crackle.wav"
    pause 1.0
    play music "audio/rag.mp3" fadeout 1

    label notes:
        scene bg questura desk
        show grain
        show reel
        with fade

        menu:
            "Felicien - Known owner of the establishment; weapons found on his person; uncooperative and rude. Charges: Suspected money laundering, involvement in organized crime" if FelicienInterrogated1_flag == False and FelicienInterrogated2_flag == False:
                jump choice1_Felicien
            "Domani - Refuses to remove his mask. Confessed at the scene of the crime to having fired his guns. Charges: Second degree murder, aggravated assault with a deadly weapon, suspected involvement in organized crime" if DomaniInterrogated1_flag == False and DomaniInterrogated2_flag == False:
                jump choice1_Domani
            "Kaj - Wearing the uniform for the establishment, but was the caller who dialed 1-1-3; therefore likely uninvolved in any criminal activity. Charges: None" if KajInterrogated1_flag == False and KajInterrogated2_flag == False:
                jump choice1_Kaj
            "Valheo - Found in conflict with a customer; weapons found on their person. Injured in the crossfire. Charges: Assault, battery, suspected involvement in organized crime" if breakOut_flag == False:
                jump choice1_Val
            "Luciano - Employee at the establishment; found standing near the suspected source of the conflict. Has largely refused to speak. Charges: Suspected involvement in organized crime" if LuciInterrogated1_flag == False and LuciInterrogated2_flag == False:
                jump choice1_Luci
            "Let's break these poor bastards out of here." if breakOut_flag:
                jump breakOut
            "I actually think I should do my job for once and let these guys go through the system..." if breakOut_flag:
                jump badEnd
    

    ## One-on-one interrogations with each suspect ##

    label choice1_Felicien:
        scene bg questura interrogation
        show angiolo at left
        show felicien at right
        show grain
        show reel
        with dissolve

        "Felicien already has one hand free of his cuffs and is working at the other when you enter. He looks up with a sly smile."
        a "Hey. Looking cozy there."
        "Felicien tosses his head."
        f "Yeah. Fuck you."
        a "Yeowch. Pretty bad day, I guess."
        f "No need to play coy with me."
        a "No, I meant it."
        if interrogateBegin_flag == False:
            "You sit down before him, resting your elbows on your knees."
            $ interrogateBegin_flag = True
        a "I got some questions for you, though, if you feel like answering."
        f "We'll see."

        label interrogate_Felicien:
            menu:
                a "Let's see..."
                "Can you give me a rundown of what happened?":
                    jump interrogate_Felicien1
                "So. You a mob boss?":
                    jump interrogate_Felicien2
                "I think we can wrap this up.":
                    jump interrogate_Felicien3

        label interrogate_Felicien1:
            f "Yeah, my fucking club got shot up by one of my useless employees."
            a "Hum? Any idea why?"
            f "No, I was in the back room doing much more important things. You can't trust Domani with anything, though, he screws up everything he touches somehow."
            a "Pretty big screw-up."
            f "Mmhmm. Who knows what's going on in that thick skull of his?"
            a "Eh, maybe I'll find out."
            f "Do that. My business is suffering because of him."

            $ FelicienInterrogated1_flag = True
            jump interrogate_Felicien

        label interrogate_Felicien2:
            f "Subtle. Is that supposed to scare me?"
            a "Nah. It's a question. My boss wants to know."
            f "And if I say no... will you believe me?"
            if FelicienInterrogated2_flag == False:
                menu:
                    "Yeah. I'll take you at your word.":
                        $ Felicien_score += 1
                        f "So obedient. Very smart."
                        f "I think I like you. Will you be coming back here?"
                        a "I can make time, if you want me to."
                        f "I would like that very much."
                        a "I'll be sure to check in later, then."
                    "Not so much. Seems kind of suspicious, if you ask me.":
                        f "Sounds like you've already made up your mind, carabinier."
                        a "I'm just saying. Can't really ignore the facts."
                        f "You said it yourself. It's been a bad day. I'd advise against making it any worse."
                        a "Woof. There's another one for the case file, I guess."
                        f "..."

            $ FelicienInterrogated2_flag = True
            jump interrogate_Felicien

        label interrogate_Felicien3:
            a "Got anything else for me?"
            f "No."
            a "Well, if anything comes to you..."
            f "I'll give you a call."
            a "Sure thing. Hope your day gets better."

            jump notes

    label choice1_Domani:
        scene bg questura interrogation
        show angiolo at left
        show domani at right
        show grain
        show reel
        with dissolve

        "You enter the interrogation room to a lone figure wearing a fancifully-decorated Venetian mask so that you can't see his face. He looks up with a start."
        if interrogateBegin_flag == False:
            "You sit down before him, resting your elbows on your knees. He seems to cringe away from you."
            $ interrogateBegin_flag = True
        a "Woah, easy there."
        d "I'm sorry, I'm sorry, I did it! I killed them all!"
        "His voice is a tearful young man's. His mask is cool and unfeeling, but he seems to be sobbing behind it."
        a "Yeah, so I've heard. Let's just settle down now."
        d "You caught me, you have who you want, so do anything you like to me! Please... Val, I'm sorry..."
        "Valheo?"
        a "Dude, you didn't kill them. We have them in custody right now. And I don't really have the authority to 'do' anything to you."
        a "I just gotta ask you some questions real quick, 'kay?"
        "Domani sniffles miserably and looks up at you, awaiting his doom."
        
        label interrogate_Domani:
            menu:
                a "Let's see..."
                "Can you give me a rundown of what happened?":
                    jump interrogate_Domani1
                "What's up with the mask?":
                    jump interrogate_Domani2
                "I think we can wrap this up.":
                    jump interrogate_Domani3

        label interrogate_Domani1:
            "You worry he might start bawling again."
            d "I... I..."
            a "Easy..."
            d "...I hated that stupid job!"
            d "Felicien wanted us to do all these sinful things! I've never been so ashamed in my life."
            a "You mind if I ask what things?"
            d "I hardly dare say...! Flirtation, handholding..."
            "He takes a flustered moment."
            d "...And then when it inevitably went wrong, he didn't do a thing about it. So I had to. It's okay if you don't understand. I'm horrible. No one else would..."
            a "...And that's when you shot the place up."
            "He nods, defeated."
            d "Some terrible bloodlust came over me..."
            a "That's okay, we hear that all the time. We'll get it all sorted."

            $ DomaniInterrogated1_flag = True
            jump interrogate_Domani

        label interrogate_Domani2:
            d "Oh, um..."
            a "Just curious, because it's kinda freaking everyone out. Seems like the kind of thing some criminal higher-up would wear. But you seem alright."
            d "No, it's not that..."
            "He sounds embarassed."
            a "Well, that's good. If you were that kind of scary guy, I wouldn't stand a chance."
            d "You still wouldn't, probably."
            a "Ah."
            a "...Glad we got that cleared up."

            $ DomaniInterrogated2_flag = True
            jump interrogate_Domani

        label interrogate_Domani3:
            d "When will I be going to my execution?"
            a "Oh, probably in a week. Maybe two. Things are kinda slow-going around here."
            "He looks down."
            d "...Okay."
            a "Hey, cheer up. You confessed -- counts for something. See you around, maybe."
            jump notes

    label choice1_Kaj:
        scene bg questura interrogation
        show angiolo at left
        show kaj afraid at right
        show kaj hold
        show grain
        show reel
        with dissolve

        "Kaj had been sitting with his head in his hands until you walked in, at which point he jerked up to look at you. He looks wretched."
        k -hold "Hello, Carabiniere..."
        a "Hey."
        if interrogateBegin_flag == False:
            "You sit down before him, resting your elbows on your knees."
            $ interrogateBegin_flag = True
        a "Mind if I ask you some questions? Nothing crazy."
        k "Alright."

        label interrogate_Kaj:
            show kaj normal neutral
            menu:
                a "Let's see..."
                "Can you give me a rundown of what happened?":
                    jump interrogate_Kaj1
                "What do you think of your boss? Felicien, right?":
                    jump interrogate_Kaj2
                "I think we can wrap this up.":
                    jump interrogate_Kaj3

        label interrogate_Kaj1:
            k speaking "I didn't see most of it..."
            k "A customer was getting aggressive. Really aggressive. So I ran to get help?"
            a "Huh."
            a "What were they doing that was aggressive?"
            k -speaking "He was demanding, yelling in Val's face and using violently sexual language. It looked like he could have killed someone, so...I got you all."
            a "Oh. Sounds crazy."
            k "Yeah, especially considering that when I got back he was a corpse."
            a "Damn."
            a "Are your coworkers normally this rambunctious?"
            k unimpressed "Rambunctious?"
            k "...They're weird, but it was that guy that was the danger."
            a @ closed "Mmkay."

            $ KajInterrogated1_flag = True
            jump interrogate_Kaj

        label interrogate_Kaj2:
            k @ startled "Huh? He's fine..?"
            k "No, actually. He's pretentious and mean. Can I ask why?"
            a "My boss thinks he's a mob boss."
            k "...Oh."
            a "..."
            if KajInterrogated2_flag == False:
                a "...Do you want a cigarette?"
                k "Okay."
                "You lean back in your chair and rummage in your pockets for the pack of cigarettes. You hand Kaj one and take one for yourself."
                show kaj dying -normal
                "Once his is lit, Kaj takes one drag and then bursts into a coughing fit."
                menu:
                    "Laugh.":
                        a @ grin "You never smoked before?"
                        k normal angry -dying "No. But with how the day is going, I thought..."
                    "I'm not going to be mean.":
                        $ Kaj_score += 1
                        a "Easy, deep breaths."
                        k hold afraid "*cough cough*... Thanks."
                "His voice rasps. Poor guy."
                "You take a few puffs of your own and check your notes."

                $ KajInterrogated2_flag = True
            jump interrogate_Kaj
            
        label interrogate_Kaj3:
            a "Is there anything else of importance you want me to know?"
            k @ speaking "...No, that's all."
            a "Alright. Thanks for chatting."
            jump notes

    label choice1_Val:
        scene bg questura interrogation
        show angiolo at left
        show val blank at right
        show grain
        show reel
        with dissolve

        "Val is sitting stiffly, looking weary, but their eyes focus on you when you enter."
        a "Long day?"
        v @ upset "You could say that."
        "You cross your legs and take the cigarette from between your lips."
        a "You want anything? We can go on a date or something. I don't much like doing interrogations."
        v @ raised "Is that so? I'd be happy to go out with you somewhere. Beats this. No one's so much as given me laudanum for the bullet in my arm."
        "You shake your head."
        a closed @ shut downturned "Fuckin' animals."
        v "I'll say. Can I have a smoke?"
        "You shrug, pull out your cigarette pack, and frown to yourself."
        a @ upturned -closed "I'm all out..."
        menu:
            "Give them your cigarette?"
            "Yes":
                $ Val_score += 1
                a "Here."
                "You hand your cigarette to Val."
                a @ grin "You deserve one for getting shot and walking it off like this, crazy bastard!"
                "They take it."
                v @ smirk "Thanks. We can go get you more. My treat."
                a @ smile "Hey, nice idea."
            "No":
                a "We can go to the store and get another pack."
                v "Sure."
        a "You ready?"
        v "Don't have much to prepare. Let's go."
        "You open the door to the interrogation room and lead them out of la Questura di Venezia, and into the streets of Venice."

        show bg venice street
        show grain
        show reel
        with dissolve

        "As you walk down the street, you see a vendor at their stall. When they are distracted, a passerby casually grabs one of their items."
        a "Huh. P.S. should do something about that."
        v downturned "You mean, you should do something about that. You're supposed to be Carabinieri."
        a "Yeahh, but I'm trying to get fired."
        v raised "Why's that?"
        a "I just don't like it, really. I'm okay with people doing whatever they want. Seems rather nosey to me to boss people around like that."
        v upset "So...what, that's why you're bringing me out here?"
        a "Well, yeah. If I break you out, I won't be a Carabiniere for much longer, right?"
        v -raised "Is that an offer?"
        "You shrug."
        a closed "Yeah."
        show val -upset
        "They walk in silence for a long time."
        v "I'm inclined to accept, if you cover your ass well enough. Don't want to get into trouble."
        v "And my buddies?"
        a -closed "Oh. Yeah, I can do that."
        v smirk "Cool. If you're looking for another job after, my boss might have something for you."
        v "Let's get you those cigarettes, hm? My coin is yours."
        a @ smile "Okay."
        a "We'll have to head back and pretend I'm working until my coworkers are out, then I can help you guys."
        "You go to the convenience store where Val buys you a new pack of cigarettes, then return to la Questura."

        $ breakOut_flag = True
        jump notes

    label choice1_Luci:
        scene bg questura interrogation
        show angiolo at left
        show luci at right
        show grain
        show reel
        with dissolve

        "Luciano is standing in the interrogation room with his arms folded."
        if interrogateBegin_flag == False:
            "You sit down before him, resting your elbows on your knees."
            $ interrogateBegin_flag = True
        a "Hello."
        l "..."
        a "I'm Angiolo. I'm supposed to come in and interrogate you."
        l "..."

        label interrogate_Luci:
            show luci neutral normal
            menu:
                a "Let's see..."
                "Can you give me a rundown of what happened?":
                    jump interrogate_Luci1
                "Why did you start working at that place?":
                    jump interrogate_Luci2
                "I think we can wrap this up.":
                    jump interrogate_Luci3

        label interrogate_Luci1:
            l "...We were working. And a man came in and demanded that we...did what he saw in porn."
            "You raise your eyebrows."
            a "Then your shop doesn't do that?"
            l downturned "No."
            a "Okay. So, what happened?"
            l @ frown "...The man was getting aggressive. My coworker pulled out a knife."
            l -downturned "...My other coworker pulled out their gun and started shooting."
            a "Huh. Can I ask which coworkers?"
            l "Valheo and Domani."
            "You nod and write in your notes."

            $ LuciInterrogated1_flag = True
            jump interrogate_Luci

        label interrogate_Luci2:
            l downturned angry frown "It seemed like a good fit."
            if LuciInterrogated2_flag == False:
                menu:
                    "Really? Wouldn't have thought so, looking at you.":
                        "..."
                    "Huh. Yeah, you are very pretty. Makes sense.":
                        show luci -downturned -angry -frown
                        $ Luci_score += 1
                        l "..."

                $ LuciInterrogated2_flag = True
            jump interrogate_Luci

        label interrogate_Luci3:
            a "Alright. Be seeing you."
            l "..."
            jump notes


    label breakOut:
        # breaking out of prison

        "You round up the prisoners and lead them out of the Questura."
        "someone" "Where do you think you're taking these prisoners?"
        a "Uh..."
        menu:
            "BAD option":
                "fgd"
                jump badEnd
            "option":
                "fgd"

    "Escape"

    "Val is looking really bad."
    menu:
        "We should get them to a doctor.":
            jump bhospital
        "The military gave me some medical training...":
            jump bandage
        "The best we can do right now is give them some booze.":
            jump booze

    label bhospital:
        "go to the hospital"

    label bandage:
        ## WRITE
        # tending to Val's bullet wound

        "bandage val"
    
    label booze:
        "find some alcohol"

    return