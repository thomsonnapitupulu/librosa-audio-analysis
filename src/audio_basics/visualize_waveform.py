import librosa
import librosa.display
import matplotlib.pyplot as plt

y, sr = librosa.load(librosa.example("nutcracker"))

plt.figure(figsize=(10, 3))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")
plt.tight_layout()
plt.show()
