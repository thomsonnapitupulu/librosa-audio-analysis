import librosa

filename = librosa.example("nutcracker")
y, sr = librosa.load(filename)

print(f"Audio shape: {y.shape}")
print(f"Sample rate: {sr}")

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
tempo_value = float(tempo)
print(f"Estimated tempo: {tempo_value:.2f} BPM")

