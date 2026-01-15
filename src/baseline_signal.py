# src/baseline_signal.py
import numpy as np

def generate_signals(length=1000, noise_level=0.3, seed=42):
    """
    Generate a clean sine wave signal and add Gaussian noise to create a noisy signal.

    Parameters:
        length (int): Number of time steps
        noise_level (float): Standard deviation of Gaussian noise
        seed (int): Random seed for reproducibility

    Returns:
        clean_signal (np.ndarray): Clean sine wave
        noisy_signal (np.ndarray): Noisy signal
    """
    np.random.seed(seed)

    # Generate clean sine wave
    t = np.linspace(0, 4*np.pi, length)  # 2 cycles of sine
    clean_signal = np.sin(t)

    # Add Gaussian noise
    noise = np.random.normal(0, noise_level, size=length)
    noisy_signal = clean_signal + noise

    return clean_signal, noisy_signal

# Optional: if you want to run this script directly
if __name__ == "__main__":
    import pandas as pd
    import os

    # Generate signals
    clean, noisy = generate_signals()

    # Make sure data folder exists
    os.makedirs("../data", exist_ok=True)

    # Save CSVs
    pd.DataFrame(clean, columns=['Amplitude']).to_csv("../data/clean_signal.csv", index=False)
    pd.DataFrame(noisy, columns=['Amplitude']).to_csv("../data/noisy_signal.csv", index=False)

    print("Phase 1 complete: clean_signal.csv and noisy_signal.csv generated in data/")

