import numpy as np
import pandas as pd
import os
from utils import generate_clean_signal, add_noise, moving_average, fourier_low_pass, wavelet_denoise, compute_mse, compute_snr, plot_signals

# Create data and plots folders
os.makedirs("data", exist_ok=True)
os.makedirs("plots", exist_ok=True)

t = np.linspace(0, 1, 1000)
freq = 5

clean = generate_clean_signal(freq, t)
noisy = add_noise(clean, 0.5)

# Save CSVs
pd.DataFrame({'time': t, 'amplitude': clean}).to_csv("data/clean_signal.csv", index=False)
pd.DataFrame({'time': t, 'amplitude': noisy}).to_csv("data/noisy_signal.csv", index=False)

# Denoising
denoised_ma = moving_average(noisy)
denoised_fft = fourier_low_pass(noisy, cutoff_freq=10)
denoised_wavelet = wavelet_denoise(noisy)

# Save denoised CSVs
pd.DataFrame({'time': t, 'amplitude': denoised_ma}).to_csv("data/denoised_ma.csv", index=False)
pd.DataFrame({'time': t, 'amplitude': denoised_fft}).to_csv("data/denoised_fft.csv", index=False)
pd.DataFrame({'time': t, 'amplitude': denoised_wavelet}).to_csv("data/denoised_wavelet.csv", index=False)

# Compute metrics
methods = {'Noisy': noisy, 'Moving Avg': denoised_ma, 'Fourier': denoised_fft, 'Wavelet': denoised_wavelet}
print("{:<15} {:<10} {:<10}".format("Method", "MSE", "SNR"))
for name, sig in methods.items():
    mse = compute_mse(clean, sig)
    snr = compute_snr(clean, clean-sig)
    print(f"{name:<15} {mse:<10.4f} {snr:<10.2f}")

# Plot signals
plot_signals(t, {'Clean': clean, 'Noisy': noisy}, "plots/noisy_vs_clean.png")
plot_signals(t, {'Clean': clean, 'Moving Avg': denoised_ma, 'Fourier': denoised_fft, 'Wavelet': denoised_wavelet}, "plots/denoised_vs_clean.png")

print("All CSVs and plots generated in data/ and plots/")

