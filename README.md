# PROJECT TITLE: final_battle

    #### Video Demo:  <URL HERE>
    #### Description:

    The final_battle.py program is a short and simple text-based game where a player has to create their character and select their preferred abilities/skills to fight the npc/boss with. It uses a turn-based system  to determain who is supposed to make a move.

    The program contains three folder in the root directory, Audio, Img, and Text. The Audio folder stores the audio file that is used in the program as wav formate, when the boss is wins agints the player. The Img folder stores an image of the boss used in the program as png formate, this image is displayed after the fight starts. The Text folder stores txt files that are displayed to give a brief scenario of the "story",  display scertain lines that the boss would reply with if scertain moves/abilities are used by the player, display skill/ablility information so the player has an idea of what the skills/abilities do, display text to conclude the "story" if the player defeats the boss.

    The boss.py file contains a class that is used to create the boss which is imported in project.py. The class does not have a constructer method as there only needs to be one boss. The class has eight class variables that describe the attributes of the boss. Three class methods, the get_boss_info returns the bosses information as a string, the get_hp returns the bosses health as a integer and the set_hp changes the value of the bosses health.

    The player.py file contains a class that is used to create a player object. The player class has two class variables that are used when displaying the player health bar. The class has a constructor method that takes 3 arguments for player name, skill1, skill2, skill3 and thirteen instance variables that relate to the player from their name,skills,health, magic power and level. The class aslso has corrisponding setters and getters for the objects attributes. Some setters and getters are redundents as they dont have a purpose but were implemented to get use to the idea of setters and getters. The class has a getter method that returns the health bar and a dunder str method to return the player information as a string.
    



    TODO#
    The program runs with python main.py