from termcolor import colored
from boss import Boss

class Player:
    healthDashes = 20
    health_bar = ""
    def __init__(self, name="Player", skill1=1, skill2=2, skill3=7):
        self.damage_delt = Boss.max_hp - Boss.hp
        self.name = name
        self.tank = False
        self.evade = False
        self.skill_dict = {"Laser Beam": 15, "Atomic Blast": 30, "Energy Blast": 10, 
                           "Stun": 7, "Bleed": 5, "Blind": 5, "Heal": 10}
        self.skills = ["Laser Beam", "Atomic Blast", "Energy Blast", "Stun", "Bleed", "Blind", "Heal"]
        self.skill1 = skill1
        self.skill2 = skill2
        self.skill3 = skill3
        self.hp = 100  
        self.max_hp = 100
        self.mp = 100
        self.level = 1


    @property
    def evade(self):
        return self._evade
    

    @evade.setter
    def evade(self, b):
        self._evade = b


    @property
    def tank(self):
        return self._tank
    
    @tank.setter
    def tank(self, b):
        self._tank = b

    @property
    def damage_delt(self):
        return self._damage_delt
    
    @damage_delt.setter
    def damage_delt(self, dmg):
        self._damage_delt = dmg

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, string):
        if not string:
            self._name = "Player"
        else:
            self._name = string

    @property
    def skill1(self):
        return self._skill1
    
    @skill1.setter
    def skill1(self, skill):
        if skill.isdigit():
            if int(skill) > 0 and int(skill) < 8:
                self._skill1 = self.skills[int(skill) - 1]
            else:
                self._skill1 = self.skills[1 - 1]
        else:
            self._skill1 = self.skills[1 - 1]

    @property
    def skill2(self):
        return self._skill2
    
    @skill2.setter
    def skill2(self, skill):
        if skill.isdigit():
            if int(skill) > 0 and int(skill) < 8:
                self._skill2 = self.skills[int(skill) - 1]
            else:
                self._skill2 = self.skills[2 - 1]
        else:
            self._skill2 = self.skills[2 - 1]

    @property
    def skill3(self):
        return self._skill3
    
    @skill3.setter
    def skill3(self, skill):
        if skill.isdigit():
            if int(skill) > 1 and int(skill) < 8:
                self._skill3 = self.skills[int(skill) - 1]
            else:
                self._skill3 = self.skills[7 - 1]
        else:
            self._skill3 = self.skills[7 - 1]


    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, v):
        self._hp = v

    @property
    def max_hp(self):
        return self._max_hp
    
    @max_hp.setter
    def max_hp(self, v):
        self._max_hp = v
    
    @property
    def mp(self):
        return self._mp 
    
    @mp.setter
    def mp(self, v):
        self._mp = v
    
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, v):
        self._level = v
    

    @property
    def health_bar(self):
        dashConvert = int(self.max_hp/self.healthDashes) 
        currentDashes = int(self.hp/dashConvert)  
        remainingHealth = self.healthDashes - currentDashes  
        healthDisplay = '-' * currentDashes  
        remainingDisplay = ' ' * remainingHealth  
        percent = str(int((self.hp/self.max_hp)*100)) + "%"  

        health_bar = f"|{healthDisplay}{remainingDisplay}| {percent}"

        if self.hp < 15:
            return colored(health_bar, 'light_red')
        else:
            return colored(health_bar, 'light_green')
        

    def __str__(self):
        if self.hp < 15:
            return f"Player name: {self.name}\nPlayer level: {colored(self.level, 'yellow')}\nPlayer skill1: {self.skill1}\nPlayer skill2: {self.skill2}\nPlayer skill3: {self.skill3}\nPlayer health: {colored(self._hp, 'light_red')}\nPlayer MP: {self.mp}\n dmf dealt: {self._damage_delt}"
        else:
            return f"Player name: {self.name}\nPlayer level: {colored(self.level, 'yellow')}\nPlayer skill1: {self.skill1}\nPlayer skill2: {self.skill2}\nPlayer skill3: {self.skill3}\nPlayer health: {colored(self._hp, 'light_green')}\nPlayer MP: {self.mp}\n dmf dealt: {self._damage_delt}"
