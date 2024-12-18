# eeg_feature_extraction/__init__.py

from .csp import csp
from .tdp import tdp
from .psd import psd

__version__ = "0.1.0"

# Expose key functions for easier imports
__all__ = ['csp', 'tdp', 'psd']