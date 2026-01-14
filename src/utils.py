import numpy as np
import matplotlib.pyplot as plt

# ---------- Helper Functions ----------

def generate_noisy_signal(duration=1.0, sample_rate=1000, freq=5, noise_level=0.5):
    """
    Generate a noisy sine wave signal to simulate a gravitational wave.
    duration: seconds
    sample_rate: points per second
    freq: Hz of underlying sine wave
    noise_level: amplitude of Gaussian noise
    """
    t = np.linspace(0, duration, int(sample_rate*duration))
    clean_signal = np.sin(2 * np.pi * freq * t)
    noise = np.random.normal(0, noise_level, len(t))
    noisy_signal = clean_signal + noise
    return t, noisy_signal, clean_signal

def save_signal(file_path, signal):
    """Save a 1D array as CSV"""
    np.savetxt(file_path, signal, delimiter=",")

def load_signal(file_path):
    """Load CSV file into array"""
    return np.loadtxt(file_path, delimiter=",")

def plot_signals(t, original, denoised=None, title="Signal", save_path=None):

