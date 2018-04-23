#!/usr/bin/env python
import os
import glob
while True:
    files = glob.glob("SoundB*.wav")
    for file in files:
        os.rename(file,"SoundB.wav")

