---
layout: page
title: Reinforcement Learning Overview
---

## Rewards
A reward $$R_t$$ is a scalar feedback signal and indicates how well agent is doing at step $$t$$. The agent's goal is to maximize cumulative reward. 

### Sequential Decision Making
Note:
1. The goal is to **select actions to maximize total future reward**. 
2. Reward may be delayed.
3. It may be more advantageous to sacrifice immediate reward to gain more long term reward

## Agent and Environment
At time $$t$$

Inputs:

1. Observation $$O_t$$.
2. Reward $$R_t$$.

Outputs:

3. Action $$A_t$$.

### Environment State
The environment state $$S_t^e$$ is the environments private representation
    - ie. whatever data the environment uses to pick the next observation/reward.
    - The environment state is not usually visible to the agent.
    - Even if $$S_t^e$$  is visible, it may contain irrelevant info.

### Agent State
The agent state $$S_t^a$$ is the agent's internal representation
    - ie. whatever info the agent uses to pick the next action
    - It is the info used by reinforcement learning algorithms
    - It can be any function of history: $$S_t^a = f(H_t)$$

## Information State (Markov State)
A state $$S_t$$ is Markov if and only if 

$$
\mathbb{P} [S_{t+1} | S_t] = \mathbb{P} [S_{t+1} | S_1, ..., S_t]
$$


In plain English, the probability of the next state only depends on the current state. Once the state is known the history may be thrown away.
**A Markov state encodes enough information to characterize all future reward.**

The environment state $$ S_t^{e} $$.

## Fully Observable Environments (MDP)

Full observability: agent directly observes environment state: $$ O_t = S_t^a = S_t^e$$.

1. Agent state = Environment state = Information State.
2. This is a Markov decision process (MDP).

## Partially Observable Environments (POMDP)
Partial Observability: Agent indirectly observes environment

In this case $$S_t^a \neq S_t^e$$


## Major Compoents of an RL Agent
1. Policy: agent's behavior
2. Value function: reward $$R_t$$
3. Model: agent's representation of the environment

### Policy:
Policy is a map from state to action.

1. Deterministic Policy
    - $$a = \pi(s)$$
2. Stochastic Policy
    - $$\pi(a|s) = \mathbb{P}[A=a|S=s]$$

## Value Function
Value predicts future reward. How much total reward we expect to get *in the future*.

$$
v_\pi(s) = \mathbb{E}_\pi[R_t + \gamma R_{t+1} + \gamma^2 R_{t+2} + ... | S_t = S]
$$
