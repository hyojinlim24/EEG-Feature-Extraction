from setuptools import setup, find_packages

setup(
    name='eeg_feature_extraction',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
    ],
    description='Feature extraction methods for EEG data (CSP, TDP, PSD).',
    author='Hyojin Lim',
    author_email='hyojinl@uw.edu',
    url='https://github.com/hyojinlim24/EEG-Feature-Extraction',
)