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


nSpeaker = 15
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
    
    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    if frames:
        (fs,s) = read('output.wav')
        mel_coefs = mfcc(s,fs,nfiltbank)
        lpc_coefs = lpc(s, fs, orderLPC)
        sp_mfcc = minDistance(mel_coefs, codebooks_mfcc)
        sp_lpc = minDistance(lpc_coefs, codebooks_lpc)
        print (sp_mfcc+1)
        print (sp_lpc+1)
    """
    for i in range(nSpeaker):
        fname = '/s' + str(i+1) + '.wav'
        print 'Now speaker ', str(i+1), 'features are being tested'
        (fs,s) = read(directory + fname)
        mel_coefs = mfcc(s,fs,nfiltbank)
        lpc_coefs = lpc(s, fs, orderLPC)
        sp_mfcc = minDistance(mel_coefs, codebooks_mfcc)
        sp_lpc = minDistance(lpc_coefs, codebooks_lpc)
    
        print 'Speaker ', (i+1), ' in test matches with speaker ', (sp_mfcc+1), ' in train for training with MFCC'
        print 'Speaker ', (i+1), ' in test matches with speaker ', (sp_lpc+1), ' in train for training with LPC'
		
	"""

