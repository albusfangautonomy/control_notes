---
layout: default
title: SVD
---

SVD works on any matrix

# Intuitive Interpretations
## Rotation, coordinate scaling, and reflection
## 🎯 SVD Geometry Summary

For a real matrix **M**, the Singular Value Decomposition is:

$$
\mathbf{M} = \mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^*
$$

### 🔷 Square Matrix Case: $$ \mathbf{M} \in \mathbb{R}^{m \times m} $$

- **U** and **V\*** are real orthogonal matrices (rotations/reflections)
- **Σ** scales each coordinate by singular values $\sigma_i$
- Geometrically:
  `rotation/reflection → scaling → rotation/reflection`

#### 🔸 Determinant Interpretation

- $\det(\mathbf{M}) > 0$: U and V^* are both **rotations** or both **reflections**
- $ \det(\mathbf{M}) < 0 $: One of U or V^* must involve **reflection**
- $ \det(\mathbf{M}) = 0 $: U and V^* can independently be rotations or reflections

### 🔷 Rectangular Matrix Case: $\mathbf{M} \in \mathbb{R}^{m \times n}$

- M maps $$\mathbb{R}^n \to \mathbb{R}^m $$
- U and V\* act on $\mathbb{R}^m$ and $\mathbb{R}^n$ respectively
- Σ:
  - Scales the first $\min(m, n)$ coordinates
  - Extends (pads) or truncates vector dimensions appropriately

This decomposition reveals how any linear transformation can be interpreted geometrically using **rotations/reflections and scaling**.
