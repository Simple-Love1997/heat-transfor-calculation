import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 5       # Length of the material (cm) + dx = 1 cm
T = 10       # Total simulation time (s)
alpha = 0.2     # Thermal diffusivity (cm^2/s)
Nx = 6      # Number of spatial grid points
Nt = 1000       # Number of time steps
v = 1      # flow rate　(cm/s)

# Spatial and temporal step sizes
dx = L / ( Nx - 1 )
dt = T / Nt

# Initialize temperature field
u = np.zeros((Nx, Nt+1))

# Initial conditions
u[:, 0] = 0.0  # Set the initial temperature at all positions to 0℃
u[0, :] = 20.0  # Maintain the temperature at the left boundary as 20℃


# Iterative solution
for n in range(0, Nt):    # 時間n　　# 空間i
    for i in range(1, Nx-1):
        u[i, n+1] = u[i, n] + alpha * dt / dx**2 * (u[i+1, n] - 2 * u[i, n] + u[i-1, n]) + v * dt / dx * (u[i-1, n] - u[i , n])


# Plotting
x = np.linspace(0, L, Nx)
t = np.linspace(0, T, Nt+1)

X, T = np.meshgrid(x, t)
fig = plt.figure(figsize=(20, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, u.T, cmap='viridis')
ax.set_xlabel('Length (cm)')
ax.set_ylabel('Time (s)')
ax.set_zlabel('Temperature (℃)')
ax.set_title('Temperature distribution at 20s')

plt.show()

# 存储需要输出的时刻
output_times = [5,10]

# 迭代求解热传导方程
for n in range(0, Nt):
    for i in range(1, Nx-1):
        u[i, n+1] = u[i, n] + alpha * dt / dx**2 * (u[i+1, n] - 2 * u[i, n] + u[i-1, n]) + v * dt / dx * (u[i-1, n] - u[i , n])

    # 输出需要的时刻
    if (n+1) * dt in output_times:
        plt.plot(x, u[:, n+1], label=f'Time = {(n+1) * dt:.1f}s')

# 绘制曲线图
plt.xlabel('Length (cm)')
plt.ylabel('Temperature (℃)')
plt.title('Temperature Distribution at 5s and 10s')
plt.legend()
plt.show()
