# Time Domain Parameters (TDP)

## Description
TDP extracts temporal features of EEG signals using Hjorth parameters: **Activity**, **Mobility**, and **Complexity**.

## Formula

### **Activity**
Signal power:
$$
\text{Activity} = \text{var}(x(t))
$$

### **Mobility**
Mean frequency:
$$
\text{Mobility} = \sqrt{\frac{\text{Activity}\left(\frac{dx(t)}{dt}\right)}{\text{Activity}(x(t))}}
$$

### **Complexity**
Change in frequency:
$$
\text{Complexity} = \frac{\text{Mobility}\left(\frac{dx(t)}{dt}\right)}{\text{Mobility}(x(t))}
$$

## Applications
- Binary and multiclass motor imagery tasks.
- Effective for analyzing hand and wrist movements.

## Advantages
- Computationally efficient with low processing time.
- Achieves high classification accuracy when paired with Shrinkage-regularized Linear Discriminant Analysis (SRLDA).

## Limitations
- May require preprocessing for noise-prone signals.
- Slightly lower accuracy in highly complex tasks compared to CSP.

## References
1. Vidaurre, C., et al. (2009). Time domain parameters as a feature for EEG-based brain-computer interfaces. *Neural Networks*. [DOI:10.1016/j.neunet.2009.07.020](https://doi.org/10.1016/j.neunet.2009.07.020)