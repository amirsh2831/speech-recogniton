import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

sample_rqate, data = wav.read('../samples/sara.wav')
frame_size = 1024

zcr = []

if (len(data.shape) == 2):
    data = np.mean(data, axis=1)

num_frames = (len(data) - frame_size) // (frame_size // 2) + 1
print("num_frames: ", num_frames)

for i in range(num_frames):
    start = i * (frame_size // 2)
    end = start + frame_size
    frame = data[start:end]
    z = 0
    for a in range(1, len(frame)):
        if (frame[a] * frame[a-1] < 0): 
            z += 1
        elif (frame[a] * frame[a-1] == 0):
            if (frame[a] * frame[a-2] < 0):
                z += 1

    zcr.append(z)


plt.figure(figsize=(10, 6))
plt.plot(np.arange(num_frames), zcr)
plt.title('ZCR (sara.wav)')
plt.xlabel('frame')
plt.ylabel('zero crossings')
plt.grid(True)
plt.show()
