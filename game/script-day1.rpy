######################################
### DAY 1 ############################

# Contains all scenes and dialogue for day 1
# + Interrogations, character introductions, breaking out of prison
# + Getaway to Messina
# + Calling the big boss
# + Patch up Val's bullet wound

######################################


label day1:

    ########################################
    # Setting the scene ####################
    ########################################

    play audio "<loop 3.0>audio/projector.mp3"

    scene bg questura desk
    show angiolo at left
    show grain
    show reel
    with dissolve


    ## Dialogue begins ##

    """
    Palermo: a beautiful coastal city in Sicily, where cycling tourists and playing children alike can go outside and enjoy the sun.

    Unfortunately, the place is also overrun by illicit activities. People whisper it in the streets - {i}cosa nostra{/i}.
    
    And because you are an idiot, you are in the middle of it all, in a Carabinieri Comando Stazione.
    
    You are working at your desk, eyes glazing over endless piles of paperwork (positivvely daydreaming, really), when the door opens.{p}You look up.
    """
    a "Hey, boss."
    show quinn at right behind grain, reel with dissolve
    q "Look alive, Angiolo. I have a job I'd like you to handle."
    a @ flat "Right... Just what I  needed."
    q "Come on, let's keep up the professionalism here. Anyway, you're smart, Angiolo. If you just take a little interest... you've got this one in the bag."
    q "We have a handful of eyewitnesses from a shooting today. It was at their establishment, and some of them may be culprits."
    a "Huh? You telling me these people shot up their own place?"
    q "First rule of the Carabinieri, Angiolo: Never rule out homicide. From what they had on them, there's something criminal going on either way."
    q "Well, interrogate them for me and find out, would you?"
    a "Whatever you say."
    "He slips you a sheet of notebook paper."
    q "We're looking into backgrounds right now, but here's what we have from on-scene."
    q "Good luck, soldier!"



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
            # Confiscated items: dagger, dildo

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
            # Confiscated items: mask, handguns, ID

            "Uhhh.... what am I supposed to do with this. Is it even real? Shouldn't this be sent to forensics or whatever? Is that the right department..."

            show domani at right behind grain, reel with dissolve

            a "Woah."
            "The figure sitting in the center of the interrogation room is in full, extravagant festival costume. Their head in their hands, they're giving full, wracking sobs. Yikes."
            a "Yikes. Bad time?"
            "They startle at the sound of your voice, but still only peer at you through their fingers."
            d "Am I... being executed?"
            a "Executed??"
            "You're at a loss. Two seconds in, and you've never seen an interrogation like this before."
            d "I've been caught, so, please, God, just get it over with..."
            a "....Look, man, are you lost? It looks like you're coming from another city. And another time..."
            d "I... my dress? Is it illegal here, too?"
            a "Uhhhhh. I dunno. No? I mean, festival is a Venetian thing? But. Uh. You're not getting executed for that."
            d "But, for the shooting..."
            a "Is that a confession?"
            d "Do I get forgiven for a confession?"
            a "Um."
            "Do they?"
            a "Look, I just gotta ask you some questions real quick before jumping to executions."
            "They whimper and sniffle, awaiting doom."

            $ domaniInterrogated = True
            jump interrogateDomani

            # give him back mask
            a "Looks like they took this from you. And, uh, you don't seem too happy without it."
            d "Oh... oh, thank God!"
            "He turns away to quickly and nimbly afix the mask to his face. Once it's on, he breathes a sigh of relief and seems to calm somewhat."

            # ask him about ID
            a "Is this your real ID?"
            d "Ah? Oh. Oh, my God."
            "They sound embarrassed. Actually, worse. Deeply humiliated. Convinced of failure. Well... that's not too conclusive?"
            a "At least tell me what your pronouns are. I need to adjust my internal monologue over here."
            d "I'm... a man?"
            "Why does he sound so uncertain?"
            a "Cool. Nice."

            # give him back handguns
            a "These yours?"
            "He cringes back from the guns and doesn't take them from you."
            d "Oh. I… can't. I'll kill again.. Please, I don't care what you do with them. I don't deserve them anymore."
            a "Oooookay. Well."
            "He stares at them longingly. Hard to blame him. They're gorgeous puppies, with flower designs burned into the wood handles. You… keep them, I guess."

            jump interrogateDomani

        elif partner == 4:
            # Val
            # Confiscated items: multiple knives, single handgun, water-damaged photo

            show val blank at right behind grain, reel with dissolve

            a shut closed "I'm here for an interrogation."
            "You stare at your shitty sheet of notebook paper. For a long time. Your mind completely glazes over. God, this is so boring."
            a "Either that, or I'll take money. Whatever.{w} Listen, I don't like doing interrogations. I'd rather be out on the town right now, really."
            v "I think I'm hallucinating.{w} I got shot today, you know."
            show angiolo -shut
            "You look up at them. They're sitting stiffly, looking weary and staring vaguely out the window. Looks like there was an autombile crash out there?"
            "When they realize you're looking at them, though, their eyes focus on you."
            a "Oh."
            a -closed "You want anything? We can go on a date or something."
            v @ smile "Beats this. No one's so much as given me laudanum or anything for the bullet in my arm."
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
            # Confiscated items: expensive sleek weapon, cash


            show luci at right behind grain, reel with dissolve

            "The suspect is ignoring his chair to stand in the middle of the room, stiff as a board, with his arms folded."
            "He's legit just standing there, but for some reason your immediate impression is that he's beautiful. It tugs at your memory somehow... But your memory is shit, anyway."

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
            
            a "You didn't know the client, did you? The guy who got shot."
            f "I didn't see who got shot, idiot. I wasn't there."
            a "No ideas floating around up there? Any weird regulars or anything?"
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
                        f "Scary. Dipshit."

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
            "He sounds embarrassed."
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
            "Exactly what sort of establishment were we talkin' about again?":
                jump .question2
            "I think we can wrap this up.":
                jump .finish

        label .question1:
            l "...We were working. And a man came in and demanded that we...did what he saw in porn."
            a "Okay. So, what happened?"
            l @ frown "...The man was getting aggressive. My coworker pulled out a knife."
            l -downturned "...My other coworker pulled out their gun and started shooting."
            a "Wait, wait, names please?"
            l "Valheo and Domani."
            "You scribble this all down."
            a "Gotcha. Well, this isn't much of a mystery. You people must be pretty new to the life of crime, huh?"
            l "..."
            l "... Yes."
            a "Well, they can't crack down on you too hard, then. Besides, it was a mistake, yeah?"
            l ".. Yes."
            a "See, you'll be fine."

            $ LuciInterrogated1 = True
            jump interrogateLuci

        label .question2:
            l "..."
            l "......."
            l "................."
            l "............................ A night club."
            a "No way. It's not the one on .. god, what was it.... "
            """
            Now you can't remember the STREET name, but you CAN remember...

            You visited almost on a whim some boring night. You were never really 'in' on the dating scene, you still weren't really sure if you /liked/ that kind of thing, but isn't this what people do to have fun? You decided to scope it out.

            You went into the first club on the street that didn't seem too loud and crowded, almost swirling with lights and sounds and conversation, all so much you could hardly focus on trying to read a person's lips and definitely wouldn't even enjoy it.
            
            This one was quiet, nearly empty. And let's be real, it was ass.
            
            Even now, focusing with all your pathetic brain power, you can't even remember who was sitting with you. What overwhelmingly dominates is...
            """
            f "What the fuck do I pay you for?"
            "... Up on the shitty little stage they had sat on one end of the room."
            f "You're under my jurisdiction now. We have a paying customer. So you get up there and put on a show for them."
            l "I. Will. Not."
            "He grabbed Luciano."
            f "You'll stand up there and sing or I'll open a hole in that pretty little throat. And your daddy will thank me."
            "Even then, his face cold and hard as steel, you couldn't help but think how gorgeous he looked. All angelic justice. Like Michael or something."
            
            a "...I saw you there!"
            "He stares at you in horror."
            l ".. No you didn't."

            $ LuciInterrogated2 = True
            jump interrogateLuci

        label .finish:
            a "Alright, cool. Thanks. Be seeing you."
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

        # this is actually the secret Quinn route

        jump badEnd


    ########################################
    ## BREAK OUT ###########################
    ########################################

    label breakOut:
        # I need to rework this sequence

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
        q "Ah, jeez."

        jump car
    

    ########################################
    ## CAR RIDE AND WOUND TENDING ##########
    ########################################

    label car:
        # Stop at safehouse to figure out next plan and tend to wounded
        
        scene black
        with dissolve

        "He sticks his handgun into the cup holder. He has to fumble and maneuver and hammer it in a bit to fit it between the other guns and the hot pink toy already in there."
        # insert image
        k "Sir, please don't use my car as storage."
        f "Look, I know you're a little {i}bitch{/i}, but in this business you've got to be prepared for anything."

        # v "Sorry, man. This can't be what you thought you were signing up for."

        # v "So. You're born into the mafia."
        # "They tick off on their fingers."
        # v "You don't kill, you don't do the job your boss gives you, you can't help in a medical emergency, and—"
        # "They look him up and down."
        # v "—I doubt you could hold your own in a fight. So what're you good for?"

        # Car from Palermo along the coast of Sicily to Messina takes ~3 hours, and at the end includes a ferry ride

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
            """

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

    return