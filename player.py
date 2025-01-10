from termcolor import colored
from boss import Boss

class Player:
    def __init__(self, name="Player", skill1=0, skill2=1, skill3=2):
        self.damage_delt = 0
        self.name = name
        self.skills = ["Laser Beam", "Atomic Blast", "Energy Blast", "Stun", "Deflect", "Bleed", "Blind", "Root", "Heal"]
        self.skill1 = self.skills[skill1 - 1]
        self.skill2 = self.skills[skill2 - 1]
        self.skill3 = self.skills[skill3 - 1]
        self.hp = 100  #Current Health (float so division doesn't make an int)
        self.max_hp = 100
        self.healthDashes = 20  # Max Displayed in dashes
        self.dps = 2
        self.mp = 100
        self.level = 1


    def __str__(self):
        dashConvert = int(self.max_hp/self.healthDashes)  # Get the number to divide by to convert health to dashes (being 10)
        currentDashes = int(self.hp/dashConvert)  # Convert health to dash count: 80/10 => 8 dashes
        remainingHealth = self.healthDashes - currentDashes  # Get the health remaining to fill as space => 12 spaces
        healthDisplay = '-' * currentDashes  # Convert 8 to 8 dashes as a string:   "--------"
        remainingDisplay = ' ' * remainingHealth  # Convert 12 to 12 spaces as a string: "            "
        percent = str(int((self.hp/self.max_hp)*100)) + "%"  # Get the percent as a whole number

        health_bar = f"|{healthDisplay}{remainingDisplay}| {percent}"
        if self.hp < 15:
            return f"Player name: {self.name}\nPlayer level: {colored(self.level, 'yellow')}\nPlayer skill1: {self.skill1}\nPlayer skill2: {self.skill2}\nPlayer skill3: {self.skill3}\nPlayer health: {colored(health_bar, 'light_red')}\nPlayer DPS: {self.dps}\nPlayer MP: {self.mp}"
        else:
            return f"Player name: {self.name}\nPlayer level: {colored(self.level, 'yellow')}\nPlayer skill1: {self.skill1}\nPlayer skill2: {self.skill2}\nPlayer skill3: {self.skill3}\nPlayer health: {colored(health_bar, 'light_green')}\nPlayer DPS: {self.dps}\nPlayer MP: {self.mp}"
