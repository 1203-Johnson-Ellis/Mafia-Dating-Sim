######################################
### DAY 1 ############################

# Contains all scenes and dialogue for day 1
# + Interrogations, character introductions, breaking out of prison
# + Calling the big boss
# + Quinn chase scene
# + Catching the train to Messina
# + Patch up Val's bullet wound

######################################


label day1:

    ########################################
    # Setting the scene ####################
    ########################################

    play audio "<loop 3.0>audio/projector.mp3"

    scene bg questura desk
    show angiolo at left
    with dissolve

    show grain
    show reel


    ## Dialogue begins ##

    """
    Palermo: a beautiful coastal city in Sicily, where cycling tourists and playing children alike can go outside and enjoy the sun.

    Unfortunately, the place is also overrun by illicit activities. People whisper it in the streets - {i}cosa nostra{/i}.
    
    And because you are an idiot, you are in the middle of it all, in a Carabinieri Comando Stazione.
    
    You are working at your desk, eyes glazing over endless piles of paperwork, when the door opens.{p}You look up.
    """
    a "Hey, boss."
    show quinn at right behind grain, reel with dissolve
    q "Hello, Angiolo. I have a job I'd like you to handle."
    a @ flat "Right..."
    q "We have a handful of eyewitnesses from a shooting today. It was at their establishment, and some of them may be culprits."
    q "To make things messier, said establishment is suspected to be a front for the mafia. Would you interrogate them?"
    a "Whatever you say."
    "He hands you a list of suspects."


    # Begin background music

    play sound "audio/crackle start.wav"
    pause 1.0
    play music "audio/bgm/inst rag.mp3" fadeout 1


    # Display the option to interrogate someone
    # (In a perfect world, the screen here will be notebook paper. For now it's Ren'py default)

    label notes:

        # Reset the scene in case user is returning from an interrogation

        scene bg questura desk with fade
        show grain
        show reel

        # Options

        menu:
            "Felicien - Known owner of the establishment; weapons found on his person; uncooperative.\nCharges: Suspected money laundering, involvement in organized crime" if (FelicienInterrogated1 == False and FelicienInterrogated2 == False):
                $ partner = 1

            "Domani - Confessed at the scene of the crime to having fired his guns. Suspected criminal higher-up\nCharges: Second degree murder, aggravated assault with a deadly weapon, suspected involvement in organized crime" if (DomaniInterrogated1 == False and DomaniInterrogated2 == False):
                $ partner = 2

            "Kaj - Wearing the uniform for the establishment, but was the caller who dialed 1-1-3; suspected victim forced through coercion.\nCharges: None" if (KajInterrogated1 == False and KajInterrogated2 == False):
                $ partner = 3

            "Valheo - Found in conflict with a customer; weapons found on their person. Injured in the crossfire.\nCharges: Assault, battery, suspected involvement in organized crime" if canBreakout == False:
                $ partner = 4

            "Luciano - Employee at the establishment; found standing near the suspected source of the conflict. Has largely refused to speak.\nCharges: Suspected involvement in organized crime" if (LuciInterrogated1 == False and LuciInterrogated2 == False):
                $ partner = 5

            # Options which will only appear if Val has been interrogated:

            "Let's break these poor bastards out of here." if canBreakout:
                jump breakOut

            "I actually think I should do my job for once and let these guys go through the system..." if canBreakout:
                jump system
        
        jump questioning
    

    ########################################
    ### INTERROGATIONS #####################
    ########################################

    label questioning:
        scene bg questura interrogation
        show angiolo at left
        show grain
        show reel
        with dissolve

        if partner == 1:
            # Felicien
            show felicien at right behind grain, reel with dissolve

            "Felicien already has one hand free of his cuffs and is working at the other when you enter. He looks up with a sly smile."
            a "Hey. Looking cozy there."
            "Felicien tosses his head."
            f "Yeah. Fuck you."
            a "Yeowch. Pretty bad day, I guess."
            f "No need to play coy with me."
            a "No, I meant it. Sorry about all this. Must suck."
            f "Sucks like your mouth on my-"
            a "Hey, if you're so desperate, hit me up anytime."
            "He scowls, but seems to be reevaluating you. He tosses the cuffs to the ground.{w} Oh, well. Things are cheap."
            if interrogateBegin == False:
                "You sit down before him, resting your elbows on your knees."
                $ interrogateBegin = True
            a "I got some questions for you, though, if you feel like answering."
            f "We'll see."
            jump interrogateFelicien
        
        elif partner == 2:
            # Domani
            show domani at right behind grain, reel with dissolve

            "You enter the interrogation room to a lone figure with his head in his hands so that you can't see his face. He startles when you enter, but doesn't raise his head."
            if interrogateBegin == False:
                "You sit down before him, resting your elbows on your knees. He seems to cringe away from you."
                $ interrogateBegin = True
            a "Woah, easy there."
            d "I'm sorry, I'm sorry, I did it! I killed them all!"
            "His voice is a tearful young man's."
            a "Yeah, so I've heard. Let's just settle down now."
            d "You caught me, you have who you want, so do anything you like to me! Please... Val, I'm so sorry..."
            a "Look, it's time to chill a bit. I don't really have the authority to 'do' anything to you."

            if domaniInterrogated == False:
                "Something catches your eye.{p}On the table nearby lies a fancifully-decorated Venetian-style mask. It looks like one of its ribbons is torn partway off, and it's been partially crushed."
                menu:
                    "Looks like something one of the guys took from him. Is that why he's covering his face like a skittish animal?"
                    "Give him the mask back.":
                        a "Hey. This yours?"
                        "You pick up the mask."
                        "He whimpers."
                        d "My... mask?"
                        a "Yup.{p}You can have it back, if you want."
                        d "Yes, please..."
                        "You hand the somewhat-worse-for-wear mask to him and watch him slowly put it on. Even through these movements, he's careful not to give you a glimpse of his face."
                        "He finishes tying the strings,{w} sighs,{w} and looks up."
                        $ Domani_score += 1
                    "He doesn't need that. Looks like some kind of criminal thing.":
                        "You sit back and ignore the mask."
                
                $ domaniInterrogated = True

            a "I just gotta ask you some questions real quick, 'kay?"
            "Domani sniffles miserably, awaiting his doom."
            jump interrogateDomani

        elif partner == 3:
            # Kaj
            show kaj afraid hold at right behind grain, reel with dissolve

            "Kaj had been sitting with his head in his hands until you walked in, at which point he jerked up to look at you. He looks wretched."
            k -hold "Hello, Carabiniere..."
            a "Hey."

            if interrogateBegin == False:
                "You sit down before him, resting your elbows on your knees."
                $ interrogateBegin = True

            a "Mind if I ask you some questions? Nothing crazy."
            k "Alright."
            jump interrogateKaj

        elif partner == 4:
            # Val
            show val blank at right behind grain, reel with dissolve

            a shut closed "I'm here for an interrogation. Either that, or I'll take money. Whatever."
            a "Listen, I don't like doing interrogations. I'd rather be out on the town right now, really."
            v "I think I'm hallucinating.{w} I got shot today, you know."
            show angiolo -shut
            "You look up at them. They're sitting stiffly, looking weary and staring vaguely out the window. Looks like there was an autombile crash out there?"
            "When they realize you're looking at them, though, their eyes focus on you."
            a "Oh."
            "You take the cigarette from between your lips."
            a -closed "You want anything? We can go on a date or something."
            v @ smile "Beats this. No one's so much as given me laudanum for the bullet in my arm."
            a @ closed shut downturned "Fuckin' animals."
            v "I'll say. Can I have a smoke?"
            "You shrug, pull out your cigarette pack, and frown to yourself."
            a @ upturned "I'm all out..."

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

            v "You ready?"
            a "Yeah, let's get out of here."
            "You open the door to the interrogation room and lead them out of the Carabinieri Comando Stazione, and into the streets of Palermo."
            jump interrogateVal

        elif partner == 5:
            # Luci
            show luci at right behind grain, reel with dissolve

            "Luciano is standing in the interrogation room with his arms folded."

            if interrogateBegin == False:
                "You sit down before him, resting your elbows on your knees."
                $ interrogateBegin = True

            a "Hey."
            l "..."
            a "I'm Angiolo. I'm supposed to come in and interrogate you."
            l "..."
            a "Not much of a talker? Well, alright. We'll see what we can do."
            jump interrogateLuci


    #
    ## FELICIEN ##
    #

    label interrogateFelicien:
        menu:
            a "Let's see..."
            "Can you give me a rundown of what happened?":
                jump .question1
            "So. You a mob boss?":
                jump .question2
            "I think we can wrap this up.":
                jump .finish

        label .question1:
            f "Yeah, my fucking club got shot up by one of my useless employees."
            a "Hum? Any idea why?"
            f "No, I was in the back room doing much more important things. You can't trust Domani with anything, though, he screws up everything he touches somehow."
            a "Pretty big screw-up this time."
            f "Mmhmm. Who knows what's going on in that thick skull of his?"

            if domaniInterrogated == True:
                a "I do. Well, maybe. His interrogation wasn't {i}too{/i} enlightening?"
                f "Fuck, I can't imagine. Trying to get anything out of him is like pulling teeth. But bloodier."
                a "Yeah, he's interesting. He does have a violent streak, huh?"
                f "Hm. So do I."
                a "Yikes.{p}Hey, speaking of which..."

            else:
                a "Eh, maybe I'll find out."
                f "Do that. My business is suffering because of him."
                a "Yeah, well, speaking of business. What kind of place are you running, anyway?"
                f "A host club."
                a "Aha. You get a lot of regulars there?"
                f "This was actually our opening night."
                a "Oh. Landing in town with a bang, then. So..."
            
            a "You didn't know the client, did you? The guy who got shot."
            f "I didn't see who got shot, idiot. I wasn't there."
            a "No ideas floating around up there?"
            f "No."
            a "Alright, then."

            $ FelicienInterrogated1 = True
            jump interrogateFelicien

        label .question2:
            f "Subtle. Is that supposed to scare me?"
            a "Nah, it's a question. My boss wants to know."
            f "And if I say no... will you believe me?"

            # These if statements are here in an effort to keep score farming from happening
            if FelicienInterrogated2 == False:
                menu:
                    "Yeah. I'll take you at your word.":
                        $ Felicien_score += 1
                        f "Obedient little doggie."
                        f "I think I like you. Will you be coming back here?"
                        a "I can make time, if you want me to."
                        f "I would like that very much."
                        a "I'll be sure to check in later, then."

                    "Not so much. Seems kind of suspicious, if you ask me.":
                        f "Sounds like you've already made up your mind, carabiniere."
                        a "I'm just saying. Can't really ignore the facts."
                        f "You said it yourself. It's been a bad day. I'd advise against making it any worse."
                        a "Woof. There's another one for the case file, I guess."
                        f "..."

            $ FelicienInterrogated2 = True
            jump interrogateFelicien

        label .finish:
            a "Got anything else for me?"
            f "No."
            a "Well, if anything comes to you..."
            f "I'll give you a call."
            a "Sure thing. Hope your day gets better."

            jump notes


    #
    ## DOMANI ##
    #

    label interrogateDomani:
        menu:
            a "Let's see..."
            "Can you give me a rundown of what happened?":
                jump .question1
            "What's up with the mask? Kinda scary.":
                jump .question2
            "I think we can wrap this up.":
                jump .finish

        label .question1:
            d "I... I..."
            a "Easy..."
            d "...I hated that stupid job!"
            d "Felicien wanted us to do all these sinful things! I've never been so ashamed in my life."
            a "You mind if I ask what things?"
            d "I hardly dare say...! Flirtation, handholding..."
            "He takes a flustered moment."
            d "...And then when it inevitably went wrong, he didn't do a thing about it. So {i}I{/i} had to. It's okay if you don't understand. I'm horrible. No one else would..."
            a "...And that's when you shot the place up."
            "He nods, defeated."
            d "Some terrible bloodlust came over me..."
            a "That's okay, we hear that all the time. We'll get it all sorted."

            $ DomaniInterrogated1 = True
            jump interrogateDomani

        label .question2:
            d "Oh, um..."
            a "Just curious. Seems like the kind of thing some criminal higher-up would wear. But you seem alright."
            d "No, it's not that..."
            "He sounds embarassed."
            a "Well, that's good. If you were that kind of scary guy, I wouldn't stand a chance."
            d "W...what do you mean? In combat?{w} But you're polizia, aren't you?"
            a "Carabinieri."
            d "That's even worse!"
            d "Even here in military custody, I can't be stopped from killing people..."
            a "Hey, don't worry. I'm not the only one here. And they took your guns, right?"
            d "Yes...{p}But..."
            a "Are you ripped, too?"
            d "Not... exactly?"
            a "Sounds like you're good, then. Unless you have some secret power you're hiding from us. Which I'd like to see."
            d "Oh."
            "He crosses himself."
            d "God save us..."

            $ DomaniInterrogated2 = True
            jump interrogateDomani

        label .finish:
            d "When will I be going to my execution?"
            a "Oh, probably in a week. Maybe two. Things are kinda slow-going around here."
            "He looks down."
            d "...Okay."
            a "Hey, cheer up. You confessed — counts for something.{p}See you around, maybe."

            jump notes

    #
    ## KAJ ##
    #

    label interrogateKaj:
        show kaj normal neutral
        menu:
            a "Let's see..."
            "Can you give me a rundown of what happened?":
                jump .question1
            "What do you think of your boss? Felicien, right?":
                jump .question2
            "I think we can wrap this up.":
                jump .finish

        label .question1:
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

            $ KajInterrogated1 = True
            jump interrogateKaj

        label .question2:
            k @ afraid "Huh? He's fine..?"
            k "No, actually. He's pretentious and mean. Can I ask why?"
            a "My boss thinks he's a mob boss."
            k "...Oh."
            a "..."

            if KajInterrogated2 == False:
                a "...Do you want a cigarette?"
                k "Okay."
                "You lean back in your chair and rummage in your pockets for the pack of cigarettes. You hand Kaj one and take one for yourself."
                show kaj dying none
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

                $ KajInterrogated2 = True
            jump interrogateKaj
            
        label .finish:
            a "Is there anything else of importance you want me to know?"
            k @ speaking "...No, that's all."
            a "Alright. Thanks for chatting."

            jump notes


    #
    ## VAL ##
    #

    label interrogateVal:
        show bg venice street behind grain, reel with dissolve

        "As you walk down the street, you see a vendor at their stall. When they are distracted, a passerby casually grabs one of their items."
        a "Huh. P.S. should do something about that."
        v downturned "You mean, you should do something about that. You're supposed to be Carabinieri."
        a "Yeahh, but I'm trying to get fired."
        v raised "Why's that?"
        a "I just don't like it, really. I'm okay with people doing whatever they want. Seems rather nosey to me to boss people around like that."
        v upset "So...what, that's why you're bringing me out here?"
        a "Well, yeah. If I break you out, I won't be a Carabiniere for much longer, right?"
        v -upset "Is that an offer?"
        "You shrug."
        a closed "Yeah."
        show val -raised
        "They walk in silence for a long time."
        v "I'm inclined to accept, if you cover your ass well enough. Don't want to get into trouble."
        v "And my buddies?"
        a -closed "Oh. Yeah, I can do that."
        v smirk "Cool. If you're looking for another job after, my boss might have something for you."
        v "Let's get you those cigarettes, hm? My coin is yours."
        a @ smile "Okay."
        a "We'll have to head back and pretend I'm working until my coworkers are out, then I can help you guys."
        "You go to the convenience store where Val buys you a new pack of cigarettes, then return to the comando stazione."

        $ canBreakout = True
        jump notes


    #
    ## LUCI ##
    #

    label interrogateLuci:
        show luci neutral normal
        menu:
            a "Let's see..."
            "Can you give me a rundown of what happened?":
                jump .question1
            "Why did you start working at that place?":
                jump .question2
            "I think we can wrap this up.":
                jump .finish

        label .question1:
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

            $ LuciInterrogated1 = True
            jump interrogateLuci

        label .question2:
            l downturned angry frown "It seemed to be a good fit for me."

            if LuciInterrogated2 == False:
                menu:
                    "Really? Wouldn't have thought so, looking at you.":
                        "..."

                    "Huh. Yeah, you are very pretty. Makes sense.":
                        show luci -downturned -angry -frown
                        $ Luci_score += 1
                        l "..."

                $ LuciInterrogated2 = True
            jump interrogateLuci

        label .finish:
            a "Alright. Be seeing you."
            l "..."

            jump notes


    ########################################
    ## Choosing to try them as criminals ###
    # (Bad ending)
    ########################################

    label system:
        show angiolo at left
        """
        You open your notebook and begin to gather all your notes into a cohesive and reasonable-sounding report.

        You work unpaid overtime late into the night, because of your easily-distractible ADHD brain and because the military doesn't care about your wellbeing, individuality, or personhood.

        Your boss claps you on the shoulder.
        """
        show quinn at right
        q "Keep it up, Angiolo, you're doing great. I've never seen you come so close to doing an average amount of work. I knew you had it in you."
        q "Now, I'm heading home for the night. Leave your report outside my office when you're done."
        a flat "Yeah, okay, thanks..."

        jump badEnd


    ########################################
    ## CHASE SCENE #########################
    ########################################

    label breakOut:
        """
        You sit in your office for a bit, contemplating how to pull this off.
        
        You're not scared, but you're not stupid either.{w} Well, not completely. Anyway, you've been wanting a change of pace for a while now.

        The stazione is so quiet. There are rarely many others here, after all. Most are out on patrol... or filling out paperwork. The quiet is honestly kind of nice.

        And convenient. Who will notice or care if you just... get up from your desk... leave your office...{p}The keys jingle pleasantly in your hand.
        """
        show bg questura interrogation behind grain, reel
        show domani behind grain, reel
        with fade
        d "Snf...{w} snf...{w} huh?{w} W-what is this?!{p}Oh, God! Thank God!"

        hide domani
        show felicien behind grain, reel
        with fade
        f "Oh, puppy, you're back.{w}{size=-20} Damn. I was hoping for someone sexier.{/size}"

        hide felicien
        show kaj afraid behind grain, reel
        with fade
        k "Carabiniere... you... you can't do this. This is illegal..."

        hide kaj
        show luci behind grain, reel
        with fade
        l "...{p}...?"
        hide luci

        "You go around to the holding cells of each of the suspects, insert the key, hush them, and quietly release them.{w} Easy."
        show val smirk blank behind grain, reel
        with fade
        v "Well, aren't you a sight for sore eyes.{w} Thanks for hearing me out. Now, let's get out of here."
        hide val with dissolve

        "Score. Prisoners rounded up, you lead them to the back entrance, same place criminals get brought in. Guess they can't really be brought through the front where civilians come in."
        scene bg questura front
        show grain
        show reel
        with dissolve
        """
        Everything is going to plan. And it's so quiet in here, maybe your boss went out on patrol?{w} His office isn't {i}too{/i} close, just gotta creep to the back door...

        There's a tap on your shoulder.
        """
        show angiolo at left behind grain, reel
        show domani at right behind grain, reel
        with dissolve
        d "Is that... your friend?"
        a "Huh-?"
        q "Angiolo?"
        a wide upset "Ggk!"
        hide domani with dissolve

        show quinn at right behind grain, reel with dissolve
        show angiolo -upset
        "It only takes him a moment to look over your little procession and put together what's going on."
        q "Sigh... Couldn't you at least have run this by me first?"
        a "Ahhhhahaha. Whoops."
        
        hide quinn with dissolve
        show felicien at right behind grain, reel
        f "MOVE IT, ASSHOLES!" with vpunch

        hide felicien
        "Before you can do anything to fix this, Felicien has bolted for the door. His entourage obediently follows suit, and only Kaj glances back at you. But also..."
        show domani at right behind grain, reel with dissolve
        d "AAAAAAAAHHHHH!!!!!{p}{size=+40}AAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH{/size}"
        hide domani with dissolve

        "You watch him run out of the door and headlong into the wall of the neighboring building and rebound. Poor guy seems too frightened to think."
        show quinn at right behind grain, reel with dissolve

        menu:
            q "Ah, jeez."
            "Go after them. You know the Carabinieri, you know how to help them escape.":
                show angiolo -wide
                hide quinn with dissolve
                jump chase

            "Stay behind and try to reason with your boss, buy them time.":
                jump stayBehind


        label chase:
            # Running

            "You break away from your boss and tear out of that place, grabbing Domani and pushing him along ahead of you to get him running."
            show bg venice street behind grain, reel with dissolve
            show domani at right behind grain, reel with dissolve
            a downturned "Let's get those legs moving, yeah?!"
            d "BAAAHHHH!!{p}O God, if you want me dead, just strike me down??! Even with savescumming, this is all too scary!!!"
            d "{i}O Santa Maria, Madre di Dio, prega per noi peccatoti, adesso e nell'ora della nostra morte...{/i}"
            """
            Once Domani is running, he's actually kinda fast. You do your best to keep up with him, tearing after the others.

            imagine there's more action here
            """
            #running around

            # can choose to hide in the strip club where you meet Eligio
            # I think this might be a whole new path a la Azami Hatoful Boyfriend

            # must have a score of 1 with Felicien for him to care enough to save you
            if Felicien_score >= 1:
                """
                A hand flashes out of the dark and closes tight around your wrist, and you're yanked sideways so hard you lose balance.

                Luckily, he catches you before you tumble pussy-over-teakettle into the dirt. For those slender arms, he sure is strong— oof!
                """
                f "Clumsy ass."
                "His voice is a hiss, irritated as always. He has you shoved hard against the wall, and my God, he towers over you in those heels."
                a "Hey, I—"
                """
                His hand clamps over your mouth so hard, you think he knocked some of your teeth in a little. Staring out at the street, he mouths the words, 'shut up'.
                
                He has you caught like a fish, so you can only move your eyes to watch as best you can. Felicien pulled you on the other side of some crates, so the view is terrible, but you can just see through some of the slats... Maybe?
                
                Someone seems to be running past, at least.{w} There's no way you actually pulled ahead enough that he didn't see that little maneuver, right?

                Felicien stands over you, stock-still, staring with those hard eyes for what feels like an eternity after the guy you {i}think{/i} was your boss ran past.
                """
                pause
                "...He releases you and shakes out his slender-fingered hand with an air of disgust."
                f "Ew. You breathe so God damned much."
                a "Sorry?"
                f "Yeah, you should be."

                jump .success

            else:
                # he pushes you into the street to keep Quinn occupied. FIGHT FIGHT
                """
                You don't see who, but someone must have collided into you, because you're launched off your feet — you try to catch yourself, but your shocked wrists buckle under you and your face smacks the stone ground.{w} {i}Yowch.{/i}
                
                But behind you, your boss isn't stopping; no, he's coming up fast. Those thundering, booted footsteps. He's too close. You have to get up.

                You have to get up.
                """
                pause
                "You scramble to your feet, clumsy in your daze. The adrenaline in your veins is leaving you shaky."
                q "Down, soldier!"
                """
                He doesn't even sound winded.

                Of course you couldn't outrun him. For all your military training, you now work a {i}desk job{/i} while he's on the field. Save the times he's conveniently breathing down your neck.
                
                You turn to face your boss as steadily as you can, determined not to let him past.{p}Oh, God. He's intending on just barrelling past you. Or {i}through{/i} you?
                """

                menu:
                    "HE'S HUGE AND RUNNING AT ME, WHAT THE HELL DO I DO??":
                        a "{size=+20}BOSS!!{/size}"
                        """
                        He's... not stopping. He's going to run full-force into you. And you're going to implode like a little grape. He's-
                        
                        ...Running right past you.{p}Oh, thank the almighty Lord.

                        {w}Wait, how the hell are you going to save your escapees now?
                        """
                        jump badEnd

                    "DRAW SWORD??!":
                        "You whip your sword out of its sheath?!?!"
                        # continues below
                    
                show quinn at right behind grain, reel with dissolve
                "He slows down and comes to a stop before you."
                q "...What are you doing, soldier?"
                a "Uh, what I was taught, sir. To draw my weapon on instinct."
                q "On your commanding officer."
                q "That's an unfortunate choice, Angiolo. By law, I can't take this kind of breach of orders lightly."
                "Now he's drawing his own blade. Yikes yikes yikes, this was {i}not{/i} where you would have liked this to go."
                q "Sigh.{p}I'd better take care of this quickly so I can find our suspects."
                "He's advancing on you. You raise your blade."
                a "Uhhhhhhhhhhhhhhhhhh, boss? The charge for this kind of thing isn't, like, firing squad, right?"
                """
                He moves suddenly, and his blade comes down hard on yours. Jesus! Just that blow struck your fingers numb. Or maybe that's a side effect of the creeping feeling that you're completely screwed. It's all you can do not to drop the thing.

                Okay, so the charge is definitely death. Well, what were you supposed to do? If you hadn't been tripped in the street by some jerk...

                He moves again, and you just manage to deflect the blow to your shoulder. ADHD brain be damned, you have to focus!

                The next one comes fast. He's trying to disarm you. You again sweep your blade to the side to drive his away, but he's not only stronger than you but also generally {i}better{/i} than you. You never thought you'd {i}actually{/i} have to fight for your life like this, okay!

                You need to find your opening. You can only hold him off for so long before your twig arms break off.

                another move or two
                """

                menu:
                    "Kill him.":
                        "you Get Him"
                        jump .success
                    "Man, as much as I hate my job, he {i}is{/i} a nice guy... Probably has a wife and kids...":
                        "you give him an opening"
                        jump .failure
            
            label .failure:
                # Bad end: die. this is utter betrayal
                "Bro you die"
                jump badEnd
            
            label .success:
                # Good end: run away to find and reunite with your comrades
                "You get away yippee!"
                jump train


        label stayBehind:
            # Staying behind with Quinn

            a "Ay boss, I'm running it by you now."
            "You try to position yourself in his way as casually as possible. Which is {i}terrifying{/i}, because he could break you like a twig."
            "He smiles pleasantly."
            q "Well, this is mighty inconvenient!"

            menu:
                a "Uh, I'll make it quick. So look here..."
                "They're not who we're after.":
                    q "Give us the full report, soldier."
                    a "Nothing but lies. Lies, lies, lies, lies, lies lieslieslLIESLIESLEISL"

                    # Val score must be at least 1 to pull off this lie
                    if Val_score >= 1:
                        jump .success

                    else:
                        q "Who do you think you're fooling, little man?"
                        jump .failure

                "They're not so bad.":
                    q "No?"
                    a "Yeah. We had a nice chat. I think they could have a change of heart if we just give 'em a chance."
                    jump .failure

                "Their story's kinda sad, really.":
                    q "Aww. You're a kindhearted guy, Angiolo. And it's hard being kindhearted in this line of work. You really hear the worst of it, don't you?"
                    a "Yeah..."
                    jump .success
            
            label .failure:
                # Bad end: convinced to stay with the Carabinieri (Quinn ending)

                q "Sorry, Angiolo."
                jump badEnd
            
            label .success:
                # Good end: Quinn lets you go, have to go and find them. but with Doubt in your heart (Quinn wooing opportunity)

                q "..."
                q "You know, I think you made a good call, soldier."
                a "Yeah?!"
                q "Don't make those calls again without talking to me."
                a "Yeah.{w} Yessir."
                jump train
    

    ########################################
    ## TRAIN RIDE AND WOUND TENDING ########
    ########################################

    label train:
        # regroup
        "you go meet back up with the gang to regroup and there's some conversation in here and you decide to call the mafia guy"

        # v "Sorry, man. This can't be what you thought you were signing up for."

        # Vittore put Luci under Felicien as punishment for something
        # idk if I actually want this conversation on-screen
        f "Hello, boss."
        boss "{i}Felicien. I'm surprised to hear your voice. I was under the impression you useless group of baccalà got yourselves imprisoned.{/i}"
        f "We ran into a bit of trouble. Nothing we can't handle."
        boss "{i}Why are you calling, then?{/i}"
        f "We'd be able to handle it a bit better if we had somewhere to stay until the cops are off our asses."
        boss "{i}Do one better: get them off{/i} my {i}ass. Fucking moron.{p}What secrets can we expect them to know now?{/i}"
        f "I am {i}not{/i} stupid enough to let anything slip."
        boss "{i}And your team?{/i}"
        "Felicien turns and looks dirently at Domani."
        f "If they did, I don't think they should be involved in cosa nostra."
        boss "{i}No. But unfortunately if you want to get anything done in this world, you'll have to work with idiots. They're impossible to avoid.{p}God fuck it, Felicien. If you want to try to do something right, then get out of Palermo. Tonight.{/i}"
        f "Excuse me?"
        boss "{i}You heard me. You know the damn prime minister and his guys have been out here recently, and they're quickly making an enemy of us.{/i}"
        boss "{i}Since you so badly want to draw attention to yourselves, lead the feds to Reggio. I have a contact you can stay with. A clementine farmer. Get her and yourselves killed, I don't care. My business is here, in the west.{/i}"
        f "I have wounded, I can't cross Sicily tonight."
        boss "{i}All the better. They'll be able to follow the blood trail you leave behind.{/i}"
        f "Fucking great..."
        boss "{i}Play stupid games, win stupid prizes. Don't call again.{/i}{w} Bzzzt..."
        "Felicien slams the phone back onto its holder and steps out of the booth."

        # v "So. You're born into the mafia."
        # "They tick off on their fingers."
        # v "You don't kill, you don't do the job your boss gives you, you can't help in a medical emergency, and—"
        # "They look him up and down."
        # v "—I doubt you could hold your own in a fight. So what're you good for?"

        # Train from Palermo along the coast of Sicily to Messina takes ~3 hours, and at the end includes a ferry ride. Tend to Val on the way.
        # I need a train interior bg image
        "hop on the train (there's some stuff that sounds like this isn't a train bc I hadn't worked out all the details yet dw abt it)"

        "As you settle into the place, you notice Val slump hard against a wall, closing their eyes and breathing deliberately.{p}They must be in some wicked pain."

        menu:
            "We should get them to a doctor.":
                jump .bhospital

            "The military gave me some medical training...":
                jump .bandage

            "The best we can do right now is give them some booze.":
                jump .booze

            "They haven't said anything. Leave them be.":
                "They must be handling it alright. If they wanted help, they'd speak up. And it's not like we have much to work with for wound treatment in this dump, anyway."
                return

        ## BAD END ##

        label .bhospital:
            a "Hey, you're not looking too good. Someone should take a look at that."
            "Their eyes open and focus on you."
            v "Someone."
            a "You know, a professional. I can't believe you've just been walking around with that hole in your shoulder.{p}Is there a hospital around?"
            f "A hospital?{p}Tell me you're not that much of a dumbfuck."
            a "What? There's not much we can do here, and they need medicine. Clearly."
            f "Right. They won't ask questions, will they?"
            l "Angiolo is correct, Felicien."
            l "They will simply give unenlightening answers to any questions."
            a "Yeah. I'm smart enough for that."
            "and they went to the hospital and got caught by the authorities"

            jump badEnd


        label .bandage:
            a "Hey, you're not looking too good. I might be able to help."
            "Their eyes open and focus on you."
            v "How?"
            a "We learn some stuff about first aid in the Carabinieri. I could at least clean it up and stuff."
            "They look reluctant."
            v "...Yeah, that'd probably be good."
            a "Don't worry. I'm not {i}that{/i} bad at this."
            v "Ha, ha. I'm sure you're great. Just not excited about being poked and prodded."
            a "Yeah, I bet."
            a "But trust me. And if you need me to stop, don't be scared to give a shout."
            "They eye you with equal parts embarrassment and gratitude."
            v "Okay.{w} Thanks."
            a "Aight, be right back."
            "You search the hideout for any supplies you might need, then return to Val. They eye your handful of supplies."
            v "Is that enough?"
            a "Should be. There's some good first aid stuff here, really. But carabinieri teaches you how to improvise. Now..."
            "You look them up and down."
            a "Need some help getting that shirt off?"
            v "Guh, no..."
            "They use their good arm to pull it up, exposing a strong chest and surprisingly slender waist. From here, though, how they should move to remove the shirt further is unclear, and you watch them struggle for a bit."
            a "Here, let me."
            """
            You come forward and take the hem of the shirt from them. You guide their head out first.

            From there you have to be careful of the fabric around the wound, unsticking it where it has been glued down by blood and carefully pulling it out of the hole.{p}They grit their teeth as it comes free.

            Then you remove the shirt from their arms the rest of the way and toss it aside.

            Now you can see the bullet wound clearly. At least some of it came out the other side, and the impact looks to have pulverized the surrounding flesh painfully.
            """
            a "Tsss, ouch. This stuff is brutal on you dikarycota."
            "You reach out a finger to prod the muscle along the outer damage, and they stiffen."
            v "Can you just get this over with?"
            a "Sure thing, boss."
            "You pour some of the alcohol you had seen earlier into a small bowl, and a little bit over the wound. You rinse your hands in the bowl, then turn to Val."
            a "Looks like I'm gonna have to fish around for any bullet or cloth bits."
            "They close their eyes, looking a little ill."
            v "Okay."
            a "You scared?"
            "They shake their head nauseously."
            "You take their well-muscled arm firmly with one hand."
            a "Ready?"
            "They nod once."
            "With your other hand, you reach two fingers into the bullet hole. First they tense to rigidity, then they jolt and hiss."
            "pretend this scene reaches a conclusion"
            # continue

            return
        

        label .booze:
            "You thought you saw some earlier..."
            "You open some cabinets and rummage through them. Bingo.{p}You turn back to Val."
            a "Hey, you're not looking too good."
            "You hold up the bottle."
            a "Want some?{w} It's no laudanum, but..."
            "Their eyes open and focus on the bottle in your hand."

            $ Val_score += 1

            v "Where'd you get that, in a place run by Mr. Stickler? Yes, {i}please{/i}."
            "You hand it to them, and they take a mighty swig."
            v "God, you're my favorite person right now, Angiolo."
            a "Haha, hey, you're not too bad yourself. We gotta keep you up and running, right? The best we can, anyway."
            """
            When you look up, you notice Luci staring at you. Why are his eyes always so scary and intense like that?

            And just as you were thinking about saying something, he's turned away again. Yeesh. Okay, then.

            Well, it's time for lights out and go to sleep. The rumbling and gentle swaying of the train car knocks you right out...
            """

    return