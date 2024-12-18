import numpy as np
from eeg_feature_extraction.csp import csp

def test_csp_output_shapes():
    # Simulated EEG data: 100 samples, 64 channels, 256 time points
    X = np.random.randn(100, 64, 256)
    y = np.random.randint(0, 2, 100)  # Binary labels
    
    # Call CSP function
    W1, W2 = csp(X, y)
    
    # Assert correct shapes of output matrices
    assert W1.shape[1] == 64, "W1 output has incorrect shape"
    assert W2.shape[1] == 64, "W2 output has incorrect shape"