import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

sample_rqate, data = wav.read('../samples/sara.wav')
frame_size = 1024

averages = []

if (len(data.shape) == 2):
    data = np.mean(data, axis=1)

num_frames = (len(data) - frame_size) // (frame_size // 2) + 1
print("num_frames: ", num_frames)

for i in range(num_frames):
    start = i * (frame_size // 2)
    end = start + frame_size

    avg = np.mean(data[start:end])
    averages.append(avg)

print("single average)", averages[64])

plt.figure(figsize=(10, 6))
plt.plot(np.arange(num_frames), averages)
plt.title('Average (sara.wav)')
plt.xlabel('frame')
plt.ylabel('average Amplitude')
plt.grid(True)
plt.show()
