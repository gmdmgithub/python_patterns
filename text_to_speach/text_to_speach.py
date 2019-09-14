from gtts import gTTS

import os

text_en = "Alex is the best of the best"
text = "Alex est le meilleur des meilleurs"

output_fr = gTTS(text=text, lang='fr')
output_en = gTTS(text=text_en)
output_en.save('alex_en.mp3')
output_fr.save('alex_fr.mp3')

from playsound import playsound
playsound('alex_en.mp3')
playsound('alex_fr.mp3')
