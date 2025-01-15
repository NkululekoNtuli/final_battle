class Boss:
    boss_name = "Malakar the Abyssal Warden"
    skills = {"Laser Beam": 20, "Hell Fire": 10, "Cleave": 15, "Stun": 7, "Bleed": 5}
    healthDashes = 100
    hp = 400
    max_hp = 400
    mp = 250
    leve1_2 = 0
    level_3 = 0

    @classmethod
    def get_boss_info(cls):
        return (f"Demo king: {cls.boss_name}\nAbilities: {cls.skills.keys()}\nHealth: {cls.hp} \nMagic Power: {cls.mp}")
    
    @classmethod
    def get_hp(cls):
        dashConvert = int(cls.max_hp/cls.healthDashes) 
        currentDashes = int(cls.hp/dashConvert)  
        remainingHealth = cls.healthDashes - currentDashes  
        healthDisplay = '-' * currentDashes  
        remainingDisplay = ' ' * remainingHealth 
        percent = str(int((cls.hp/cls.max_hp)*100)) + "%"  

        health_bar = f"|{healthDisplay}{remainingDisplay}| {percent}"
        return  health_bar

    @classmethod
    def set_hp(cls, damage):
        cls.hp -= damage