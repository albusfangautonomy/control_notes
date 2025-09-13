import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.81
m = 1.0
l = 1.0
b = 0.0   # small damping
I = m*l*l

# Grid
theta = np.linspace(-2*np.pi, 2*np.pi, 25)
dtheta = np.linspace(-6, 6, 25)
Theta, DTheta = np.meshgrid(theta, dtheta)

def vector_field(Theta, DTheta, u):
    U = DTheta
    V = (-b*DTheta - m*g*l*np.sin(Theta) + u) / I
    return U, V

def normalize(U, V):
    mag = np.sqrt(U**2 + V**2)
    mag[mag == 0] = 1
    return U/mag, V/mag

# Vector fields
U0, V0 = vector_field(Theta, DTheta, u=0.0)   # no torque
U1, V1 = vector_field(Theta, DTheta, u=1.0)   # constant torque = 1
U0n, V0n = normalize(U0, V0)
U1n, V1n = normalize(U1, V1)
# U0n, V0n = U0, V0
# U1n, V1n = U1, V1 
# Plot
plt.figure(figsize=(9, 6))
plt.title("Pendulum Vector Fields: u=0 (blue) vs u=1 (orange)")
plt.xlabel(r"$\theta$ (rad)")
plt.ylabel(r"$\dot{\theta}$ (rad/s)")

plt.quiver(Theta, DTheta, U0n, V0n, color="blue", alpha=0.6, label="u=0")
plt.quiver(Theta, DTheta, U1n, V1n, color="orange", alpha=0.6, label="u=1")

plt.legend()
plt.savefig("control_input_shapes_vector_field.png")
plt.show()
