import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

sample_rate, data = wav.read('../samples/sara.wav')
frame_size = 1024
num_frames = (len(data) - frame_size) // (frame_size // 2) + 1
print("num frames", num_frames)

if (len(data.shape) == 2): 
    data = np.mean(data, axis = 1)

energies = []
for i in range(num_frames):
    start = i * frame_size // 2
    end = start + frame_size
    frame = data[start:end]
    sum = np.sum(frame ** 2)

    energies.append(sum)
    
norm = energies / max(energies)

plt.figure(figsize=(10, 6))
plt.plot(np.arange(num_frames), norm)
plt.title('sara.wav')
plt.xlabel('frame')
plt.ylabel('main wave')
plt.grid(True)
plt.show()
