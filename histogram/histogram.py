import wave
import struct
import matplotlib.pyplot as plt

# read from wave file ------------------
wav_file = wave.open('samples/sara.wav', 'rb')

# parameters
sample_width = wav_file.getsampwidth()
num_frames = wav_file.getnframes()
num_channels = wav_file.getnchannels()

raw_data = wav_file.readframes(num_frames)

if sample_width == 2:  
    samples = struct.unpack(f'<{num_frames * num_channels}h', raw_data)
wav_file.close()

if num_channels == 2:
    samples = samples[::2]  
# ----------------------------------------

hist = [0] * 65536

for sample in samples:
    index = sample + 32768
    hist[index] += 1

x_values = list(range(-32768, 32768))

plt.figure(figsize=(10, 6))
plt.bar(x_values, hist, width=1)
plt.title('Histogram (sara.wav)')
plt.xlabel('Sample Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.xlim(-10000, 10000)  # Zoom 
plt.show()