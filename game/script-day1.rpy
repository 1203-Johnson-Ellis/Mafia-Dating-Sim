######################################
### DAY 1 ############################

# Contains all scenes and dialogue for day 1
# + Interrogations, character introductions, breaking out of prison
# + Getaway to Messina
# + Calling the big boss
# + Patch up Val's bullet wound

# I will want to go through and check all the {w} and {p} tags with the new pause automation

######################################


########################################
# Setting the scene ####################
########################################

## Introductory sequence

label day1:
    "This is an unfinished version of the game. It's still in the process of being written and refined. Please excuse any missing scenes or visuals."

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
    
    You are working at your desk, eyes glazing over endless piles of paperwork (positively daydreaming, really), when the door opens.{p}
    You look up.
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
    "She slips you a sheet of notebook paper."
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
            ## Suspects
            # The option to interrogate a suspect will disappear if they have been asked all available questions
            # Otherwise, I want them to remain in case the player changes their mind about not asking a question, or wants a refresher
            # (^ should probably change to being greyed out when all questions have been asked or something)

            "Felicien - Known owner of the establishment; weapons found on person; uncooperative.\nCharges: Suspected money laundering, involvement in organized crime" if (FQ1Asked == False and FQ2Asked == False):
                $ partner = 1

            "Domani - Confessed at the scene of the crime to having fired guns. Suspected criminal higher-up\nCharges: Second degree murder, aggravated assault with a deadly weapon, suspected involvement in organized crime" if (DQ1Asked == False and DQ2Asked == False):
                $ partner = 2

            "Valheo - Found in conflict with a customer; weapons found on person. Injured in the crossfire.\nCharges: Assault, battery, suspected involvement in organized crime" if canBreakout == False:
                $ partner = 4

            "Luciano - Employee at the establishment; found standing near the suspected source of the conflict. Has largely refused to speak.\nCharges: Suspected involvement in organized crime" if (LQ1Asked == False and LQ2Asked == False):
                $ partner = 5

            ## Story progression
            # Will only appear if Val has been interrogated

            "Let's break these poor bastards out of here." if canBreakout:
                jump breakOut

            "I actually think I should do my job for once and let these guys go through the system..." if canBreakout:
                jump system
        
        jump confiscatedItems
    

    ########################################
    ### INTERROGATIONS #####################
    ########################################

    # Go through these labels when a suspect is selected for interrogation

    ## Loops through this until all desired items have been taken

    label confiscatedItems:
        menu:
            a "Looks like some items were confiscated from the suspect. I could take some of these, if I think they'll be useful. Unless they're better kept out of reach."

            # Felicien options
            # Clean up coding on this so options are removed on subsequent loops
            "Take the dagger." if partner == 1:
                a "Nice. It looks old."
                # May not need these additional vars if can just add it to the set
                # Unless the indication that it was taken once ends up being useful
                $ FDaggerPickedUp = True
                $ playerInventory.add("Ceremonial Dagger")
            
            "Take the sparkly fun toy." if partner == 1:
                "You're gonna touch that? Is it {i}washed{/i}?"
                a "Yeesh... I don't get paid enough to deal with this."
                $ FDildoPickedUp = True
                $ playerInventory.add("Sparkly Toy")
            
            # Domani options
            "Take the mask." if partner == 2:
                a "This is like those masks at the Venetian festival thing that was outlawed. I guess that's evidence."
                $ DMaskPickedUp = True
                $ playerInventory.add("Venetian Mask")
            
            "Take the handguns." if partner == 2:
                a "Pretty incriminating. But a very nice pair of custom Rafficas."
                $ DGunsPickedUp = True
                $ playerInventory.add("Dual Rafficas")

            # Val options
            "Take the knives." if partner == 4:
                a "Why are there so many..."
                $ VKnivesPickedUp = True
                $ playerInventory.add("Too Many Knives")
            
            "Take the water-damaged photo." if partner == 4:
                "The photo depicts four kids of varying ages hangin' out with their dad."
                $ VPhotoPickedUp = True
                $ playerInventory.add("Water-Damaged Photo")

            # Luci options
            "Take the sleek, expensive handgun." if partner == 5:
                a "It's a single, small Glisenti. This thing is swank."
                $ LGunPickedUp = True
                $ playerInventory.add("Sleek Glisenti")
            
            "Take the thick wad of cash." if partner == 5:
                a "Hell yea, this is why you work with criminals. Rob 'em and make bank."
                $ LCashPickedUp = True
                $ playerInventory.add("Wad of Cash")
                # Consider adding a currency function (if it would be useful for anything)

            "I'm set.":
                "Time to go meet the suspect in question."
                jump questioning
        
        jump confiscatedItems


    ## Dialogue sequence for introducing the selected suspect

    label questioning:
        scene bg questura interrogation
        show angiolo at left
        show grain
        show reel
        with dissolve


        ## Felicien
        if partner == 1:
            show felicien at right behind grain, reel with dissolve

            "Felicien already has one hand free of his cuffs and is working at the other when you enter. He looks up with a sly smile."
            a "Hey. Looking cozy there."
            "Felicien tosses her head."
            f "Yeah. Fuck you."
            a "Yeowch. Pretty bad day, I guess."
            f "No need to play coy with me."
            a "No, I meant it. Sorry about all this. Must suck."
            f "Sucks like your mouth on my-"
            a "Hey, if you're so desperate, hit me up anytime."
            "He scowls, but seems to be reevaluating you. He tosses the cuffs to the ground.{w} Oh, well. Things are cheap."
            
            if beganInterrogations == False:
                "You sit down before her, resting your elbows on your knees."
                $ beganInterrogations = True

            a "I got some questions for you, though, if you feel like answering."
            f "We'll see."

            jump interrogateFelicien
        

        ## Domani
        elif partner == 2:
            show domani at right behind grain, reel with dissolve

            a "Woah."
            "The figure sitting in the center of the interrogation room is in full, extravagant festival costume. His head in his hands, he's giving full, wracking sobs. Yikes."
            a "Yikes. Bad time?"
            "He startles at the sound of your voice, but still only peers at you through his fingers."
            d "Am I... being executed?"
            a "Executed?? Uh, we don't really-"
            d "I've been caught, so, please, God, just get it over with..."
            a "....Look, man, are you lost? It looks like you're coming from another city. And another time..."
            d "I... my dress? Is it illegal here, too?"
            a "Uhhhhh. I dunno. No? I mean, festival is a Venetian thing? But. Uh. You're not getting executed for that."
            d "But, for the shooting..."
            a "Is that a confession?"
            d "Do I get forgiven for a confession?"
            a "Um."
            "Does he?"
            a "Look, I just gotta ask you some questions real quick before jumping to executions."
            "He whimpers and sniffles, awaiting doom."

            $ DInterrogated = True
            jump interrogateDomani


        ## Val
        elif partner == 4:
            show val blank at right behind grain, reel with dissolve

            a shut closed "I'm here for an interrogation."
            "You stare at your shitty sheet of notebook paper. For a long time. Your mind completely glazes over. God, this is so boring."
            a "Either that, or I'll take money. Whatever."
            a "Listen, I don't like doing interrogations. I'd rather be out on the town right now, really."
            v "What the hell kind of police...? I'm so out of it, dude.{w} I got shot today, you know."
            show angiolo -shut
            "You look up at them. They're sitting stiffly, looking weary and staring vaguely at the wall."
            "When they realize you're looking at them, though, their eyes focus on you."
            a "Oh."
            a -closed "You want anything? We can go on a date or something."
            v @ smile "Beats this. No one's so much as given me laudanum or anything."
            a @ closed shut downturned "Fuckin' animals."
            v "I'll say. Can I have a smoke?"
            "You shrug, pull out your cigarette pack, and frown to yourself."
            a @ upturned "I'm all out..."

            menu:
                "Give them your cigarette?"

                "Yes":
                    $ VScore += 1

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


        ## Luci
        elif partner == 5:
            show luci at right behind grain, reel with dissolve

            "The suspect is ignoring his chair to stand in the middle of the room, stiff as a board, with his arms folded."
            "He's legit just standing there, but for some reason your immediate impression is that he's beautiful. It tugs at your memory somehow... But your memory is shit, anyway."

            if beganInterrogations == False:
                "You sit down before him, resting your elbows on your knees."
                $ beganInterrogations = True

            a "Hey."
            l "..."
            a "I'm Angiolo. I'm supposed to come in and interrogate you."
            l "..."
            a "Not much of a talker? Well, alright. We'll see what we can do."
            
            jump interrogateLuci


    ## The below labels include the questioning itself

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

            "Give back his dagger." if FDaggerPickedUp == True:
                jump .dagger
            
            "Give back his toy." if FDildoPickedUp == True:
                jump .dildo

            "I think we can wrap this up.":
                jump .finish


        label .question1:
            f "Yeah, my fucking club got shot up by one of my useless employees."
            a "Any idea why?"
            f "No, I was in the back room doing much more important things. You can't trust Domani with anything, though, he screws up everything he touches somehow."
            a "Pretty big screw-up this time."
            f "Mmhmm. Who knows what's going on in that thick skull of his?"

            if DInterrogated == True:
                a "I do. Well, maybe. His interrogation wasn't {i}too{/i} enlightening?"
                f "Fuck, I can't imagine. Trying to get anything out of him is like pulling teeth. But bloodier."
                a "Yeah, he's interesting. He does have a violent streak, huh?"
                f "Hm. So do I."
                a "Yikes.{p}
                Hey, speaking of which..."

            else:
                a "Eh, maybe I'll find out."
                f "Do that. My business is suffering because of him."

            $ FQ1Asked = True
            jump interrogateFelicien


        label .question2:
            f "Subtle. Is that supposed to scare me?"
            a "Nah, it's a question. My boss wants to know."
            f "And if I say no... will you believe me?"

            # These 'if' statements are here in an effort to prevent score farming
            if FQ2Asked == False:
                menu:
                    "Yeah. I'll take you at your word.":
                        $ FScore += 1
                        f "Obedient little doggy."
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

            $ FQ2Asked = True
            jump interrogateFelicien
        

        label .dagger:
            "You give back his dagger"

            $ playerInventory.remove("Ceremonial Dagger")
            jump interrogateFelicien

        
        label .dildo:
            "You give back his toy"

            $ playerInventory.remove("Sparkly Toy")
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
            
            "Give him back his mask." if DMaskPickedUp == True:
                jump .mask
            
            "Give him back his handguns." if DGunsPickedUp == True:
                jump .handguns

            "I think we can wrap this up.":
                jump .finish


        label .question1:
            d "I... I..."
            a "Easy..."
            d "... I hated that stupid job!"
            d "Felicien wanted us to do all these sinful things! I've never been so ashamed in my life."
            a "You mind if I ask what things?"
            d "I hardly dare say...! Flirtation, handholding..."
            "He takes a flustered moment."
            d "... And then when it inevitably went wrong, he didn't do a thing about it. So {i}I{/i} had to. It's okay if you don't understand. I'm horrible. No one else would..."
            a "... And that's when you shot the place up."
            "He nods, defeated."
            d "Some terrible bloodlust came over me..."
            a "That's okay, we hear that all the time. We'll get it all sorted."

            $ DQ1Asked = True
            jump interrogateDomani


        label .question2:
            d "Oh, um..."
            a "Just curious. Seems like the kind of thing some criminal higher-up would wear. But you seem alright."
            d "No, it's not that..."
            "He sounds embarrassed."
            a "Well, that's good. If you were that kind of scary guy, I wouldn't stand a chance."
            d "W... what do you mean? In combat?{w} But you're polizia, aren't you?"
            a "Carabinieri."
            d "That's even worse!"
            d "Even here in military custody, I can't be stopped from killing people..."
            a "Hey, don't worry. I'm not the only one here. And they took your guns, right?"
            d "Yes... {p}But..."
            a "Are you ripped, too?"
            d "Not... exactly?"
            a "Sounds like you're good, then. Unless you have some secret power you're hiding from us. Which I'd like to see."
            d "Oh."
            "He crosses himself."
            d "God save us..."

            $ DQ2Asked = True
            jump interrogateDomani


        label .mask:
            a "Looks like they took this from you. And, uh, you don't seem too happy without it."
            d "Oh... oh, thank God!"
            "He turns away to quickly and nimbly afix the mask to his face. Once it's on, he breathes a sigh of relief and seems to calm somewhat."

            $ playerInventory.remove("Venetian Mask")
            jump interrogateDomani


        label .handguns:
            a "These yours?"
            "He cringes back from the guns and doesn't take them from you."
            d "Oh. I... can't. I'll kill again.. Please, I don't care what you do with them. I don't deserve them anymore."
            a "Oooookay. Well."
            "He stares at them longingly. Hard to blame him. They're gorgeous puppies, with flower designs burned into the wood handles. You... keep them, I guess."

            jump interrogateDomani


        label .finish:
            d "When will I be going to my execution?"
            a "Probably in a week. Maybe two. Things are kinda slow-going around here."
            "He looks down."
            d "... Okay."
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
        v "I'm inclined to accept, if you cover your ass well enough. {w}And my buddies?"
        a -closed "Oh. Yeah, I can do that."
        v smirk "Cool. If you're looking for another job after, my boss might have something for you."
        v "Let's get you those cigarettes, hm? My coin is yours."
        a @ smile "Okay."

        if (VKnivesPickedUp == True or VPhotoPickedUp == True):
            call .itemMenu from _call_interrogateVal_itemMenu

        "Okay, cool. You go to the convenience store where Val buys you a new pack of cigarettes and tells you that they have some getaway driver they'll go fetch."
        "Guess they'll be fine? Anyway, you return alone to the comando stazione."

        $ canBreakout = True
        jump notes


        label .itemMenu:
            menu:
                "You have some of their stuff. If you want to give it back, this is your last chance."

                "Give back their knives." if (VKnivesPickedUp == True and VKnivesReturned == False):
                    jump .knives
                
                "Give back their photo." if (VPhotoPickedUp == True and VPhotoReturned == False):
                    jump .photo
                
                "It's better to hold onto this for now.":
                    return


        label .knives:
            "You give back their knives"

            $ playerInventory.remove("Too Many Knives")
            $ VKnivesReturned = True

            if (VPhotoPickedUp == True and VPhotoReturned == False):
                jump .itemMenu
            
            return


        label .photo:
            a "Oh, hey, by the way..."
            "When you take the photo out of your pocket, you watch their eyes light on it with recognition."
            a "You can have this back."
            v "Oh, shit.{p}... Thanks."
            "They take it from your hand and look at it for a minute."
            a "I dunno why they'd hold onto something like that. I guess just for, y'know, ID..."
            v "Yeah.{p}Fair enough, it {i}is{/i} family."
            v "..."
            v "Did anyone else get a look at this?"
            a "Well, I don't know. Obviously, whoever took it from you, but..."
            a "... But there's no saying if they actually ID'd anyone from it."
            v "Yeah, I guess not."
            "They quickly disappear it with some kind of sleight of hand thing."
            v "Well, thanks for giving it back."
            a "'Course."

            $ playerInventory.remove("Water-Damaged Photo")
            $ VPhotoReturned = True

            if (VKnivesPickedUp == True and VKnivesReturned == False):
                jump .itemMenu
            
            return


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
            
            "Give back his cool weapon." if LGunPickedUp == True:
                jump .weapon
            
            "Give back his cash. Wait, what?!" if LCashPickedUp == True:
                jump .cash

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

            $ LQ1Asked = True
            jump interrogateLuci


        label .question2:
            l "..."
            l "......."
            l "................."
            l "............................ A night club."
            a "No way. It's not the one on .. god, what was it.... "
            "Now you can't remember the STREET name, but you CAN remember..."

            show black
            with fade

            """
            You visited almost on a whim some boring night. You only recently realized it was even there, so you decided to scope it out.

            It didn't seem too loud or crowded like they always are on a Friday night; swirling with lights and sounds and conversation, all so much you could hardly focus on anything.
            
            This one was quiet, nearly empty.{w} And let's be real: it was ass.
            
            Even now, focusing with all your pathetic brain power, you can't even remember who was sitting with you. What overwhelmingly dominates is...
            """
            f "What the fuck do I pay you for?"
            "... Up on the shitty little stage they had sat on one end of the room."
            f "You're under my jurisdiction now. We have paying customers. So you get up there and put on a show for them."
            l "I. Will. Not."
            "He grabbed Luciano."
            f "You'll stand up there and sing or I'll open a hole in that pretty little throat. And your daddy will thank me."
            "Even then, his face cold and hard as steel, you couldn't help but think how gorgeous he looked. All angelic justice. Like Michael or something."
            
            hide black
            with fade
            
            a "...I saw you there!"
            "He stares at you in horror."
            l ".. No you didn't."
            "Okay, well, that was just straight lies."
            "But he said it with {i}so much confidence{/i}. He shut you down so hard, all you can think to do is shrug it off and move on."
            "It doesn't matter whether he admits to it or not, anyway."

            $ LQ2Asked = True
            jump interrogateLuci
        

        label .weapon:
            "You give back his handgun."

            $ playerInventory.remove("Sleek Glisenti")
            jump interrogateLuci

        
        label .cash:
            "You give back his money. Why did you pick that option??"

            $ playerInventory.remove("Wad of Cash")
            jump interrogateLuci


        label .finish:
            a "Alright, cool. Thanks. Be seeing you."
            l "..."

            jump notes


    ########################################
    ## Choosing to try them as criminals ###
    # (Bad ending)
    ########################################

    # I actually want to find a good way to eliminate the consequences of bad endings
    # One way of doing that is making this not actually a bad ending
    # But instead the beginning of the secret Quinn route

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
    ## BREAK OUT ###########################
    ########################################

    ## Breaking the suspects out of the stazione

    label breakOut:
        # This could use some rewriting

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
        f "Oh, puppy, you're back.{w} {size=-20}Damn. I was hoping for someone sexier.{/size}"

        hide felicien
        show luci behind grain, reel
        with fade
        l "...{p}...?"
        hide luci

        "You go around to the holding cells of each of the suspects, insert the key, hush them, and quietly release them.{w} Easy."
        "Score. Prisoners rounded up, you lead them to the back entrance, same place criminals get brought in. Guess they can't really be brought through the front where civilians come in."
        scene bg questura front
        show grain
        show reel
        with dissolve
        """
        Everything is going to plan. And it's so quiet in here, maybe your boss went out on patrol?{w} Her office isn't {i}too{/i} close, just gotta creep to the back door...

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
        "It only takes her a moment to look over your little procession and put together what's going on."
        q "Sigh... Couldn't you at least have run this by me first?"
        a "Ahhhhahaha. Whoops."
        "An automobile pulls up to a screesching halt outside, and Felicien's face lights up for a moment."

        hide quinn with dissolve
        show felicien at right behind grain, reel
        f "Thank God {i}someone's{/i} doing their job."
        f "MOVE IT, ASSHOLES!" with vpunch

        menu:
            "She and her little entourage dart outside. You... guess you're supposed to follow them?"

            "Yeah. I'm with them now. If I stay, I'll just be fired anyway.":
                hide felicien
                hide angiolo
                with dissolve

                "You run outside and hop in the automobile."
                jump getaway
            
            "No way, I should stay behind and buy them time.":
                hide felicien
                hide angiolo
                with dissolve

                "Yeah. Yeah. This way, I can even explain myself."
                jump badEnd
    

    ########################################
    ## CAR RIDE AND WOUND TENDING ##########
    ########################################

    ## Getaway drive
    ## Stop at safehouse to figure out next plan and tend to wounded
    ## Drive to Messina and stop there for the night, take ferry next day

    label getaway:
        scene black
        with dissolve

        "There's not enough seats in here!!! Domani yelps as you try to get settled, kind of standing all bent over him."
        "The getaway driver (as you assume her to be) is a hunched, scrawny little lady with sallow skin. Uhhh... is she ill? She also looks at you in alarm when you jump in."

        show kaj at right behind grain, reel with dissolve
        k "Uuuuuhhhhhhhhhhhhhhhhhmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm............................"

        show felicien at left behind grain, reel with dissolve
        f "Get us the fuck out of here."
        "She steps on the gas, and you tumble into Domani's lap so that he shrieks again."
        a "Sorry, dude, I'm sorry."
        d "I've... never felt the touch of a man!"
        "Okay."
        "You brace yourself as firmly against the walls of the automobile as you can as the driver whips around corners, so you only get flung around a little."

        if FDaggerPickedUp == True:
            "Felicien sticks his dagger into the cup holder. He has to fumble and maneuver and hammer it in a bit to fit it between the handguns and the hot pink toy already in there."
            # insert image
            k "Sir, please don't use my car as storage."
            f "Look, I know you're a little {i}bitch{/i}, but in this business you've got to be prepared for anything."
        
        k "..."
        k "So... who's this?"
        f "New fuckbuddy."
        k "Oh."
        "You turn enough to salute her."
        a "Howdy. I'm Angiolo. I'm ditching my job to hang out with you guys."
        k "... My name is Kaj."

        "Soon, the car slows down and you assimilate back into normal traffic."
        k "No one was giving chase. We should be fine."
        k "... Where were we going?"
        f "Are you stupid? We just broke out of military confinement. We're jumping town."
        l "My father will want a report. And we have wounded."
        "He spares Val a momentary glance."
        l "We should stop and regroup before moving on. My family has a safehouse on the edge of town."
        "Felicien gives an angry growl."
        f "You think you override {i}my{/i} authority, wormdick? Remember, your daddy wants {i}you{/i} to listen to {i}me{/i}."
        "Luci's face turns stoney and his eyes glint ferociously, but he shuts the fuck up."
        "Val looks at you sideways. They speak quietly."
        v "Sorry, man. This can't be what you thought you were signing up for."
        a "Eh. You know I was looking to leave that place anyway."
        v "Well, still..."

        ## Arrive at safehouse

        """
        Despite her blustering, Felicien demands Luci give the instructions to the safehouse. He directs in stiff, clipped words.

        You soon stop at a building. You hop out of the car and go inside.

        The place is pretty nice inside. Guess that's what mafia money gets you. As you get settled, Felicien zeroes in on the phone and begins dialing someone up.
        
        You notice Val slump hard against a wall, closing their eyes and seeming to focus on their breathing.{p}They must be in some wicked pain.
        """

        menu:
            "The military gave me some medical training...":
                jump .bandage

            "The best we can do right now is give them some booze.":
                jump .booze

            "They haven't said anything. Leave them be.":
                "If they wanted help, they'd speak up. Otherwise, it's not worth maybe damaging the pride of a mafia member."
                jump .phonecall


        label .bandage:
            a "Hey, you're not looking too good. I might be able to help."
            "Their eyes open and focus on you."
            v "How?"
            a "We learn some stuff about first aid in the Carabinieri. I could at least clean it up and stuff."
            "They look reluctant."
            a "Don't worry. I'm not {i}that{/i} bad at this."
            v "Ha, ha. I'm sure you're great. Just not excited about being poked and prodded."
            a "Yeah, I bet."
            a "But trust me. And if you need me to stop, give a shout."
            "They eye you with equal parts embarrassment and gratitude."
            v "Okay.{w} Thanks."
            a "Aight, be right back."
            "You search the hideout for any supplies you might need, then return to Val. They eye your handful of supplies."
            v "Is that enough?"
            a "Should be. There's some good first aid stuff here, really. But carabinieri teaches you how to improvise, too. Now..."
            "You look them up and down."
            a "Need some help getting that shirt off?"
            v "Guh, no..."
            "They use their good arm to pull it up, exposing a strong chest and surprisingly slender waist. From here, though, how they should move to remove the shirt further is unclear, and you watch them struggle for a bit."
            a "Lemme give you a hand."
            """
            You come forward and take the hem of the shirt from them. You guide their head out first.

            From there you have to be careful of the fabric around the wound, unsticking it where it has been glued down by blood and carefully pulling it out of the hole.{p}They grit their teeth as it comes free.

            Then you remove the shirt the rest of the way and toss it aside.

            Now you can see the bullet wound clearly. At least some of it came out the other side, and the impact looks to have pulverized the surrounding flesh painfully.
            """
            a "Tsss, ouch. This stuff is brutal on you Solari."
            "You reach out a finger to prod the muscle along the outer damage, and they stiffen."
            v "Can you just get this over with?"
            a "Sure thing, boss."
            "You pour some of the alcohol you had seen earlier into a small bowl, and a little bit over the wound. You rinse your hands in the bowl, then turn to Val."
            a "Looks like I'm gonna have to fish around for any bullet or cloth bits."
            "They close their eyes, looking a little ill."
            v "Okay."
            a "You scared?"
            "They shake their head.{p}So, you take their well-muscled arm firmly with one hand."
            a "Ready?"
            """
            They nod once.

            With your other hand, you insert two fingers into the bullet hole. Their flesh is warm and slick.
            
            You slowly press your fingers further in, searching. First Val tenses to rigidity, then they jolt and hiss.
            """
            a "Need me to slow down?"
            v "... Just a little."
            """
            Their voice is strained.

            You return your focus to your work, careful to move slowly, paying close attention to how their body responds.
            
            It's a surprisingly intimate back-and-forth; their muscles tense, and you pause to give them hushed reassurance. When you ask if they're ready to continue, they close their eyes in preparation and nod.

            You feel your way progressively deeper, how their blood coats your fingers wetly, the texture of the walls of the wound pressing in around you. They don't make a sound through the whole thing, except to gasp occasionally.

            Then, you reach it: a thin piece of {i}something{/i} out of place. The way their shirt was sticking, you expected some cloth would've gotten stuck up in there.

            It takes a few tries, the thing's so flopsy and elusive... You eventually do pinch it between your fingers.
            """
            a "Got it. Just a little bit more."
            v "Okay."
            "You draw your fingers out, and with it the bit of cloth. They hiss again as it drags its way out..."
            "And it's free. You inspect it, about an inch square, all stained dark blue with their blood. Your fingers are coated with it, too, almost up to the third knuckle."
            a "There, see? You don't want this stuff festering in there."
            v "Uh huh."
            "Poor guy's panting with the pain, and trying to pretend they're not."
            a "I still gotta clean this up a little and then stitch it..."
            v "Yeah."
            a "... Hangin' in there?"
            v "I fucking hate stitches."
            a "Aha. I'll be gentle, promise."
            """
            Before the stitches, you rinse your hands again, then soak a cloth in the alcohol and use it to carefully wipe away the blood around their wound. There's the easy part.

            Now, prepare the needle and thread. Might as well give all that a quick rinse in alcohol, too, before putting it inside them.

            Then...
            """
            a "I'm gonna start stitching you up now. ... The bullet hole itself is small, it'll be quick."
            """
            They're facing away from you, but they nod, giving you the go ahead.

            You ready yourself to do some super-fast stitching, needle pinched between your fingers. Then, you push it into their skin.
            """
            v "Shit!" with vpunch
            a "Hey, try not to move!"
            v "Try not to be so rough!"
            a "What! That was a normal jab."
            "They huff, seeming a bit embarrassed despite themself."
            v "Fucking hell..."
            """
            You wait for them to get settled again, their eyes squeezed shut.

            You find the best angle to sit at, then get back to stitching. It really is only a few passes of the needle, but they wince every time.
            """
            a "Come on, you're strong enough to walk off a gunshot. You've got this, easy."
            "Finally, you finish up and tie it off, then bite off the tail end of the thread with your teeth."
            a "All done."
            "They open their eyes to look at your handiwork. Uh, well,, it's not {i}bad{/i}..."
            v "... Thanks."
            "They look nauseous."
            a "Yeah. Anytime, I guess?"

            jump day1WrapUp
        

        label .booze:
            "You thought you saw some earlier..."
            "You open some cabinets and rummage through them. Bingo.{p}
            You turn back to Val."
            a "Hey, you're not looking too good."
            "You hold up the bottle."
            a "Want some?{w} It's no laudanum, but..."
            "Their eyes open and focus on the bottle in your hand."

            $ VScore += 1

            v "Where'd you get that, in a place run by Mr. Stickler? Yes, {i}please{/i}."
            "You hand it to them, and they take a mighty swig."
            v "God, you're my favorite person right now, Angiolo."
            a "Haha, hey, you're not too bad yourself. We gotta keep you up and running, right? The best we can, anyway."
            """
            When you look up, you notice Luci staring at you. Why are his eyes always so scary and intense like that?

            And just as you were thinking about saying something, he's turned away again. Yeesh. Okay, then.

            Val's shoulder must be bothering them, because they just keep chugging at that bottle. Eventually, they catch Luci's sidelong glances in both your direction.
            """
            v "What's up, big boy?"
            l "..."
            "They hold up the bottle."
            v "You want some of this?"
            l "... No."
            v "Figures. Fuckin' prick."
            l "..."
            v "You think pretty highly of yourself, huh?"
            l "...."
            v "That station of yours taste pretty good, mafia boy?"
            l "....."
            v "How can you be in this business, anyway?"
            "They tick off on their fingers."
            v "You don't kill, you don't do the job your boss gives you, you can't help in a medical emergency, and—"
            "They look him up and down."
            v "—I doubt you could hold your own in a fight. So what're you good for?"
            l "............."
            "Is he genuinely hurt by that?"
            a "Hey, maybe it's time for you to lay off the drink a little."
            v "What, am I wrong? What kinda mafia guy doesn't kill? Luc thinks he's special."
            l "....................."
            "He seems to have had enough. He gets up and walks away. {w}Except there aren't really any other rooms in this place, so he just goes to stare at one of the walls."
            a "I think you hurt his feelings."
            v "No way. Luc doesn't have those."

            jump day1WrapUp

        
        label .phonecall:
            "While you adjust to the place, you can't help but overhear Felicien's phone conversation."

            f "Good evening, boss."
            boss "{i}Felicien. I'm surprised to hear your voice. I was under the impression you useless group of baccalà got yourselves imprisoned.{/i}"
            f "We ran into a bit of trouble. Nothing we can't handle."
            boss "{i}Why are you calling, then?{/i}"
            f "We'd be able to handle it a bit better if we had somewhere to stay until the cops are off our asses."
            boss "{i}Do one better: get them off{/i} my {i}ass. Fucking moron.{p}
            What secrets can we expect them to know now?{/i}"
            f "I am {i}not{/i} stupid enough to let anything slip."
            boss "{i}And your team?{/i}"

            "Felicien turns and looks directly at Domani, who's busy rocking in the corner in the fetal position."

            f "If they did, I don't think they should be involved in cosa nostra."
            boss "{i}No. But unfortunately if you want to get anything done in this world, you'll have to work with idiots at some point.{p}
            God fuck it, Felicien. If you want to try to do something right, then get out of Palermo. Tonight.{/i}"
            f "Excuse me?"
            boss "{i}You heard me. You know the damn prime minister and his guys have been out here recently, and they're quickly making an enemy of us.{/i}"
            boss "{i}Since you so badly want to draw attention to yourselves, lead the feds to Reggio. I have a contact you can stay with. A clementine farmer. Get yourselves killed out there, I don't care. My business is here, in the west.{/i}"
            f "I have wounded. I can't cross Sicily tonight."
            boss "{i}All the better. They'll be able to follow the blood trail you leave behind.{/i}{w} Bzzzt..."

            jump day1WrapUp


    label day1WrapUp:
        "Felicien slams the phone back onto its holder."
        f "Fucking great..."
        k "What's wrong?"
        f "What the hell do you think is wrong? Someone in this room fucking outed us to the cops."
        # This is a lie
        "He stares directly at Domani."
        d "W-what?? {i}I{/i} didn't call them!!!!"
        f "Great, so we have multiple fuck-ups in here. Whatever. We're jumping. Back in the car, {i}now{/i}."

        ## Car from Palermo along the coast of Sicily to Messina takes ~3 hours
        "Alright, well, you all hop in the car. There's still not enough room for everyone."
        f "Domani, get in the trunk."
        d "Huh?"
        f "Are you deaf? Did you huwt youw eaws in the shootout YOU fucking caused? GET IN THE TRUNK."
        "Domani obediently gets in the trunk, and Felicien slams it shut. You all go on a little roadtrip to a new hideout in Messina, where you get settled in."

    return