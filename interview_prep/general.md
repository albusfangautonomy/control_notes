---
layout: default
title: General Interview Prep
---

## How does rate limiting and actuator saturation affect stability?
Both introduce nonlinear effects that can significantly influence a control system's stability and performance.

### Actuator Saturation
1. Loss of Phase Margin: we assume actuator perfectly tracks the commanded signal. Often increaes effective delay and reduce stability margins
2. Integral wind-up. The integral term keeps accumulating even though motors are saturated.
3. Limit Cycles.


How to resolve:
1. Integrator clamping for anti-windup.
2. Gain scheduling


### Rate Limiting
The actuator can only change its output at a limited rate (slew rate)

1. Effective delay: Rate limitting effectively adds delay to the system, introducing phase lag - slows down the system's ability to respond.
2. Reduced damping: In high-gain systems phase lag can push phase margin close to zero, making the system oscillatory.
3. Reduced bandwidth: cannot track higher frequency reference signals.

---

## You perceived overshoot in your system. What are the causes and what do you do?
There are several potential causes of overshoot:
1. **Low damping**: reducing $$K_p$$ and increasing $$K_d$$
2. **Integral Windup (Integral term too high)**: anti-windup 

---

## Effects of PID on Bandwidth

### Kp
Increasing the proportional gain generally increases the bandwidth because it amplifies the response to changes in the error signal, allowing the system to react more quickly to disturbances or reference changes.

**Limitations:**
Higher gain correspond to smaller phase margin. High Kp can cause the system to become oscillatory or unstable.




