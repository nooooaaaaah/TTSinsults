from multiprocessing.connection import wait
from operator import truediv
from gtts import gTTS
from mpyg321.MPyg321Player import MPyg321Player
import random
from time import sleep
import os 

def random_insult(insults):
    insult = next(insults)
    for num, line in enumerate(insults,2):
        if random.randrange(num):
            continue
        insult = line
    return insult

def speak_insult(insult):
    CHINESE = 'zh-cn'
    ttsObj= gTTS(text=insult, lang=CHINESE, slow=True)
    ttsObj.save("insult.mp3")
    player = MPyg321Player()

    player.play_song('insult.mp3')
    sleep(2)
    
    print(insult)




speak_insult(random_insult(open("insults.txt","r")))
