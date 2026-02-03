import librosa
import numpy as np

y, sr = librosa.load(librosa.example("nutcracker"))

mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
print("MFCC shape:", mfccs.shape)
