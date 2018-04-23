# -*- coding: utf-8 -*-
"""
Created on Tuesday Feb 27 20:21:03 2018

@author: TITAN
"""

from __future__ import division
import numpy as np
from scipy.io.wavfile import read
from LBG import EUDistance
from mel_coefficients import mfcc
from LPC import lpc
from train import training
import os
import pyaudio
import wave


#nSpeaker = 15
nfiltbank = 12
orderLPC = 15
(codebooks_mfcc, codebooks_lpc) = training(nfiltbank, orderLPC)
directory = os.getcwd() + '/test';
fname = str()
nCorrect_MFCC = 0
nCorrect_LPC = 0


def minDistance(features, codebooks):
    speaker = 0
    distmin = np.inf
    for k in range(np.shape(codebooks)[0]):
        D = EUDistance(features, codebooks[k,:,:])
        dist = np.sum(np.min(D, axis = 1))/(np.shape(D)[0]) 
        if dist < distmin:
            distmin = dist
            speaker = k
            
    return speaker

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "output.wav"



while True:
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    sistem = True
    while (sistem): #go for every seconds
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        peak=np.average(np.abs(data))*2
        #bars="#"*int(50*peak/2**16)
        if peak > 1500:
            frames = []
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)
            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            sistem = False
        #print("%05d %s"%(peak,bars))

    #if frames:
    (fs,s) = read('output.wav')
    mel_coefs = mfcc(s,fs,nfiltbank)
    lpc_coefs = lpc(s, fs, orderLPC)
    sp_mfcc = minDistance(mel_coefs, codebooks_mfcc)
    sp_lpc = minDistance(lpc_coefs, codebooks_lpc)
    #print (frames)

    if ((sp_lpc+1) <= 5):
        b = 'vesa'
    elif ((sp_lpc+1) > 5) and ((sp_lpc+1) <= 10):
        b = 'belva'
    elif ((sp_lpc+1) > 10) and ((sp_lpc+1) <= 15):
        b = 'ary'
    elif ((sp_lpc+1) > 15) and ((sp_lpc+1) <= 18):
        b = 'ali'
    elif ((sp_lpc+1) > 18) and ((sp_lpc+1) <= 21):
        b = 'astrid'
    elif ((sp_lpc+1) > 21) and ((sp_lpc+1) <= 24):
        b = 'donigo'
    elif ((sp_lpc+1) > 24) and ((sp_lpc+1) <= 27):
        b = 'evan'
    elif ((sp_lpc+1) > 27) and ((sp_lpc+1) <= 30):
        b = 'fara'
    elif ((sp_lpc+1) > 30) and ((sp_lpc+1) <= 33):
        b = 'fiqi'
    elif ((sp_lpc+1) > 33) and ((sp_lpc+1) <= 36):
        b = 'ian'
    elif ((sp_lpc+1) > 36) and ((sp_lpc+1) <= 39):
        b = 'ingmar'
    elif ((sp_lpc+1) > 39) and ((sp_lpc+1) <= 42):
        b = 'ipin'
    elif ((sp_lpc+1) > 42) and ((sp_lpc+1) <= 45):
        b = 'muchtar'
    elif ((sp_lpc+1) > 45) and ((sp_lpc+1) <= 48):
        b = 'rickwin'
    elif ((sp_lpc+1) > 48) and ((sp_lpc+1) <= 51):
        b = 'rio'
    elif ((sp_lpc+1) > 51) and ((sp_lpc+1) <= 54):
        b = 'tsaqif'
    elif ((sp_lpc+1) > 54) and ((sp_lpc+1) <= 57):
        b = 'ary baru'

    print 'Speaker in test matches with speaker ', b, ' in train for training with MFCC'
    print 'Speaker in test matches with speaker ', b, ' in train for training with LPC'
    