# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Bobby Smith", image="bobby")
# Eugene Zuckerberg
define e = Character("Old Man", image="eugene angry right")
image bobby neutral c = im.FactorScale("images/bobby neutral c.png", 0.7)
image bobby neutral c left = Image("images/bobby neutral c.png", xalign=-1.0)
image eugene angry = im.FactorScale("images/eugene angry.png", 0.7)
image eugene angry right = Image("images/eugene angry.png", xalign=1.0)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene house1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show bobby neutral c with dissolve

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

    e "EHHHH!?!?!? For goodness sake do you have eyes? (EHHHH!?!?!? Zen no tame ni anata wa me o motte imasu ka?)" 

    show bobby neutral c
    with dissolve
    hide eugene angry

    b "Relax Old man hes a foreigner(Kare wa gaikoku hitodearu rōjin o rirakkusu)"

    hide bobby neutral c
    with dissolve
    show eugene angry
    
    e "*scoffs* Stupid (Baka)"

    hide eugene angry
    with dissolve

    # This ends the game.

    return
