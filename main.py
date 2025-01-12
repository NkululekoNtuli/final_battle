from pyfiglet import figlet_format
from pydub.playback import play
from pydub import AudioSegment
from termcolor import colored
from player import Player
from boss import Boss
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import fontstyle
import pyttsx3
import random
import time
 

def get_intro():  #To get intro
    try:
        with open("Text/intro.txt", "r") as f:
            file = f.read()
        return fontstyle.apply(file, 'Italic')
    except FileNotFoundError:
        print("File not found")


def get_boss_lines():
    try:    
        with open("Text/boss_lines.txt" , "r") as f:
            file = f.readlines()
        return file
    except FileNotFoundError:
        print("File not found")


def get_skill_info():
    try:
        with open("Text/skill_info.txt") as f:
            file = f.read()
            return colored(file, 'cyan')
    except FileNotFoundError:
        print("File not found")

def get_outro():  #To get outro
    try:
        with open("Text/outro.txt", "r") as f:
            file = f.read()
        return fontstyle.apply(file, 'Italic')
    except FileNotFoundError:
        print("File not found")


def creat_player():  #To creat player
    hero = Player(input("Enter your name hero: "),
        int(input("Abilities:\n1>> Laser Beam\n2>> Atomic Blast\n3>> Energy Blast\n4>> Stun\n5>> Bleed\n6>> Blind\n7>> Heal\nEnter number of skill you want to choose for primary skill: ")),
        int(input("Enter number of skill you want to choose for secondary skill: ")),
        int(input("Enter number of skill you want to choose for ultimate skill: ")))
    return hero


def style_output(text):  # For displaying into and outro in style
    for l in text:
        print(l, end='', flush=True)
        time.sleep(0.1)
    print("\n")


def display(hero):  #To display boss name and health
    print(f"\n                                            Boss: {colored(Boss.boss_name, 'light_red')}\n         {colored(Boss.get_hp(), 'red')}\nlevel: {colored(hero.level, 'light_green')}                                                                                                      Health: {hero.health_bar}\nHero: {colored(hero.name,'blue')}                                                                                                   Magic power:{colored(hero.mp, 'blue')}\n")


def upgrade_level(hero):  #To upgrade player level
    if Boss.hp < 266 and Boss.hp >= 133:
        Boss.leve1_2 += 1

    elif Boss.hp < 133:
        Boss.level_3 += 1

    if Boss.leve1_2 == 1:
        hero.hp += 20  
        hero.max_hp += 20
        hero.mp += 20
        hero.level += 1

    elif Boss.level_3 == 1:
        hero.hp += 10 
        hero.max_hp += 10
        hero.mp += 10
        hero.level += 1


def display_boss_im():
    ImageItself = Image.open("Img/boss.png")
    ImageNumpyFormat = np.asarray(ImageItself)
    plt.imshow(ImageNumpyFormat)
    plt.draw()
    plt.pause(7) 
    plt.close()


