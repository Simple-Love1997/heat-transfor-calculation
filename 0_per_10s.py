import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 5.0       # Length of the material (cm)
T = 100       # Total simulation time (s)
alpha = 0.04  # Thermal diffusivity (cm^2/s)
Nx = 6        # Number of spatial grid points
Nt = 100      # Number of time steps

# Spatial and temporal step sizes
dx = L / (Nx - 1)
dt = T / Nt

# Initialize temperature field
u = np.zeros((Nx, Nt+1))

# Initial conditions
u[:, 0] = 0.0   # Set the initial temperature at all positions to 0℃
u[0, :] = 20.0  # Maintain the temperature at the left boundary as 20℃

# Iterative solution
for n in range(0, Nt):
    for i in range(1, Nx-1):
        u[i, n+1] = u[i, n] + alpha * dt / dx**2 * (-u[i, n] + u[i-1, n])

# Plotting
x = np.linspace(0, L, Nx)
t = np.linspace(0, T, Nt+1)

# Extract every 10 seconds
time_interval = 10  # seconds
frames_to_extract = np.arange(0, Nt+1, int(time_interval / dt))

# Plot and combine frames
fig, ax = plt.subplots(figsize=(10, 6))
for frame in frames_to_extract:
    ax.plot(x, u[:, frame], label=f'Time = {frame * dt:.1f} s')

ax.set_xlabel('Length (cm)')
ax.set_ylabel('Temperature (℃)')
ax.set_title('Temperature Distribution at Different Times')
ax.legend()
plt.show()