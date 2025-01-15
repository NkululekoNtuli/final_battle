import pytest
from project import get_skill_info, get_intro, style_output
from player import *
from boss import *
import fontstyle

def test_get_skill_info():
    text = "Skills info:\n\nLaser Beam : a damaging attack that deals 15 damage.\nAtomic Blast: a damaging attack that deals 30 damage, deal % damage to the user.\nEnergy Blast: a damaging attack that deals 10 damage.\nStun: keep enemy in place and deals 7 damage.\nBleed: a low level damaging attack that deals 5 damage.\nHeal: a healing skill that heal for % missing health.\nBlind: a % chance of enemy missing or reduced damage.\nEvade: % chance of dodging enemy attack or reduced damage.\nTank: reduced % damage"
    assert get_skill_info() == text
    assert get_skill_info() != "hello world"


def test_get_intro():
    string = "The peacfull town of Alabasta has enjoyed a long lasting peace, however \nit now faces a great threat from the demon known as Malakar the Abyssal Warden.\nMany have tried to rid the town of his presence and many have sucumbe to his greate power.\nAs the greate hero who saved countless lives, cities and towns, Alabasta calls upon you to aid them \nin such difficult times. \nMission: Sunder Malakar's presence from this realm.\nGood luck oh legendary hero!"
    string = fontstyle.apply(string, 'Italic')
    assert get_intro() == string
    assert get_intro() != "INTRO"

def test_style_output():
    text = "hello world"
    assert style_output(text) ==  "hello world"
    assert style_output(text) != "Hello world"