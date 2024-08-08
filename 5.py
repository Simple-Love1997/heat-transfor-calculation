import numpy as np
import matplotlib.pyplot as plt

# Parameters for the first simulation
L_before = 6.0       # Length of the material (cm)
T_before = 100       # Total simulation time (s)
alpha_before = 0.04     # Initial thermal diffusivity (cm^2/s)
Nx_before = 7      # Number of spatial grid points
Nt_before = 100      # Number of time steps

# Spatial and temporal step sizes for the first simulation
dx_before = L_before / (Nx_before - 1)
dt_before = T_before / Nt_before

# Initialize temperature field for the first simulation
u_before = np.zeros((Nx_before, Nt_before+1))

# Initial conditions for the first simulation
u_before[:, 0] = 0.0  # Set the initial temperature at all positions to 0℃
u_before[0, :] = 20.0  # Maintain the temperature at the left boundary as 20℃
u_before[6, :] = 0.0  # Maintain the temperature at the right boundary as 0℃

# Iterative solution for the first simulation
for n in range(0, Nt_before):
    for i in range(1, Nx_before-1):
        u_before[i, n+1] = u_before[i, n] + alpha_before * dt_before / dx_before**2 * (u_before[i+1, n] - 2 * u_before[i, n] + u_before[i-1, n])

# Parameters for the second simulation
L_after = 6.0       # Length of the material (cm)
T_after = 100       # Total simulation time (s)
alpha_after = 0.04     # Initial thermal diffusivity (cm^2/s)
Nx_after = 7      # Number of spatial grid points
Nt_after = 100      # Number of time steps

# Spatial and temporal step sizes for the second simulation
dx_after = L_after / (Nx_after - 1)
dt_after = T_after / Nt_after

# Initialize temperature field for the second simulation
u_after = np.zeros((Nx_after, Nt_after+1))

# Initial conditions for the second simulation
u_after[:, 0] = 0.0  # Set the initial temperature at all positions to 0℃
u_after[0, :] = 20.0  # Maintain the temperature at the left boundary as 20℃
u_after[6, :] = 0.0  # Maintain the temperature at the right boundary as 0℃

# Iterative solution for the second simulation
for n in range(0, Nt_after):
    for i in range(1, Nx_after-1):
        if i * dx_after == 5.0:
            u_after[i, n+1] = u_after[i, n] + alpha_after * dt_after / dx_after**2 * (- u_after[i, n] + u_after[i-1, n]) + 0.5 * alpha_after * dt_after / dx_after**2 * (- u_after[i, n] + u_after[i+1, n])
        else:
            u_after[i, n+1] = u_after[i, n] + alpha_after * dt_after / dx_after**2 * (u_after[i+1, n] - 2 * u_after[i, n] + u_after[i-1, n])

# Extract temperature at 5cm position from the first simulation
temperature_before = u_before[int(5 / dx_before), :]

# Extract temperature at 5cm position from the second simulation
temperature_after = u_after[int(5 / dx_after), :]

# Plotting
plt.figure(figsize=(5, 3))
plt.plot(np.linspace(0, T_before, Nt_before+1), temperature_before, label='Before')
plt.plot(np.linspace(0, T_after, Nt_after+1), temperature_after, label='After')
plt.xlabel('Time (s)')
plt.ylabel('Temperature at 5cm (℃)')
plt.title('Comparison of Temperature at 5cm Position Over Time')
plt.legend()
plt.grid(True)
plt.show()