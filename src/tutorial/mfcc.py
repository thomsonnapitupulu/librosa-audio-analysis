import librosa
import numpy as np

y, sr = librosa.load(librosa.example("nutcracker"))

mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
print("MFCC shape:", mfccs.shape)

duration = mfccs.shape[1] * 512 / sr
print("MFCC duration: ", duration)

mfcc_mean = mfccs.mean(axis=1)
mfcc_std = mfccs.std(axis=1)

print("MFCC mean:", mfcc_mean)
print("MFCC Std:", mfcc_std)