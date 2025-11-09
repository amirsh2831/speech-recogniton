import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

sample_rqate, data = wav.read('../samples/sara.wav')
frame_size = 1024


if (len(data.shape) == 2):
    data = np.mean(data, axis=1)

num_frames = (len(data) - frame_size) // (frame_size // 2) + 1
ac = np.zeros((num_frames, frame_size))
print("num_frames: ", num_frames)

for i in range(num_frames):
    start = i * (frame_size // 2)
    end = start + frame_size
    frame = data[start:end]

    for r in range(frame_size):
        sum = 0.0
        for n in range(frame_size - r):
            sum += frame[n] * frame[n + r]
        ac[i, r] = sum

plt.figure(figsize=(10, 5))
plt.imshow(ac.T, origin='lower', aspect='auto', cmap='viridis')
plt.colorbar(label='Autocorrelation')
plt.xlabel('Frame')
plt.ylabel('samples')
plt.title('Autocorrelation')
plt.show()