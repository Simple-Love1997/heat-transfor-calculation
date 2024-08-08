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
u = np.zeros((Nx, Nt + 1))

# Initial conditions
u[:, 0] = 0.0  # Set the initial temperature at all positions to 0℃
u[0, :] = 20.0  # Maintain the temperature at the left boundary as 20℃

# Add heat source from 3 to 4 cm
heat_source_start = 3.0  # cm
heat_source_end = 4.0    # cm

# Iterative solution
for n in range(0, Nt):
    for i in range(1, Nx - 1):
        # Check if within the range of the heat source
        if heat_source_start <= i * dx <= heat_source_end:
            # Add heat source term
            u[i, n + 1] = u[i, n] + (alpha * dt / dx**2) * (u[i + 1, n] - 2 * u[i, n] + u[i - 1, n] + 14.5)
        else:
            # Standard heat conduction equation
            u[i, n + 1] = u[i, n] + alpha * dt / dx**2 * (u[i + 1, n] - 2 * u[i, n] + u[i - 1, n])

# Plotting
x = np.linspace(0, L, Nx)
t = np.linspace(0, T, Nt + 1)

X, T = np.meshgrid(x, t)
fig = plt.figure(figsize=(20, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, u.T, cmap='viridis')
ax.set_xlabel('Length (cm)')
ax.set_ylabel('Time (s)')
ax.set_zlabel('Temperature (℃)')
ax.set_title('One-dimensional unsteady heat conduction with heat source')

plt.show()