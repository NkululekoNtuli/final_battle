from termcolor import colored
from player import Player
from boss import Boss
import time
import random
import pyttsx3


engine = pyttsx3.init()

def get_intro():
    with open("intro.txt", "r") as f:
        file = f.read()
    return file


def get_outro():
    with open("outro.txt", "r") as f:
        file = f.read()
    return file


def creat_player():
    hero = Player(input("Enter your name hero: "),
        int(input("Skills:\n1>> Punch\n2>> Healing\n3>> Rooting\n4>> Blinding\n5>> Draining\n6>> Deaflecting\n7>> Stun\n8>> Laser\nEnter number of skill you want to choose for primary skill: ")),
        int(input("Enter number of skill you want to choose for secondary skill: ")),
        int(input("Enter number of skill you want to choose for ultimate skill: ")))
    return hero

def fight(hero, boss):
    while hero.hp > 0 or boss.hp > 0:
        print("Your turn")


def style_output():
    text = "my name  is nkululeko"

    for l in text:
        print(l, end='', flush=True)
        time.sleep(0.1)
    print("\n")

def main():
    hero = creat_player()
    #Must implement changing player attributes in main function instead of player class
    print()
    Boss.set_hp(50)
    hero.damage_delt = 100 - Boss.hp

    if hero.damage_delt > 33 and hero.damage_delt <= 66:
        hero.hp += 10  #Current Health (float so division doesn't make an int)
        hero.max_hp += 10
        hero.dps += 1
        hero.mp += 1
        hero.level += 1

    elif hero.damage_delt > 66:
        hero.hp += 40  #Current Health (float so division doesn't make an int)
        hero.max_hp += 40
        hero.dps += 3
        hero.mp += 3
        hero.level += 1

    print(hero)
    print(Boss.hp)
    # print(Boss.get_boss_info())
    # engine.say(f"{get_intro()} great hero {colored(hero.name, 'green')}")
    # engine.runAndWait()


if __name__ == "__main__":
    main()