def main():
    engine = pyttsx3.init()
    intro = get_intro()
    outro = get_outro()
    style_output(f"\n{intro}\n")
    print(f"{get_skill_info()}\n")
    hero = creat_player()
    print()
    blind_dmg = 1 
    turn = 0

    while hero.hp > 0 and Boss.hp > 0:

        display(hero)  #To dislay the boss and player stats

        if hero.mp < 7.5:
            print(get_boss_lines()[5])
            print(get_boss_lines()[6])
            print(get_boss_lines()[7])
            hero.hp = hero.hp - 100
            break

        elif Boss.mp < 10:
            print(get_boss_lines()[8])
            print(get_boss_lines()[9])
            print(get_boss_lines()[10])
            break

        elif turn == 0:  #For the first move of the player.
            display_boss_im()
            print(colored(get_boss_lines()[0], 'red'))
            print(colored(get_boss_lines()[1], 'red'))
            print()

            move = int(input("1>> Attack\n2>> Pass\nYour move: ")) 
            print()

            if move == 1:  #Display choices that can be made.
                ability_move = int(input(f"1>> {hero.skill1}\n2>> {hero.skill2}\n3>> {hero.skill3}\nYour move: "))

                if ability_move == 1:
                    if ((ability_move == 1) and (hero.skill1 == "Laser Beam" or hero.skill1 == "Atomic Blast" or hero.skill1 == "Energy Blast" or hero.skill1 == "Bleed")):
                        Boss.set_hp(hero.skill_dict[hero.skill1])
                        hero.mp =   hero.mp - (hero.skill_dict[hero.skill1] * hero.level * 0.5)

                elif ((ability_move == 2) and (hero.skill2 == "Laser Beam" or hero.skill2 == "Atomic Blast" or hero.skill2 == "Energy Blast" or hero.skill2 == "Bleed")):
                    Boss.set_hp(hero.skill_dict[hero.skill2])
                    hero.mp =   hero.mp - (hero.skill_dict[hero.skill2] * hero.level * 0.5)
                    
                elif ((ability_move == 3) and (hero.skill3 == "Laser Beam" or hero.skill3 == "Atomic Blast" or hero.skill3 == "Energy Blast" or hero.skill3  =="Bleed")):
                    print(hero.skill3)
                    Boss.set_hp(hero.skill_dict[hero.skill3])
                    hero.mp =   hero.mp - (hero.skill_dict[hero.skill3] * hero.level * 0.5)

                turn += 2

            else:
                print(colored(get_boss_lines()[14], 'red'))
                print(colored("Malakar used UNDYING RAGE on you", 'yellow'))

                rage_skill = 60
                hero.hp = hero.hp - rage_skill
                Boss.mp = Boss.mp - 80
                Boss.hp = Boss.hp - 200
                turn += 1
                
        elif turn == 1:  #Any other move thats is not the first one.
            move = int(input("1>> Attack\n2>> Evade\n3>> Tank\nYour move: "))
            print()

            if move == 1:
                ability_move = int(input(f"1>> {hero.skill1}\n2>> {hero.skill2}\n3>> {hero.skill3}\nYour move: "))

                # For damaging skills
                if ((ability_move == 1) and (hero.skill1 == "Laser Beam" or hero.skill1 == "Atomic Blast" or hero.skill1 == "Energy Blast" or hero.skill1 == "Bleed")):
                    Boss.set_hp(hero.skill_dict[hero.skill1])
                    hero.mp =   hero.mp - (hero.skill_dict[hero.skill1] * hero.level * 0.5)

                elif ((ability_move == 2) and (hero.skill2 == "Laser Beam" or hero.skill2 == "Atomic Blast" or hero.skill2 == "Energy Blast" or hero.skill2 == "Bleed")):
                    Boss.set_hp(hero.skill_dict[hero.skill2])
                    hero.mp =   hero.mp - (hero.skill_dict[hero.skill2] * hero.level * 0.5)

                elif ((ability_move == 3) and (hero.skill3 == "Laser Beam" or hero.skill3 == "Atomic Blast" or hero.skill3 == "Energy Blast" or hero.skill3  =="Bleed")):
                    print(hero.skill3)
                    Boss.set_hp(hero.skill_dict[hero.skill3])
                    hero.mp =   hero.mp - (hero.skill_dict[hero.skill3] * hero.level * 0.5)

                # For stun 
                elif ((ability_move == 1 ) and ("Stun" == hero.skill1) or 
                      (ability_move == 2 ) and ("Stun" == hero.skill2) or 
                      (ability_move == 3 ) and ("Stun" == hero.skill3)):
                    hero.mp =   hero.mp - (hero.skill_dict["Stun"] * hero.level * 0.5)
                    turn -= 1

                # For blind
                elif ((ability_move == 1 ) and ("Blind" == hero.skill1) or 
                      (ability_move == 2 ) and ("Blind" == hero.skill2) or 
                      (ability_move == 3 ) and ("Blind" == hero.skill3)):
                    hero.mp =   hero.mp - (hero.skill_dict["Blind"] * hero.level * 0.5)
                    blind = random.choice([1, 2, 3])

                    if blind == 1:
                        turn -= 1
                    else:
                        blind_dmg = 2
  
                # For heal
                elif ((ability_move == 1 ) and ("Heal" == hero.skill1) or 
                      (ability_move == 2 ) and ("Heal" == hero.skill2) or 
                      (ability_move == 3 ) and ("Heal" == hero.skill3)):
                    hero.mp =   hero.mp - ((hero.skill_dict["Heal"] * hero.level * 0.5))
                    hero.hp = hero.hp + (hero.level * 15)
                
            elif move == 2:  # For when player wants to evade
                hero.evade = True
                hero.mp =   hero.mp - (hero.skill_dict[hero.skill1] * hero.level * 0.5)
                print()
                print(colored(get_boss_lines()[5], 'red'))
         
            elif move == 3:  #For when player wants to tank
                hero.tank = True
                hero.mp = hero.mp - 10
                print()
                print(colored(get_boss_lines()[4], 'red'))

            upgrade_level(hero)
            turn += 1
        
        elif turn == 2: # for the bosses turn.
            print()
            print(colored(get_boss_lines()[13], 'light_magenta'))
            tank = 1
            evade_dmg = 1
            if hero.tank:
                tank += 3
            else:
                tank = 1

            if hero.evade:
                evade = random.choice([1, 2])
                if evade == 2:
                    turn == 1
                    continue
                else:
                    evade_dmg = 2

            if hero.hp > 90:
                hero.hp = hero.hp - (Boss.skills["Laser Beam"] / blind_dmg / tank / evade_dmg)
                Boss.mp = Boss.mp - (Boss.skills["Laser Beam"] / 2)
                print(colored(f"\nMalakar used Laser Beam on you", 'yellow'))

            else:
                abilities = ["Laser Beam", "Bleed", "Stun", "Cleave", "Hell Fire"]
                active_abilty = random.choice(abilities)

                if active_abilty == "Stun":
                    hero.hp = hero.hp - ((Boss.skills["Stun"] / blind_dmg) / tank / evade_dmg)
                    Boss.mp = Boss.mp - (Boss.skills["Stun"] * 2 )
                    print(colored(f"\nMalakar used Stun on you", 'yellow'))
                    turn += 1

                else:
                    hero.hp = hero.hp - ((Boss.skills[active_abilty] / blind_dmg) / tank / evade_dmg)
                    Boss.mp = Boss.mp - (Boss.skills[active_abilty] * 2)
                    print(colored(f"Malakar used {active_abilty} on you", 'yellow'))

            hero.tank = False  
            hero.evade = False      
            blind_dmg = 1
            tank = 1
            turn -= 1    

    if hero.hp <= 0 or hero.mp < 10:       
        txt_style = colored(figlet_format("GAME OVER!!", font='slant'), 'light_red')
        engine.say("GAME OVER")
        engine.runAndWait()
        song = AudioSegment.from_wav("Audio/I_win.wav")

        play(song)      
        print(txt_style)
        print(hero)
        print()
        print(Boss.get_boss_info())


    else:
        txt_style = colored(figlet_format("YOU WIN!!", font='slant'), 'light_green')
        engine.say(f"you win")
        engine.runAndWait()

        print(txt_style)
        print()
        print(hero)
        print()
        print(Boss.get_boss_info())
        print()
        style_output(outro)


if __name__ == "__main__":
    main()