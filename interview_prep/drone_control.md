---
layout: default
title: Drone Control and Complementary Filter
---

# Drone Control and Complementary Filter

## IMU
### Gyroscope (Gyro)
- **Measures**: *Angular velocity* (rate of rotation) around each axis (x, y, z).
- **Units**: degrees/second (°/s) or radians/second (rad/s).
- **Strengths**:

  - Very good at detecting quick, short-term changes in orientation.
  - Not affected by linear acceleration (e.g., if you shake the sensor).
- **Weaknesses**:

  - Needs integration to get orientation → causes **drift** over time.
  - Small constant errors (bias) accumulate when integrated.

### 2. Accelerometer
- **Measures**: *Specific force* along each axis (x, y, z) — includes **gravity** and **linear acceleration**.
- **Units**: meters/second² (m/s²) or g (1 g ≈ 9.81 m/s²).
- **Strengths**:
  - Can give **absolute tilt/orientation** relative to gravity if stationary or moving slowly.
  - No drift over time.
- **Weaknesses**:
  - Very noisy during movement or vibration.
  - Can’t distinguish between gravity and actual movement acceleration.

---

## Continuous Time Complementary Filter
A complementary filter is a simple sensor fusion technique that combines measurements from two (or more) sensors in a way that uses each sensor’s strengths while compensating for its weaknesses.



### Complementary Filter Example - Measuring roll with IMU
1. Dead Reckoning

    - Integrating rate of change at each measurement step by adding it to the current measurement



**Many sensors have trade-offs:**

Accelerometers: Good at measuring long-term orientation (low-frequency information), but noisy and sensitive to vibration.

    - Cannot be trusted at a given second.


Gyroscopes: Good at measuring short-term changes (high-frequency information), but drift over time.

**The complementary filter** blends them:

![continuous complementary filter](../figures/complementary_filter.png)

Simplified filter diagram in practice:

![Simplified complementary filter](../figures/simplifiying_complementary_filter.png)

**Low-pass filter** the accelerometer → keeps slow, long-term trends (reduces noise).

**High-pass filter** the gyroscope → keeps fast, short-term changes (reduces drift).


## Discrete Complementary Filter

![discrete complementary filter](../figures/discrete_complementary_filter.png)

By believe the Gyro more, we are allowing short-term agility to make it through and also adding a small amount of accelerometer data to nudge it back to prevent drifting

---

# Drone Control in practice

## Sensors
1. Ultrasound sensor - measures altitude or distance above a surface
2. Camera - measures horizontal motion and speed
3. Pressure Sensor - Altitude
4. IMU - Angular rate and Acc

## Hardware
Opposing motors rotate in the same way but different from adjacent motors. This means **Thrust, roll, pitch, and yaw can be commanded independently**.

This design is due to the way yaw interacts with roll and pitch.

### How to command yaw
![command drone yaw](../figures/drone_yaw_diagram.png)

To change yaw, slow a pair of motors that spin in the same direction down and speed the other pair up. This will still counteract gravity but total torque is not 0. This Design allows drone to yaw without changing thrust, pitch, or roll.

### How to command roll
![command drone roll](../figures/drone_roll_diagram.png)
Decrease either left or right pairs of motors spinning in the opposite direction, causing a rolling torque.

### How to command thrust
Set all motors to the same speed.

### Motor Mixing Algorithm
![drone motor mixing](../figures/drone_motor_mixing_algorithm.png)

### Unactuated Directions
Forward, backward, left, and right are unactuated.

### Maintaining Altitude while going in un-actuated directions
To go left, tilt the drone so its thrust force partially counteracts gravity, partially points left. Increase thrust so the vertical component counteracts gravity completely.


---

## Control Diagram

![Drone Control Diagram](../figures/drone_control_diagram.png)

There are our actuators, four sensors, six degrees of freedom (x, y, z, roll, pitch, yaw).
**This is an underactuated system.** Since we don't have an actuator for every motion, some some directions are uncontrollable at any given time.
we are going to develop a controller that couples thrust with rotational dynamics

---

### Control Scheme

Plant: Drone

Desired output: hovering at fixed altitude.

Design goal: how to manipulate the four actuators to maintain altitude.

### Why a simple PID for altitude control wouldn't work
A PID for altitude (same as thrust) control cannot take into account wind gust and other disturbances. Since increasing thrust can only make the drone travel along its **local z axis (pointing down)**. We therefore needs to ensure a level flight. This motivates the next part.

### Why a decoupled four-indenpendent-controller control scheme wouldn't work

![Undesirable decoupled independent controller control scheme](../figures/independent_drone_controller.png)

This is **undesirable** since **Reference Pitch and Roll may need to be non-zero while hovering**, the drone needs to lean into the wind
    - wind gust can still cause the drone to drift away from its starting coordinates even though the drone would be level.

We **need to couple position errors with roll and pitch** because left, right, forward, and backward movements are not actuated

---

## Drone Altitude Controller

![drone altitude controller](../figures/drone_altitude_controller.png)

**Note:** We can command **thrust, roll, pitch, and yaw independently**. We can thereby create a feedback controller for each one. To ensure the drone doesn't drift away from the original (x,y) coordinates due to disturbance, we add a cascade loop for position control.

### Important notes on Drone Altitude Controller
1. We need estimated yaw for position controller, due to the fact that we need to coordinate-transform world coordinate of the starting position to drone body frame.

2. We have five parameters that require estimates for: yaw, pitch, roll, altitude, (x, y)
    - Sensor fuse the 4 sensors we have to estimate.

3. We have 6 PIDs to tune with 4 in cascade.
    - We need a great model to simulate drone dynamics

4. The position controller takes the position error as input and output roll and pitch. 

--- 

# Altitude Controller Walkthrough
**Scenario starts**: Altitude correct, but position is a bit off to the left -> position error.
Step 1: P controller of PID request roll angle to fly right, which gives a reference roll angle.
Step 2: Inner loop roll PID takes the reference roll angle from previous step and calculate rolling torque.
Step 3: Motor-Mix-Algorithm takes rolling torque as input and outputs motor commands, making motors on the left speed up and motors on the right slow down.
**Scenario prgoresses**: Step 3 makes the drone roll to the right, but since the vertical component of the thrust is slightly smaller than gravity when rolled, the drone loses altitude.
Step 4: Altitude controller senses this altitude error and increases thrust.
Step 5: Position error decreases as drone moves to the right, the requested roll angle also drops.
Step 6: Roll PID senses decreases in error, brings drone back to level.


---

# Flight code and simulation
![drone control workflow](../figures/drone_control_workflow.png)



This diagram shows the four components of the Flight Code Software (FCS)

## Flight code software
![drone control FCS](../figures/drone_block_diagram.png)

## Simulate Flight Dynamics
![Drone model design process](../figures/drone_model_design.png)
1. A high fidelity nonlinear model to simulate the real world
2. A linear model to test linear controllers

### What's inside the model block?
![Drone model details](../figures/drone_model_detail.png)

---

# Tuning the PID controller

start with the simplest model possible
1. Focus on altitude control only (thrust control) first by setting inputs to MMA for roll, pitch, and yaw to 0
2. Assume sensor model plays no role first.












