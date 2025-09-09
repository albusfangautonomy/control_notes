import numpy as np
import matplotlib.pyplot as plt

# Time vector
t = np.linspace(0, 2 * np.pi, 500)

# Sine and Cosine waves
sine_wave = np.sin(t)
cosine_wave = np.cos(t)  # 90-degree (π/2 rad) phase lead over sine

# Plotting
plt.figure(figsize=(8, 4))
plt.plot(t, sine_wave, label='sin(t)', linewidth=2)
plt.plot(t, cosine_wave, label='cos(t)', linestyle='--', linewidth=2)

# Mark the phase shift visually
plt.axvline(x=np.pi/2, color='gray', linestyle=':', label='π/2 (90°)')

# Decorations
plt.title('Cosine Leads Sine by 90° (π/2 radians)')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../plots/phase_lead.png")
plt.show()
