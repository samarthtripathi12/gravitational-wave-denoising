import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load noisy signal
noisy_signal = pd.read_csv("data/noisy_signal.csv")["Signal"].values

# Moving average filter
def moving_average(signal, window_size=20):
    return np.convolve(signal, np.ones(window_size)/window_size, mode="same")

denoised_signal = moving_average(noisy_signal)

# Save denoised signal
pd.DataFrame(denoised_signal, columns=["Signal"]).to_csv(
    "data/denoised_moving_average.csv", index=False
)

# Plot comparison
plt.figure(figsize=(10, 4))
plt.plot(noisy_signal, label="Noisy Signal", alpha=0.5)
plt.plot(denoised_signal, label="Moving Average Denoised", linewidth=2)
plt.legend()
plt.title("Moving Average Denoising (Initial Attempt)")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.savefig("plots/moving_average_result.png")
plt.show()

