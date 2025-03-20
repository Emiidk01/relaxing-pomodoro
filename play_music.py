import time
from pygame import mixer

mixer.init()

mixer.music.load('wet_hands.mid')

mixer.music.play()

while True:
    time.sleep(0.1)