# Power Spectral Density (PSD)

## Description
PSD is a spectral-domain feature extraction method that estimates the power distribution of a signal across frequencies.

## Formula
PSD is derived using the Yule-Walker method for autoregressive modeling:

$$
x_t = \sum_{i=1}^{p} \phi_i x_{t-i} + \zeta_t
$$

where:
- $p$: Model order.
- $\phi_i$: Model coefficients.
- $\zeta_t$: Noise term.

The PSD estimation uses:

$$
\gamma_m = \sum_{k=1}^{p} \phi_k \gamma_{m-k} + \sigma^2 \delta_m
$$

## Applications
- Motor imagery tasks (e.g., left- and right-hand movements).
- Frequency-domain analysis of EEG signals.

## Advantages
- Captures rich frequency-domain information.
- Useful for simple motor imagery tasks.

## Limitations
- Computationally expensive.
- Lower accuracy for multiclass tasks compared to TDP or CSP.

## References
1. Herman, P., et al. (2008). Comparative analysis of spectral approaches to feature extraction for EEG-based motor imagery classification. *IEEE Transactions on Neural Systems and Rehabilitation Engineering*. [DOI:10.1109/tnsre.2008.926694](https://doi.org/10.1109/tnsre.2008.926694)