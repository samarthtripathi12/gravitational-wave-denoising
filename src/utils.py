import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
import pywt
import pandas as pd

def generate_clean_signal(freq, t):
    return np.sin(2 * np.pi * freq * t)

def add_noise(signal, noise_level=0.5):
    noise = np.random.normal(0, noise_level, len(signal))
    return signal + noise

def moving_average(signal, window_size=5):
    return np.convolve(signal, np.ones(window_size)/window_size, mode='same')

def fourier_low_pass(signal, cutoff_freq, dt=0.001):
    n = len(signal)
    freq = np.fft.fftfreq(n, dt)
    fft_signal = fft(signal)
    fft_signal[np.abs(freq) > cutoff_freq] = 0
    return np.real(ifft(fft_signal))

def wavelet_denoise(signal, wavelet='db4', level=1):
    coeff = pywt.wavedec(signal, wavelet, level=level)
    sigma = np.median(np.abs(coeff[-level])) / 0.6745
    uthresh = sigma * np.sqrt(2 * np.log(len(signal)))
    denoised_coeff = [pywt.threshold(c, value=uthresh, mode='soft') for c in coeff]
    return pywt.waverec(denoised_coeff, wavelet)

def compute_mse(signal1, signal2):
    return np.mean((signal1 - signal2)**2)

def compute_snr(signal, noise):
    return 10 * np.log10(np.sum(signal**2)/np.sum(noise**2))

def plot_signals(time, signals_dict, filename):
    plt.figure(figsize=(10,5))
    for label, sig in signals_dict.items():
        plt.plot(time, sig, label=label)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

