Development of Machine Learning Models for Precise Prediction of Bioactive Supramolecular Nucleoside Hydrogels
==============================

This code is the details of the manuscript "Development of Machine Learning Models for Precise Prediction of Bioactive Supramolecular Nucleoside Hydrogels".


## Table of Contents

- [Overview](#overview)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Deatails](#details)
- [Contributing](#contributing)
- [License](#license)
 
## Overview

Supramolecular hydrogels have demonstrated significant potential in drug delivery and tissue engineering. Among these, nucleoside hydrogels are particularly notable for their unique properties. Despite the broad potential applications of nucleoside hydrogels in the biomedical field, there is currently a lack of systematic approaches to guide their synthesis, thereby limiting their application potential. A major challenge in this field is that, apart from experimental validation, there are no established scientific methods to predict whether a nucleoside can form a hydrogel and determine its bioactivity. Our team has focused on utilizing machine learning (ML) to predict gelation capacity and has made substantial progress. Building on this, the present study aims to further predict the biological activity of nucleosides to guide the rational synthesis of bioactive hydrogels. Specifically, we first constructed predictive models and a database for nine biological activities using multiple ML methods based on feature selection, including decision trees, logistic regression, random forest, and extreme gradient boosting, to screen nucleoside derivatives with specific bioactivities. Then, the Molecular Bioactivity Specificity Index (MBSI) was created to evaluate the dominant bioactivity of nucleoside derivatives, and the Composite Molecular Attribute Score (CMAS) was developed to assess the overall performance of antibacterial nucleoside hydrogels. Subsequently, a systematic screening strategy for bioactive nucleoside hydrogels was established based on MBSI and CMAS, using antibacterial treatment for periodontitis as a sample to identify candidate hydrogels (n=4) with high hydrogel-forming ability, biocompatibility, and antibacterial activity. Finally, we experimentally validated two hydrogels (Guanosine - 5' - monophosphate, GMP; 2' - Deoxyguanosine 5' - phosphate, dGMP) for their efficacies in the antibacterial treatment of periodontitis. This study demonstrates the feasibility of utilizing the synthesis strategy based on ML models and MBSI/CMAS Methods to achieve the rational synthesis of functional bioactive nucleoside hydrogels, offering significant potential for applications across various biomedical fields.

 <img src="https://github.com/leescu/NBPND/blob/main/Figure/Figure.png" width = "900"  alt="Graph abstract" align=center />

## System Requirements
### Hardware requirements
Requires only a standard computer with enough RAM to support the in-memory operations.

### Software requirements
### OS Requirements
Supported for *windows* and *Linux*. The package has been tested on the following systems:
+ Windows: Win 10
+ Linux: Ubuntu 20.04
### Python Dependencies
Mainly depends on the Python 3.9.12 and  JupterLab Notebook 3.5.0-1 . The versions of packages are, specifically:

```
rdkit ≥ 2022.3.3
numpy ≥ 1.22.3
scipy ≥ 1.8.1
pandas ≥ 1.4.2
sklearn ≥ 1.1.1
joblib ≥ 1.1.0
seaborn ≥ 0.11.2
matplotlib ≥ 3.5.2
plotnine ≥ 0.10.1
optuna ≥ 3.0.5
xgboost ≥ 1.7.2
```
#### Notes
The calculation of molecular descriptors relies on the payware alvaDesc(https://www.alvascience.com/alvadesc/), and we provide the results of the descriptors in the corresponding file.


## Installation Guide

Installation via cloned repository:

```
$ git clone https://github.com/leescu/NBPND.git
$ cd NBPND
```
Make sure that the unpacked folders are inside “python/” folder in NBPND. Now you should be able to run the ipyn notebook or play with the python scripts!


## Contributing

See [the contributing file](CONTRIBUTING.md)!

### Contributions for manuscript

### Any optional sections

## License

[The Apache license 2.0](LICENCE.md)

