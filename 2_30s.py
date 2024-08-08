import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 5.0       # Length of the material (cm)
T = 100       # Total simulation time (s)
Nx = 6        # Number of spatial grid points
Nt = 100      # Number of time steps

# Spatial and temporal step sizes
dx = L / (Nx - 1)
dt = T / Nt

# Initialize temperature field
u_steel = np.zeros((Nx, Nt+1))
u_air = np.zeros((Nx, Nt+1))

# Initial conditions
u_steel[:, 0] = 0.0  # Set the initial temperature at all positions to 0℃
u_steel[0, :] = 20.0  # Maintain the temperature at the left boundary as 20℃

u_air[:, 0] = 0.0  # Set the initial temperature at all positions to 0℃
u_air[0, :] = 20.0  # Maintain the temperature at the left boundary as 20℃

# Thermal diffusivity for steel and air
alpha_steel = 0.04       # Thermal diffusivity (cm^2/s)
alpha_air = 0.2        # Thermal diffusivity (cm^2/s)

# Iterative solution for steel
for n in range(0, Nt):
    for i in range(1, Nx-1):
        u_steel[i, n+1] = u_steel[i, n] + alpha_steel * dt / dx**2 * (u_steel[i+1, n] - 2*u_steel[i, n] + u_steel[i-1, n])

# Iterative solution for air
for n in range(0, Nt):
    for i in range(1, Nx-1):
        u_air[i, n+1] = u_air[i, n] + alpha_air * dt / dx**2 * (u_air[i+1, n] - 2*u_air[i, n] + u_air[i-1, n])

# Plotting
x = np.linspace(0, L, Nx)

# Plot for steel and air together
plt.plot(x, u_steel[:, int(30 / T * Nt)], label='Steel')
plt.plot(x, u_air[:, int(30 / T * Nt)], label='Air')
plt.xlabel('Length (cm)')
plt.ylabel('Temperature (℃)')
plt.title('Temperature Distribution at 30s - Steel vs. Air')
plt.legend()

plt.show()