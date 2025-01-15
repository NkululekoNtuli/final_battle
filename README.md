# PROJECT TITLE: final_battle

    #### Video Demo:  <URL HERE>
    #### Description:

    The final_battle.py program is a short and simple text-based game where a player has
    to create their character
    and select their preferred abilities/skills to fight the npc/boss with. It uses a
    turn-based system  to
    determain who is supposed to make a move.

    The program contains three folder in the root directory, Audio, Img, and Text. The 
    Audio folder stores the
    audio file that is used in the program as wav formate, when the boss is wins agints
    the player. The Img folder
    stores an image of the boss used in the program as png formate, this image is
    displayed after the fight
    starts. The Text folder stores txt files that are displayed to give a brief scenario
    of the "story",  display
    scertain lines that the boss would reply with if scertain moves/abilities are used by the player, display
    skill/ablility information so the player has an idea of what the skills/abilities do, display text to conclude
    the "story" if the player defeats the boss.

    The boss.py file contains a class that is used to create the boss which is imported in project.py. The class
    does not have a constructer method as there only needs to be one boss. The class has eight class variables
    that describe the attributes of the boss. Three class methods, the get_boss_info returns the bosses
    information as a string, the get_hp returns the bosses health as a integer and the set_hp changes the value of
    the bosses health.

    The player.py file contains a class that is used to create a player object. The player class has two class
    variables that are used when displaying the player health bar. The class has a
    constructor method that takes 3 arguments for player name, skill1, skill2, skill3 and thirteen instance variables that relate to the player
    from their name,skills,health, magic power and level. The class aslso has corrisponding setters and getters
    for the objects attributes. Some setters and getters are redundents as they dont have a purpose but were
    implemented to get use to the idea of setters and getters. The class has a getter method that returns the
    health bar and a dunder str method to return the player information as a string.

    The project.py file is the main file of the program and contains the core
    functionality that allows the player create their charecter and firght the boss.
    The get_intro, get_boss_lines, get_skill_info and get_outro function returns
    the text stored in the intro.txt, boss_lines.txt, skill_info.txt and outro.txt file.
    The create_player function prompts the user for name and abilities to be asinged
    to the player object and returns that object. The style_output fucntion is used to display specific text as if it is being typed. The
    display fucntion is simply used to display the players stats like level, name, health and magic power.
    The upgrade_level function is used to increase the players level when a condition has been meet. The display_boss_im fucntion is used to
    display the bosses image to the player.
    The main function is responsable for implementing the fight using a turn based system where the user is promted for a skill/ability to use
    aginst the boss then the boss would respond with its choice to skill/ability, mainly choosing them randomly. When the players health, magic
    power  or the bosses health, magic power is less then a specific value the function then decides who won the final battle.

    TODO#
    The program runs with python main.py