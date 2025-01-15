# PROJECT TITLE: final_battle

    #### Video Demo:  <URL HERE>
    #### Description:

    The final_battle.py program is a short and simple text-based game where a player has to create their character and select their preferred abilities/skills to fight the NPC/boss. It uses a turn-based system to determine who is supposed to make a move. The program contains three folders in the root directory: Audio, Img, and Text. 

    The Audio folder stores the audio file that is used in the program in WAV format when the boss wins against the player. The Img folder stores an image of the boss used in the program in PNG format; this image is displayed after the fight starts. The Text folder stores TXT files that give a brief scenario of the "story," display certain lines that the boss would reply with if certain moves/abilities are used by the player, display skill/ability information so the player has an idea of what the skills/abilities do, and display text to conclude the "story" if the player defeats the boss.
    
    The boss.py file contains a class that is used to create the boss, which is imported in project.py. The class does not have a constructor method as there only needs to be one boss. The class has eight class variables that describe the attributes of the boss. Three class methods: get_boss_info returns the boss's information as a string, get_hp returns the boss's health as an integer, and set_hp changes the value of the boss's health. The player.py file contains a class that is used to create a player object.

    The player class has two class variables that are used when displaying the player health bar. The class has a constructor method that takes three arguments for player name, skill1, skill2, and skill3 and thirteen instance variables that relate to the player
    from their name, skills, health, magic power, and level, the class also has corresponding setters and getters for the object's attributes. Some setters and getters are redundant as they don't have a purpose but were implemented to get used to the idea of setters and getters. The class has a getter method that returns the health bar and a dunder str method to return the player's information as a string. 

    The project.py file is the main file of the program and contains the core functionality that allows the player to create their character and fight the boss. The get_intro, get_boss_lines, get_skill_info, and get_outro functions return the text stored in the intro.txt, boss_lines.txt, skill_info.txt, and outro.txt files. The create_player function prompts the user for a name and abilities to be assigned to the player object and returns that object. The style_output function is used to display specific text as if it is being typed. The display function is simply used to display the player's stats like level, name, health, and magic power. The upgrade_level function is used to increase the player's level when a condition has been met. The display_boss_img function is used to display the boss's image to the player. The main function is responsible for implementing the fight using a turn-based system where the user is prompted for a skill/ability to use against the boss, then the boss would respond with its choice of skill/ability, mainly choosing them randomly. When the player's health, magic power, or the boss's health, magic power is less than a specific value, the function then decides who won the final battle.


    TODO#
    The program runs with python main.py