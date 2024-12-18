# Common Spatial Patterns (CSP)

## Description
CSP is a spatial-domain feature extraction method used for EEG signal analysis. It maximizes the variance of EEG signals for one class while minimizing the variance for the other.

## Formula
The optimization problem is defined as:

$$
\text{maximize} \quad \frac{w^T C_1 w}{w^T C_2 w}
$$

where:
- $C_1$ and $C_2$ are the covariance matrices for two classes.
- $w$ is the spatial filter.

The optimal $w$ is derived as the eigenvectors corresponding to the largest eigenvalues of $C_1^{-1} C_2$.

## Applications
- Binary motor imagery tasks, such as left- and right-hand movements.

## Advantages
- High performance for binary classification tasks.
- Well-suited for motor imagery-based brain-computer interfaces (MI-BCIs).

## Limitations
- Performance decreases for multiclass tasks without additional preprocessing.
- Computational cost increases with the number of channels.

## References
1. Ramoser, H., et al. (2000). Optimal spatial filtering of single trial EEG during imagined hand movement. *IEEE Transactions on Rehabilitation Engineering*. [DOI:10.1109/86.895946](https://doi.org/10.1109/86.895946)