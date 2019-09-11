from gtts import gTTS

import os

text_en = "Bartek is the best"
text = "Bartek jest gość"

output_pl = gTTS(text=text, lang='pl')

output_en = gTTS(text=text_en)

output_en.save('bartek_en.mp3')
output_pl.save('bartek_pl.mp3')

from pygame import mixer

mixer.init()
mixer.music.load('bartek_pl.mp3')
mixer.music.play()