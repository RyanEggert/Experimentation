import re


audioFileName = 'song1_mod_mel_3.mp3'


splitFileName = re.split("[_\.]", audioFileName)

print splitFileName