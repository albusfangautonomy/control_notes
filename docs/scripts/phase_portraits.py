import matplotlib
matplotlib.use("TkAgg") 
import matplotlib.pyplot as plt
import numpy as np

def pendulum_vector_field(theta, dtheta, u=0, g=9.81, m=1.0, l=1.0, b=1.0):
    theta_dot = dtheta
    # dtheta_dot = -b*dtheta - m*g*l*np.sin(theta)
    dtheta_dot = 1/(m*l*l) * (u-b* theta_dot - m*g*l*np.sin(theta))
    return theta_dot, dtheta_dot

# Grid in state space
theta = np.linspace(-2*np.pi, 2*np.pi, 200)      # angle
dtheta = np.linspace(-6.0, 6.0, 160)             # angular velocity
Theta, DTheta = np.meshgrid(theta, dtheta)

# Vector field
U, V = pendulum_vector_field(Theta, DTheta)

# Plot
plt.figure(figsize=(8, 5))
plt.title("Simple Pendulum Phase Portrait (Continuous Streamlines)")
plt.xlabel(r"$\theta$ (rad)")
plt.ylabel(r"$\dot{\theta}$ (rad/s)")
plt.streamplot(Theta, DTheta, U, V, density=1.2, linewidth=1.0, arrowsize=1.0)

# (Optional) mark a few equilibria
for th in [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]:
    plt.plot(th, 0.0, 'o', markersize=4)

plt.tight_layout()
# plt.savefig("simple_pendulum_phase_portrait_with_damping.png")
plt.show()
