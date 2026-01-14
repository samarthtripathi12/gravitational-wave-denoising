from utils import generate_noisy_signal, save_signal

# Generate example signal
t, noisy_signal, clean_signal = generate_noisy_signal(duration=1.0, sample_rate=1000, freq=5, noise_level=0.5)

# Save noisy signal to your data folder
save_signal("../data/noisy_signal.csv", noisy_signal)
save_signal("../data/clean_signal.csv", clean_signal)

print("Noisy signal and clean signal saved in /data folder.")

