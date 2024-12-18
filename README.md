# EEG Feature Extraction

This repository contains a Python package for extracting features from EEG data, specifically implementing Common Spatial Patterns (CSP), Time Domain Parameters (TDP), and Power Spectral Density (PSD). These methods are widely used in Brain-Computer Interfaces (BCI) for motor imagery tasks and have been tested for binary and multiclass discrimination tasks.

## Overview

Electroencephalogram (EEG) signals are a critical source of neurophysiological data in motor imagery-based brain-computer interfaces (MI-BCIs). Accurate discrimination of these signals is essential for controlling external devices, such as robotic arms, based on user intent. 

This package provides implementations of three conventional EEG feature extraction techniques:

1. **Common Spatial Patterns (CSP)**: Extracts spatial features that maximize variance for one class while minimizing it for another.
2. **Time Domain Parameters (TDP)**: Computes Hjorth parameters to describe the signal in terms of activity, mobility, and complexity.
3. **Power Spectral Density (PSD)**: Estimates the power spectral density of the signal using autoregressive modeling.

These methods have been evaluated for their performance in binary, ternary, and quaternary classification tasks involving complex motor imagery activities.

## Methods

### Common Spatial Patterns (CSP)
CSP extracts spatial features by solving an optimization problem to maximize the variance for one class while minimizing it for another. It is most effective for binary motor imagery tasks such as left- and right-hand movements.

### Time Domain Parameters (TDP)
TDP computes Hjorth parameters, which describe signal properties in the time domain:
- **Activity**: Signal power.
- **Mobility**: Mean frequency.
- **Complexity**: Changes in frequency.

### Power Spectral Density (PSD)
PSD estimates frequency-domain features using an autoregressive model. It is useful for capturing the power distribution of EEG signals across frequency bands.

## Package Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/EEG-Feature-Extraction.git
   cd EEG-Feature-Extraction
   ```

2. Install the package in editable mode:
   ```bash
   pip install -e .
   ```

3. Install additional dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The package provides modular functions for feature extraction. Here's an example of using all three methods:

```python
import numpy as np
from eeg_feature_extraction.csp import csp
from eeg_feature_extraction.tdp import tdp
from eeg_feature_extraction.psd import psd

# Simulated EEG data
X = np.random.randn(100, 64, 256)  # 100 samples, 64 channels, 256 time points
y = np.random.randint(0, 2, 100)   # Binary labels

# Apply CSP
W1, W2 = csp(X, y)
print("CSP filters computed.")

# Apply TDP
tdp_features = tdp(X)
print("TDP features computed.")

# Apply PSD
psd_features = psd(X)
print("PSD features computed.")
```

## Documentation

Detailed documentation for each method is available in the following files:
- [CSP Documentation](docs/csp.md)
- [TDP Documentation](docs/tdp.md)
- [PSD Documentation](docs/psd.md)

## References

1. Ramoser, H., et al., "Optimal spatial filtering of single trial EEG during imagined hand movement," IEEE Transactions on Rehabilitation Engineering, 2000.
2. Vidaurre, C., et al., "Time domain parameters as a feature for EEG-based brain-computer interfaces," Neural Networks, 2009.
3. Herman, P., et al., "Comparative analysis of spectral approaches to feature extraction for EEG-based motor imagery classification," IEEE Transactions on Neural Systems and Rehabilitation Engineering, 2008.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.