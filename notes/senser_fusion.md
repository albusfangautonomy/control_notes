---
layout: default
title: Stability Analysis
---

# Sensor Fusion

## Definition
Sensor fusion is a technique that combines two or more data sources in a way taht geneartes a more consistent, accurate, and dependable understanding of the system.

## Advantages and Use Cases
1. It can increase the quality of the data by fusing either two sensors of either the same type or different types together.

2. It can increase reliability.

3. It can estimate unmeasured states.

4. It can be used to increase coverage.

---

# Sensor Fusion Examples

## Attitude and heading reference system (AHRS)
To defin an orientation:
1. Reference Frame

2. Specify rotation

### Measuring Attitude and Heading

### Sensors - IMU (Magnetometer, Accelerometer, and Gyro)
The absolute orientation for a static object can be determined just with M and A and taking cross products.

**Magnetometer** measures the strength and direction of a magnetic field and determines heading relative to the Earth's magnetic north.

    - readings can be corrupted by other magnetic sources.
    - Hard Iron sources (Magnet or Coil) shift the sphere, soft irons (nails) distorts the sphere. Sphere refers to 
    - needs to calibrate by rotate the device around

**Accelerometer** measures acceleration

    - if the accelerometer is not at center of rotation, readings can be off.
    - linear acceleration can corrcupt Acc measurement of "down"

**Gyro** measures angular rate
    - Dead reckoning refers to integrating gyro readings (integration is a low pass filter, which filters out high frequency noise)
    - Gyros have drift


### Sensor Fusion algorithm for IMU
1. Initialize attitude
2. Use mag field and gravity to correct gyro drift


In **complementary filter**, the user decides how much accel+mag and gyro data need to be trusted. Kalman filter automatically computes the confidence.

---

