import sounddevice as sd
import soundfile as sf

#Audio parameters 
duration = 10
fs = 44100


#Capture 
print("Recording... press q to stop")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)

#Wait for finish 
sd.wait()

print("recording finished")

#OUTPUT TO FILE
outputFile = "desktopAudio.wav"
sf.write(outputFile, recording, fs)