import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("SHG-FROG Pulse Measurement Simulation")

st.markdown("Adjust pulse parameters to observe changes in the FROG trace.")

# Sliders
pulse_width = st.slider("Pulse Width (fs)", 5, 60, 20)
chirp = st.slider("Chirp", 0.0, 0.05, 0.01)

# Time grid
t = np.linspace(-100,100,512)
delays = np.linspace(-80,80,80)

# Pulse
E = np.exp(-t**2/(2*pulse_width**2)) * np.exp(1j*chirp*t**2)

# Compute FROG
frog = []

for delay in delays:
    E_delayed = np.interp(t-delay,t,E.real) + 1j*np.interp(t-delay,t,E.imag)
    shg = E * E_delayed
    spectrum = np.fft.fftshift(np.fft.fft(shg))
    frog.append(np.abs(spectrum)**2)

frog = np.array(frog)

# Plot
fig, ax = plt.subplots()
ax.imshow(frog, aspect='auto', origin='lower', cmap='seismic')
ax.set_title("FROG Trace")
ax.set_xlabel("Frequency")
ax.set_ylabel("Delay")

st.pyplot(fig)