## Sensor Fusion with GPS and IMU: Algorithm - Extended Kalman
[Matlab Example](https://www.mathworks.com/help/fusion/ug/pose-estimation-from-asynchronous-sensors.html)

Note that the model in Extended Kalman is not vehicle specific. This model refers to how each state of the filter is affected by other states of the filter. The 'model' just dead-reckon the sensor data adjusted for biases and predict the pose.

GPS measured velocity and position.
If GPS reading doesn't need to be very accurate or fast, adding IMU is not helping much. (driving with google maps)
If GPS reading needs to be accurate and fast velocity constantly changing, adding IMU helps. (drone flying around obstacles)



**Estimating the sensor bias is extremely imporant** because bias drifts over time.

### Step 1: Initializing the filter

**28 state kalman state vector:**  
1. Orientation (4 states quaternion)
2. Angular Velocity(XYZ) (3) where XYZ means angular rates about body x,y,z, axes
3. Position (NED) (3)
4. Velocity (NED) (3)
5. Acceleration (NED) (3)
6. Accelerometer Bias (XYZ) (3)
7. Geomagnetic Field Vector (NED) (3)
4. Magnetometer Bias (XYZ) (3)

If no estimates of sensor bias is available at system start, let the kalman filter converge to the correct solution while the vehicle is stationary.

![sensor bias over time](../figures/sensor_bias.png)

**Note:** Extended Kalman linearizes the nonlinear model at current estimate and uses the linear model to predict state into the future. If the filter is not initialized close to the true state, the linearization result would deviate and estimate would not converge.


Initializing a real system

![Initializing filter for a real system](../figures/initialize_filter_real_system.png)

### Step 2: Kalman
**Predict** and **Correct**

1. Predict the state based on model and keep track of confidence (Process Noise). When new measurement comes in with measurement noise, the filter compare the measurement with predicted model and corrects its estimate based on the confidence.

2. If there is an update from any of the sensors, update the state based on the relative confidence based on the estimate and the measurement.

    - The sensor can therefore run with **asyncronous measurements**

---

# Tracking Remote Objects

## Interacting Multiple Model Filter (IMM) - How to track a single remote object with remote sensors

Tracking a remote object. Key difference: with Kalman filters, one knows the state model to predict the future state of an object. However, when tracking a remote object, we typically don't have access to the input to the plant.

Cooperative Tracking: tracked object shares control input.

![cooperative tracking](../figures/cooperative_tracking.png)


Unkown inputs are taken into account by **process noise**.

Uncoorperative Tracking: tracked object does not share control input.

![Uncooperative Tracking](../figures/uncooperative_tracking.png)


---

### Uncooperative tracking with a remote object

Trade-off between High process noise and low process noise.

Example: constant velocity model but don't know the exact control inputs

Scheme: Increase Process noise to trust prediction less and trust measurement more. This would reduce noise when the actual dynamics is not constant velocity. However, this comes at the cost of error for area which the model predicts the dynamics well (constant velocity case).

![Process Noise trade-off](../figures/process_noise_tradeoff.png)

---

### Interactive Multiple Model Filter (single object tracking)
To have one model for each type of motion. Allowing each model to interact to reduce transient error

![IMM](../figures/imm.png)

Interactive Multi-Model filter vs Multi-Model Filter
1. IMM reduces transient error compared to independent models in Multi-Model filters
2. IMM blends all models together based on the likelihood of each representing the true motion

### Disadvantages of too many models in IMM
A large number of models for IMM can introduce both computationall cost and performance hit

Performance:
1. More models means more transitions between models
2. Harder to know when to make a transitions

Try to find the **smallest number** of models that adequetly predicts the possible motion of the object you're tracking.

---

## Tracking Multiple Remote Objects

![Multi-Object Tracking](../figures/multi_object_tracking.png)

### Challenges of multi-object tracking

Date Association Problem
1. Uncertainty in observations and predictions play a major role in the challenges.
2. Objects can be close enough to accurately attribute a measurement to an object.
3. Uncertainty can be great enough that a measurement can be of more than one object.

Track Maintanence Problem
4. The number of objects being tracked is not fixed.
5. Sometimes tracks need to be created or removed (stop tracking when plane lands).
6. False positive or missed detection measurements

### Diagram Breakdown
1. Observations

    - Measured Quantities: range, range rate, line of sight
    - Measured Attributes: target type, ID number, object shape

2. Assignment: Matching an Observation to a Tracked Object

    - Mahalanobis distance: the closest probability distance (normalized by stadard deviation)
    - Joint Probabilistic Data Association (JPDA): does not commit to a single observation and assgin one object to one track but instead make a weighted combinations of all neighboring observations (closer ones have bigger weight)

    ![jpda](../figures/jpda.png)

3. Track Maintenance (deleting and creating track)
    
    - Delete a track if not detected at least P times in R updates with R and P tunable.
    - Create a track: tentative track an observation not assigned to an object. Confirm trakc if object has been detected M times in N updates.

4. Estimation Filters

    - Each filter runs. Fused measured state $$\hat{x}$$ and fused covariance $$\bar{P}$$ are captured.

5. Gating

    - Screens all detections to detect which detections are feasible to look at for assignment.
    - Ignores detections outside of a region, also called "gate".

---

# Track Level Fusion

Central-level tracking vs Sensor-level Tracking and Track Level Fusion

![central vs sensor level tracking](../figures/central_vs_sensor_level.png)

source tracks provide their own track with distribution. The track fuser determines if these are the same object or different objects

sensor level tracking:

![sensor level tracking](../figures/sensor_level_tracking.png)

## Advantages and Challenges of Track Level Fusion

### Advantages

1. Access to data

    - TLF is necessary if you don't have access to raw sensor data. For instance, a Lidar sensor that doesn't return point cloud but instead the tracks. No track level data available

    ![track level access to data](../figures/track_level_access_to_data.png)

2. Bandwidth

    - Transmitting data from sensors in real time to computing centers that runs tracking.
    - Track level fusion data is smaller than raw sensor data.


3. Compute

    - Local computer can pre-process data to reduce processing time.

4. Specialize

    - TLF allows sensor level trackers to be specialized to the particular sensor type.
    - Since these trackers need motion and sensor models. Track maintenance needs to be tuned.

![track level specialize](../figures/track_level_specialize.png)

### Challengs of TLF

1. Reduced Accuracy

    - Track distills sensor raw data to a lot less info. We may remove useful info.

2. Correlated noise

    - If tracks are correlated, then we can't multiply the probabilities like Kalman.

---

# Appendix

## IMM walkthrough

<section id="imm-one-cycle">
  <h3>Interacting Multiple Model (IMM): One Cycle</h3>
  <ol>
    <li>
      <h3>Model-conditioned reinitialization (mixing), for each model \( m_i \in \mathcal{M} \)</h3>
      <ol>
        <li>
          <strong>Predicted model probability</strong><br>
          \[
            \mu_{k|k-1}^{(i)} = \sum_{j} \pi_{ji}\,\mu_{k-1}^{(j)}
          \]
        </li>
        <li>
          <strong>Mixing probabilities</strong> (previous model \(j\) given current \(i\))<br>
          \[
            \mu_{k-1}^{j|i} = \frac{\pi_{ji}\,\mu_{k-1}^{(j)}}{\mu_{k|k-1}^{(i)}}
          \]
        </li>
        <li>
          <strong>Mixed initial state</strong><br>
          \[
            \bar{x}_{k-1|k-1}^{(i)} = \sum_{j} \hat{x}_{k-1|k-1}^{(j)} \,\mu_{k-1}^{j|i}
          \]
        </li>
        <li>
          <strong>Mixed initial covariance</strong><br>
          \[
            \bar{P}_{k-1|k-1}^{(i)} =
            \sum_{j}\Big(
              P_{k-1|k-1}^{(j)}
              + (\bar{x}_{k-1|k-1}^{(i)}-\hat{x}_{k-1|k-1}^{(j)})
                (\bar{x}_{k-1|k-1}^{(i)}-\hat{x}_{k-1|k-1}^{(j)})^\top
            \Big)\,\mu_{k-1}^{j|i}
          \]
        </li>
      </ol>
    </li>

    <li>
      <h3>Model-conditioned filtering (per model)</h3>
      <ol>
        <li>
          <strong>Prediction</strong><br>
          \[
            \hat{x}_{k|k-1}^{(i)} = F_{k-1}^{(i)}\,\bar{x}_{k-1|k-1}^{(i)},\qquad
            P_{k|k-1}^{(i)} = F_{k-1}^{(i)}\,\bar{P}_{k-1|k-1}^{(i)}\,(F_{k-1}^{(i)})^\top + Q_{k-1}^{(i)}
          \]
        </li>
        <li>
          <strong>Update</strong><br>
          \[
            \tilde{z}_{k}^{(i)} = z_k - H_{k}^{(i)} \hat{x}_{k|k-1}^{(i)},\qquad
            S_{k}^{(i)} = H_{k}^{(i)} P_{k|k-1}^{(i)} (H_{k}^{(i)})^\top + R_{k}^{(i)}
          \]
          \[
            K_{k}^{(i)} = P_{k|k-1}^{(i)} (H_{k}^{(i)})^\top (S_{k}^{(i)})^{-1}
          \]
          \[
            \hat{x}_{k|k}^{(i)} = \hat{x}_{k|k-1}^{(i)} + K_{k}^{(i)} \tilde{z}_{k}^{(i)},\qquad
            P_{k|k}^{(i)} = P_{k|k-1}^{(i)} - K_{k}^{(i)} S_{k}^{(i)} (K_{k}^{(i)})^\top
          \]
        </li>
      </ol>
    </li>

    <li>
      <h3>Model probability update (per model)</h3>
      <ol>
        <li>
          <strong>Likelihood</strong><br>
          \[
            L_{k}^{(i)} = \mathcal{N}\!\big(\tilde{z}_{k}^{(i)};\; 0,\; S_{k}^{(i)}\big)
          \]
        </li>
        <li>
          <strong>Bayesian update</strong><br>
          \[
            \mu_{k}^{(i)} =
            \frac{\mu_{k|k-1}^{(i)}\, L_{k}^{(i)}}{\sum_{j} \mu_{k|k-1}^{(j)}\, L_{k}^{(j)}}
          \]
        </li>
      </ol>
    </li>

    <li>
      <h3>Estimate fusion</h3>
      \[
        \hat{x}_{k|k} = \sum_{i} \hat{x}_{k|k}^{(i)} \,\mu_{k}^{(i)}
      \]
      \[
        P_{k|k} = \sum_{i}\Big(
          P_{k|k}^{(i)}
          + (\hat{x}_{k|k}-\hat{x}_{k|k}^{(i)})(\hat{x}_{k|k}-\hat{x}_{k|k}^{(i)})^\top
        \Big)\,\mu_{k}^{(i)}
      \]
    </li>
  </ol>

  <details>
    <summary><strong>Symbol notes</strong></summary>
    <ul>
      <li>\(\pi_{ji}\): probability of switching from model \(j\) to model \(i\)</li>
      <li>\(\mu_{k}^{(i)}\): probability model \(i\) is correct at time \(k\)</li>
      <li>\(\hat{x}, P\): state mean and covariance; bars \((\bar{\cdot})\) denote mixed (pre-prediction) quantities</li>
      <li>\(F^{(i)}, Q^{(i)}\): dynamics and process noise for model \(i\)</li>
      <li>\(H^{(i)}, R^{(i)}\): measurement model and noise for model \(i\)</li>
      <li>\(\tilde{z}\): measurement residual; \(S\): residual covariance; \(K\): Kalman gain</li>
    </ul>
  </details>
</section>
