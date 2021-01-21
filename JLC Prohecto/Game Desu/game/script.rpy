# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Bobo Smith", image="bobby")
define e = Character("Old Man", image="eugene angry right")
define w = Character("Waiter", image="claire neutral")
define c = Character("Claire", image="claire neutral")
define k = Character("Brock Spear", image="brockoli")
define n = Character("Narrator", image="eugene angry right")
image bobby neutral c = im.FactorScale("images/bobby neutral c.png", 0.7)
image bobby_smiling_c = im.FactorScale("images/bobby_smiling_c.png", 0.7)
image brockoli = im.FactorScale("images/brockoli.png", 0.7)
image bobby neutral c left = Image("images/bobby neutral c.png", xalign=-1.0)
image eugene angry = im.FactorScale("images/eugene angry.png", 0.7)
image eugene angry right = Image("images/eugene angry.png", xalign=1.0)
image claire neutral = im.FactorScale("images/claire neutral.png", 0.7)
image claire excited = im.FactorScale("images/claire excited.png", 0.7)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene house1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show bobby_smiling_c with dissolve

    # These display lines of dialogue.

    b "Hi My Name is Bobby (Watashi no namae wa Bobby desu.)"

    b "What is your name? (O-namae wa nan desu ka?)"

    $ player_name = renpy.input("What is your name? ")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Bobo"
    b "I am very glad to meet you, %(player_name)s! (Oaidekite ureshī desu, %(player_name)s!)"

    b "Today i will take you on a tour of Japan where along the way you will learn japanese. (Kyō wa, nihongo o manabu Nihon tsuā ni go an'nai shimasu.)"

    b "Lets Go To The First Place!(Somosomo ikou)"
    
    hide bobby neutral c
    scene street
    with dissolve
    show bobby neutral c
    with dissolve

    b "A few more minutes and we should be almost-(Ato sū-bu de, hobo)"

    hide bobby neutral c
    show eugene angry
    with vpunch

    e "*An old man yoinks your hand sanitizer*" 

    hide eugene angry
    show bobby neutral c
    with dissolve

    b "HEY come back here with my friends hand sanitizer(Tomodachi no shushi shōdoku-zai o motte koko ni modotte kite ne)"

    hide bobby neutral c
    with dissolve
    show eugene angry
    
    e "*old man runs off laughing like a leprechaun*"

    hide eugene angry
    show bobby neutral c
    with dissolve

    b "Sorry about that, %(player_name)s ill get you a new hand sanitizer later for now lets keep going."

    hide bobby neutral c
    scene black
    with dissolve

    n "About half an hour later..."

    scene bar
    with dissolve
    
    n "You sit down at a table and a waiter walks up"

    show claire neutral
    with dissolve

    w "Irasshaimase, Nihonshu wa ikagadesu ka?"

    $ player_sake = renpy.input("Irasshaimase, Nihonshu wa ikagadesu ka?(Answer in Japanese)")

    $ player_sake = player_sake.strip()

    if player_sake == "":
        n "Wrong, Now you have to learn! HA"    
        jump gay
    elif player_sake == "Hai":
        n "You did it, Now you dont have to learn! YEEEEEAAAA"
        jump lesbo 
    else:
        n "Wrong, Now you have to learn! HA"   
        jump gay    

    # This ends the game.

    return


label gay:

    hide claire neutral
    show claire excited
    with dissolve

    w "Oh a foreigner that doesnt know japanese!?!? Ive always wanted to teach a foreigner japanese!(Ā, nihongo ga wakaranai gaikoku hito! ? ! ? Watashi wa itsumo gaikoku hito ni nihonjin o oshietai to omotte imashita!)"

    hide claire excited
    show bobby neutral c
    with dissolve

    b "Well thats just what we are looking for! Please teach them the basics while i take this call outside.(Sore ga watashitachi ga sagashite iru monodesu! Watashi ga kono denwa o sotonidasu-kan, karera ni kihon o oshietekudasai.)"

    hide bobby neutral c
    show claire excited
    with dissolve

    w "Hello is konichiwa and good evening is konbawa. The way to ask someones name is O-namae wa nan desu ka?"

    w "The way to say who is that in japanese is Kore wa dare desu ka?"
    
    w "Also who are you in Japanese is Anata wa dare desu ka?"
    
    w "Next what is this in Japanese is Kore wa nan desu ka?"
    
    w "Then what is that in Japanese is Are wa nan desu ka?"
    
    w "Finally when are you going in Japanese is Itsu iku no?"
    
    n "Bobo comes back"

    b "We have to leave now because i have to go to a business meeting in a couple of hours so we have to go to the final place asap! Thank you Waitress for the help!"

    
    jump lesbo

    return

label lesbo:

    hide claire neutral
    scene black
    with dissolve

    n "After going to the bar you and Bobo go to a nearby park called Rinshinomori Park"
    
    scene park1
    with dissolve

    n "You and Bobo see an bald Japanese man yelling at a kid"

    scene park2
    show brockoli:
        xalign 1.0
        yalign 1.0
    with dissolve

    $ player_brock = renpy.input("You go up to the man and try to ask, in Japanese: Hello what is your name?")

    $ player_brock = player_brock.strip()

    if player_brock == "":
        n "Wrong, You get beaten up by the old japanese nationalist for not knowing Japanese"    
    elif player_brock == "Konichiwa O-namae wa nan desu ka?":
        n "You said it correctly!"
        jump correctobrockoli 
    elif player_brock == "Konichiwa O-namae wa nan desu ka":
        n "You said it correctly!"
        jump correctobrockoli 
    elif player_brock == "Konichiwa, O-namae wa nan desu ka":
        n "You said it correctly!"
        jump correctobrockoli 
    elif player_brock == "Konichiwa, O-namae wa nan desu ka?":
        n "You said it correctly!"
        jump correctobrockoli 
    else:
        n "Wrong, You get beaten up by the old japanese nationalist for not knowing Japanese"

    return

label correctobrockoli:

    scene park2
    show brockoli:
        xalign 1.0
        yalign 1.0
    with dissolve

    $ player_brocko = renpy.input("You go up to the man and try to ask, in Japanese: Hello what is your name?")

    $ player_brocko = player_brocko.strip()

    if player_brocko == "":
        n "Wrong, You get beaten up by the old japanese nationalist for not knowing Japanese"    
    elif player_brocko == "Konichiwa O-namae wa nan desu ka?":
        n "You said it correctly!"
        jump correctobrockoli 
    elif player_brocko == "Konichiwa O-namae wa nan desu ka":
        n "You said it correctly!"
        jump correctobrockoli 
    elif player_brocko == "Konichiwa, O-namae wa nan desu ka":
        n "You said it correctly!"
        jump correctobrockoli 
    elif player_brocko == "Konichiwa, O-namae wa nan desu ka?":
        n "You said it correctly!"
        jump correctobrockoli 
    else:
        n "Wrong, You get beaten up by the old japanese nationalist for not knowing Japanese"

    return
