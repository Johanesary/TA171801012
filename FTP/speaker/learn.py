import pyaudio
import wave
import chunk

rf = wave.open('output.wav','rb')
print rf.getnchannels()
print rf.getsampwidth()
print rf.getframerate()
print rf.getnframes()
print rf.getparams()

file = open("output.wav","r")
test = chunk.Chunk(file,align=True, bigendian=True, inclheader=False)
print test.getname()
print test.getsize()
print test.tell()

#print rf.writeframes(b''.join(frames))
