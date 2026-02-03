import librosa

# Load example audio
filename = librosa.example("nutcracker")
y, sr = librosa.load(filename)

print("Sample rate:", sr)
print("Waveform shape:", y.shape)
print("Duration (seconds):", len(y) / sr)
