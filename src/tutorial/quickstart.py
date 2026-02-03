import librosa

filename = librosa.example("nutcracker")
y, sr = librosa.load(filename)

print(f"Audio shape: {y.shape}")
print(f"Sample rate: {sr}")
