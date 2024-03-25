import keyboard
import pyaudio 
import wave

# Audio parameters 
chunk = 1024
sample_format = pyaudio.paInt16
channels = 1
fs = 44100

p = pyaudio.PyAudio()

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                input=True,
                frames_per_buffer=chunk)
print("Recording... press q to stop")

#Output to file
output_filename = "audio.wav"
frames = []

#Captures audio and saves it to frames
def recordAudio():
    while True:
        data = stream.read(chunk)
        frames.append(data)


        #press q to stop recording
        if keyboard.is_pressed("q"):
            print("recording finished")
            break


recordAudio()

stream.stop_stream()
stream.close()
p.terminate()
print("recording finished")

#save captured audio
wf = wave.open(output_filename, "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()