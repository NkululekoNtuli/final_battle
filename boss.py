class Boss:
    boss_name = "Some cool sounding name"
    skill1 = "laser Beam"
    skill2 = "Bleed"
    skill3 = "Stun"
    skill4 = "Deflect"
    hp = 100
    mp = 50
    dps = 50

    @classmethod
    def get_boss_info(cls):
        
        return (f"Demo king: {cls.boss_name}\nSkill: {cls.skill1} \nSkill: {cls.skill2} \nSkill: {cls.skill3} \nSkill: {cls.skill4}\nHealth: {cls.hp} \nMagic Power: {cls.mp} \nDps: {cls.dps}")

    @classmethod
    def set_hp(cls, damage):
        cls.hp -= damage