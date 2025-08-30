---
layout: default
title: Kodiak Autonomous Trucking
---

## Q1: Your GNSS feed drops for 5 seconds, but you still have IMU data. How would you keep the state estimate stable during that time? Which estimation technique(s) would you use and why?
When GNSS drops, I’d rely on high-rate inertial data for short-term state propagation. The IMU provides fast gyroscope and accelerometer updates; gyros give smooth angular rate but drift over time, while accelerometers are noisy but drift-free. I’d use an Extended Kalman Filter to fuse the IMU with any other available aiding sensors — like magnetometer for yaw reference — and explicitly model sensor biases for gyro, accel, and magnetometer in the state vector.

During the dropout, the EKF runs in prediction mode, essentially doing dead reckoning. For a ground vehicle, I might also constrain motion with wheel odometry or nonholonomic constraints to reduce drift. The state would include pose, velocity, accelerations, and sensor biases — about 25–30 states in my case — so when GNSS returns, the filter can quickly correct accumulated drift.

## 