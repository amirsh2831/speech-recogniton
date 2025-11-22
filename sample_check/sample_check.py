import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import os

samples = "samples/down"
frame_size = 1024
titles = ["average", "energy", "zcr"]

def extract(path):
    sample_rate, data = wav.read(path)

    if len(data.shape) == 2:
        data = np.mean(data, axis=1)

    num_frames = (len(data) - frame_size) // (frame_size // 2) + 1

    energies = []
    for i in range(num_frames):
        start = i * (frame_size // 2)
        end = start + frame_size

        energy = np.sum(data[start:end] ** 2)
        energies.append(energy)
    
    normalized_energies = energies / max(energies)

    w_start = 0
    w_end = 0

    for ws in range(num_frames):
        if (normalized_energies[ws] >= 0.06):
            w_start = ws
            break
    
    for we in range(num_frames - 1, 0, -1):
        if (normalized_energies[we] >= 0.06):
            w_end = we
            break

    length = w_end - w_start
    features = []
    averages = []
    new_energies = []
    zcr = []
    for n in range (w_start, w_end):
        start = n * (frame_size // 2)
        end = start + frame_size
        frame = data[start:end]

        energy = np.sum(frame ** 2)
        average = np.mean(frame)
        z = 0

        for a in range(1, len(frame)):
            if (frame[a] * frame[a-1] < 0): 
                z += 1
            elif (frame[a] * frame[a-1] == 0):
                if (frame[a] * frame[a-2] < 0):
                    z += 1

        averages.append(average)
        new_energies.append(energy)
        zcr.append(z)

    features = [np.array(averages), np.array(new_energies), np.array(zcr)]
    return features, length

def plot(data, x_length):
    fig, axes = plt.subplots(10, 3, figsize=(15,20))
    for i in range(len(data)):
        for j in range(3):
            axes[i, j].plot(np.arange(x_length[i]), data[i][j])
            axes[i, j].set_title(titles[j])
            axes[i, j].grid(alpha=0.3)

        axes[i, 0].set_ylabel(f'Row {i + 1}', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.show()
        
all_features = []
lengths = []

for filename in os.listdir(samples):
    if filename.endswith('.wav'):
     path = os.path.join(samples, filename)
     feats, length = extract(path)
     print(length)
     all_features.append(feats)
     lengths.append(length)

print(len(all_features[0]))

plot(all_features, lengths)


