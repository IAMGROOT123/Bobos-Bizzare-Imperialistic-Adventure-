# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Bobby Smith", image="bobby")
define b = Character("Bobby Smith", image="bobby")
image bobby neutral c = im.FactorScale("images/bobby neutral c.png", 0.7)


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



    # This ends the game.

    return
