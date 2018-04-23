# -*- coding: utf-8 -*-
"""
Created on Sat April 21 19:21:03 2018

@author: HALO TITAN
"""

from __future__ import division
import numpy as np
from scipy.io.wavfile import read
from LBG import EUDistance
from mel_coefficients import mfcc
from LPC import lpc
from train import training
import os
import glob
import sys

#nSpeaker = 3
nfiltbank = 12
orderLPC = 15
(codebooks_mfcc, codebooks_lpc) = training(nfiltbank, orderLPC)
directory = os.getcwd() + '/test'
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
    
"""
for i in range(nSpeaker):
    fname = '/s' + str(i+1) + '.wav'
    print ('Now speaker ', str(i+1), 'features are being tested')
    (fs,s) = read(directory + fname)
    print (directory+fname)
    mel_coefs = mfcc(s,fs,nfiltbank)
    lpc_coefs = lpc(s, fs, orderLPC)
    sp_mfcc = minDistance(mel_coefs, codebooks_mfcc)
    sp_lpc = minDistance(lpc_coefs, codebooks_lpc)
"""
def namaorang (sp_mfcc):    
    if ((sp_mfcc+1) <= 4):
        b = 'belva'
    elif ((sp_mfcc+1) > 4) and ((sp_mfcc+1) <= 8):
        b = 'ary'
    elif ((sp_mfcc+1) > 8) and ((sp_mfcc+1) <= 12):
        b = 'vesa'
    elif ((sp_mfcc+1) > 15) and ((sp_mfcc+1) <= 18):
        b = 'ary (rekam python)'
    elif ((sp_mfcc+1) > 18) and ((sp_mfcc+1) <= 21):
        b = 'belva (rekam python)'#b = 'astrid'
    elif ((sp_mfcc+1) > 21) and ((sp_mfcc+1) <= 24):
        b='ary (python hujan)'#b = 'donigo'
    elif ((sp_mfcc+1) > 24) and ((sp_mfcc+1) <= 27):
        b = 'evan'
    elif ((sp_mfcc+1) > 27) and ((sp_mfcc+1) <= 30):
        b = 'fara'
    elif ((sp_mfcc+1) > 30) and ((sp_mfcc+1) <= 33):
        b = 'fiqi'
    elif ((sp_mfcc+1) > 33) and ((sp_mfcc+1) <= 36):
        b = 'ian'
    elif ((sp_mfcc+1) > 36) and ((sp_mfcc+1) <= 39):
        b = 'ingmar'
    elif ((sp_mfcc+1) > 39) and ((sp_mfcc+1) <= 42):
        b = 'ipin'
    elif ((sp_mfcc+1) > 42) and ((sp_mfcc+1) <= 45):
        b = 'muchtar'
    elif ((sp_mfcc+1) > 45) and ((sp_mfcc+1) <= 48):
        b = 'rickwin'
    elif ((sp_mfcc+1) > 48) and ((sp_mfcc+1) <= 51):
        b = 'rio'
    elif ((sp_mfcc+1) > 51) and ((sp_mfcc+1) <= 54):
        b = 'tsaqif'
    elif ((sp_mfcc+1) > 54) and ((sp_mfcc+1) <= 57):
        b = 'ary baru'
    elif ((sp_mfcc+1) > 57) and ((sp_mfcc+1) <= 60):
        b = 'belva baru'
    elif ((sp_mfcc+1) > 60) and ((sp_mfcc+1) <= 63):
        b = 'vesa baru'
    return b
    #print ('Speaker ', (i+1), ' in test matches with speaker ', b, (sp_mfcc+1), ' in train for training with MFCC')
    #print ('Speaker ', (i+1), ' in test matches with speaker ', b, ' in train for training with LPC')

def test1234():
    list_of_files = glob.glob('D:/FTP/speaker/*.wav') 
    latest_file = max(list_of_files, key = os.path.getmtime)
    #print latest_file
    stamp = latest_file
    #print (latest_file)
    print (stamp)
    (fs,s) = read(stamp)
    mel_coefs = mfcc(s,fs,nfiltbank)
    lpc_coefs = lpc(s, fs, orderLPC)
    sp_mfcc = minDistance(mel_coefs, codebooks_mfcc)
    sp_lpc = minDistance(lpc_coefs, codebooks_lpc)
    b = namaorang(sp_mfcc)
    print ('Speaker ', (stamp), ' in test matches with speaker ', b, (sp_mfcc+1), ' in train for training with MFCC')


"""  
    if i == sp_mfcc:
        nCorrect_MFCC += 1
    if i == sp_lpc:
        nCorrect_LPC += 1
"""    
"""
percentageCorrect_MFCC = (nCorrect_MFCC/nSpeaker)*100
print 'Accuracy of result for training with MFCC is ', percentageCorrect_MFCC, '%'
percentageCorrect_LPC = (nCorrect_LPC/nSpeaker)*100
print 'Accuracy of result for training with LPC is ', percentageCorrect_LPC, '%'    
"""