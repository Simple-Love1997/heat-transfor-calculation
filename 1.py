import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 5.0       # Length of the material (cm)
T = 100       # Total simulation time (s)
alpha = 0.04     # Thermal diffusivity (m^2/s)
Nx = 6      # Number of spatial grid points
Nt = 100      # Number of time steps

# Spatial and temporal step sizes
dx = L / (Nx - 1)
dt = T / Nt

# Initialize temperature field
u = np.zeros((Nx, Nt+1))

# Initial conditions
u[:, 0] = 0.0  # Set the initial temperature at all positions to 0℃
u[0, :] = 20.0  # Maintain the temperature at the left boundary as 20℃

# 计算温度场
for n in range(0, Nt):
    for i in range(1, Nx-1):
        u[i, n+1] = u[i, n] + alpha * dt / dx**2 * (u[i+1, n] - 2*u[i, n] + u[i-1, n])

# 计算内部热通量
q_30s = alpha * np.gradient(u[:, int(30 / T * Nt)])
q_100s = alpha * np.gradient(u[:, -1])

# 绘制温度场
x = np.linspace(0, L, Nx)
t = np.linspace(0, T, Nt+1)

X, T = np.meshgrid(x, t)
fig = plt.figure(figsize=(20, 6))

# 绘制温度场
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, T, u.T, cmap='viridis')
ax1.set_xlabel('Length (cm)')
ax1.set_ylabel('Time (s)')
ax1.set_zlabel('Temperature (℃)')
ax1.set_title('One-dimensional unsteady heat conduction')

# 绘制内部热通量
ax2 = fig.add_subplot(122)
ax2.plot(x, q_30s, label='t = 30s')
ax2.plot(x, q_100s, label='t = 100s')
ax2.set_xlabel('Length (cm)')
ax2.set_ylabel('Heat Flux (W/m^2)')
ax2.set_title('Heat Flux at Different Times')
ax2.legend()

plt.show()