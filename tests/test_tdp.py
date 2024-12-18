import numpy as np
from eeg_feature_extraction.tdp import tdp

def test_tdp_features():
    # Simulated EEG data: 100 samples, 64 channels, 256 time points
    X = np.random.randn(100, 64, 256)
    
    # Call TDP function
    tdp_features = tdp(X)
    
    # Assert output dimensions
    assert tdp_features.shape[0] == 100, "TDP output has incorrect number of samples"
    assert tdp_features.shape[1] > 0, "TDP output has no features"