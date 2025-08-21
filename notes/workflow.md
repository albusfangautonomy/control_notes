---
layout: default
title: Control System Design Workflow
---

# Control System Specs → Design Actions Cheat Sheet

<table border="1" cellpadding="5" cellspacing="0">
<tr>
<th>Requirement / Spec</th>
<th>What It Means</th>
<th>Design Adjustments</th>
</tr>
<tr>
<td><b>Steady-State Error (Ess)</b></td>
<td>Final tracking error to step/ramp inputs</td>
<td>Increase <b>system type</b> (add integrator), adjust <b>Ki</b> in PID, or use <b>lag compensator</b></td>
</tr>
<tr>
<td><b>Rise Time (t<sub>r</sub>)</b></td>
<td>Speed to reach near-final value</td>
<td>Increase system bandwidth, add <b>lead compensator</b>, increase <b>Kp</b></td>
</tr>
<tr>
<td><b>Overshoot (M<sub>p</sub>)</b></td>
<td>How much output exceeds target</td>
<td>Increase <b>damping ratio</b> (reduce Kp, increase Kd), use <b>lead-lag</b> tuning</td>
</tr>
<tr>
<td><b>Settling Time (t<sub>s</sub>)</b></td>
<td>Time to stay within ±X% band</td>
<td>Increase natural frequency, increase damping via <b>derivative gain</b> or <b>lead compensation</b></td>
</tr>
<tr>
<td><b>Damping Ratio (ζ)</b></td>
<td>Oscillation level in transient</td>
<td>Adjust Kd or use lead to increase phase margin</td>
</tr>
<tr>
<td><b>Gain Margin (GM)</b></td>
<td>How much gain can increase before instability</td>
<td>Add phase lead, reduce open-loop gain</td>
</tr>
<tr>
<td><b>Phase Margin (PM)</b></td>
<td>Extra phase lag before instability</td>
<td>Add phase lead, adjust crossover frequency</td>
</tr>
<tr>
<td><b>Bandwidth</b></td>
<td>Frequency range of good tracking</td>
<td>Increase gain/lead for faster response, but watch noise</td>
</tr>
<tr>
<td><b>Disturbance Rejection</b></td>
<td>Suppress low/high frequency disturbances</td>
<td>Add <b>integrator</b> for low-freq rejection, notch filters for specific frequencies</td>
</tr>
<tr>
<td><b>Noise Sensitivity</b></td>
<td>Avoid amplifying sensor noise</td>
<td>Reduce bandwidth, use low-pass filter on derivative term</td>
</tr>
<tr>
<td><b>Control Effort Limit</b></td>
<td>Actuator magnitude/rate constraints</td>
<td>Add <b>rate limiter</b>, reduce aggressive gains, use anti-windup</td>
</tr>
</table>

---

## Quick Tuning Tips
- **Too slow?** → Increase Kp, add lead, raise bandwidth.  
- **Too oscillatory?** → Increase damping (Kd), reduce Kp, add lag.  
- **Steady-state error too high?** → Add integrator (Ki) or lag compensation.  
- **Noisy response?** → Lower bandwidth, filter derivative term.


---

## Quick Tuning Tips
- **Too slow?** → Increase Kp, add lead, raise bandwidth.  
- **Too oscillatory?** → Increase damping (Kd), reduce Kp, add lag.  
- **Steady-state error too high?** → Add integrator (Ki) or lag compensation.  
- **Noisy response?** → Lower bandwidth, filter derivative term.

---

# Control System Design Workflow
