import random
from termcolor import colored
import pyttsx3


engine = pyttsx3.init()

class Player:
    def __init__(self, name="Player", skill1=0, skill2=1, skill3=2):
        self.name = name
        self.skill1 = ["laser", "stun", "deflect", "drain", "blind", "root", "heal", "summoning", "punch"][skill1 - 1]
        self.skill2 = ["laser", "stun", "deflect", "drain", "blind", "root", "heal", "summoning", "punch"][skill2 - 1]
        self.skill3 = ["laser", "stun", "deflect", "drain", "blind", "root", "heal", "summoning", "punch"][skill3 - 1]
        self.hp = 100 # Current Health (float so division doesn't make an int)
        self.max_hp = 100
        self.healthDashes = 20  # Max Displayed dashes
        self.dps = 2
        self.mp = 5


    def __str__(self):
        dashConvert = int(self.max_hp/self.healthDashes)            # Get the number to divide by to convert health to dashes (being 10)
        currentDashes = int(self.hp/dashConvert)              # Convert health to dash count: 80/10 => 8 dashes
        remainingHealth = self.healthDashes - currentDashes       # Get the health remaining to fill as space => 12 spaces
        healthDisplay = '-' * currentDashes                  # Convert 8 to 8 dashes as a string:   "--------"
        remainingDisplay = ' ' * remainingHealth             # Convert 12 to 12 spaces as a string: "            "
        percent = str(int((self.hp/self.max_hp)*100)) + "%"     # Get the percent as a whole number:   40%

        health_bar = f"|{healthDisplay}{remainingDisplay}| {percent}"
        if self.hp < 15:
            return f"Player name: {self.name}\nPlayer skill1: {self.skill1}\nPlayer skill2: {self.skill2}\nPlayer skill3: {self.skill3}\nPlayer health: {colored(health_bar, 'light_red')}\nPlayer DPS: {self.dps}\nPlayer MP: {self.mp}"
        else:
            return f"Player name: {self.name}\nPlayer skill1: {self.skill1}\nPlayer skill2: {self.skill2}\nPlayer skill3: {self.skill3}\nPlayer health: {colored(health_bar, 'light_green')}\nPlayer DPS: {self.dps}\nPlayer MP: {self.mp}"


class Boss:
    boss_name = "Some cool sounding name"
    skill1 = "laser"
    skill2 = "beam"
    skill3 = "stun"
    skill4 = "deflect"
    hp = 100
    mp = 50
    dps = 50

    @classmethod
    def get_boss_info(cls):
        
        return (f"Demo king: {cls.boss_name}\nSkill: {cls.skill1} \nSkill: {cls.skill2} \nSkill: {cls.skill3} \nSkill: {cls.skill4}\nHealth: {cls.hp} \nMagic Power: {cls.mp} \nDps: {cls.dps}")


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
        int(input("Skills:\n1>> Punch\n2>> Summoning\n3>> Healing\n4>> Rooting\n5>> Blinding\n6>> Draining\n7>> Deaflecting\n8>> Stun\n9>> Laser\nEnter number of skill you want to choose for primary skill: ")),
        int(input("Enter number of skill you want to choose for secondary skill: ")),
        int(input("Enter number of skill you want to choose for ultimate skill: ")))
    return hero

def fight(hero, boss):
    while hero.hp > 0 or boss.hp > 0:
        print("Your turn")




def main():

    hero.hp = 5
    print(hero)
    # print(Boss.get_boss_info())
    # engine.say(f"{get_intro()} great hero {colored(hero.name, 'green')}")
    # engine.runAndWait()


if __name__ == "__main__":
    main()
