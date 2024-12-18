import numpy as np
from eeg_feature_extraction.psd import psd

def test_psd_estimation():
    # Simulated EEG data: 100 samples, 64 channels, 256 time points
    X = np.random.randn(100, 64, 256)
    
    # Call PSD function
    psd_features = psd(X)
    
    # Assert PSD output dimensions
    assert psd_features.shape[0] == 100, "PSD output has incorrect number of samples"
    assert psd_features.shape[1] > 0, "PSD output has no features"