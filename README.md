# Mean amplitude of PSD data

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes the mean power spectral density amplitude of each channel within a chosen frequency band and outputs a TSV of per-channel values and a histogram.**

Reads a PSD table (channels by frequencies), averages the PSD values of frequencies strictly between fmin and fmax for every channel, and plots the distribution across channels. Use it to summarize band power (e.g. alpha) of MEG/EEG data. It needs a PSD .tsv with a 'channels' column.

| | |
|---|---|
| 📥 **Inputs** | `neuro/meeg/psd` |
| 📤 **Outputs** | `neuro/meeg/psd` · `raw` |
| 🐳 **Container** | `brainlife/mne:0.23dev` |
| ⚙️ **Resources** | 1 CPUs |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.583](https://doi.org/10.25663/brainlife.app.583) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `psd01` | `neuro/meeg/psd` | yes | Power spectral density table (.tsv) with one row per channel and one column per frequency. Must have a 'channels' column; frequency column names must be numeric. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/psd` | psd.tsv with the mean band amplitude of each channel. |
| `out_figs` | `raw` | Histogram of mean band amplitude across channels. |

<details>
<summary><b>⚙️ Parameters</b> (2)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `fmin` | number | `8` | Fmin of frequency range for mean amplitude of PSD values |
| `fmax` | number | `12` | Fmax of frequency range for mean amplitude of PSD values |

</details>

📚 **References used by this App:**
- Hayashi S, Caron BA, et al. brainlife.io: A decentralized and open source cloud platform to support neuroscience research. arXiv (2023).

<!-- brainlife-app:end -->

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.583-blue.svg)](https://doi.org/10.25663/brainlife.app.583)

## Documentation
Compute the mean amplitude of a frequency range of PSD values

1) Detect mean amplitude for each channel
2) Input file is:
    * a `.tsv` file containing the Power Spectral Densities
5) Ouput files are:
    * a `.tsv` file containing the mean amplitude for each channel
    * a plot with the distribution of all peak amplitudes across channels
    * a plot the PSD peak for each channel (peak found in the psd)


## Authors
- [Guiomar Niso](guiomar.niso@ctb.upm.es), Instituto Cajal, CSIC, Spain

## Citations
We kindly ask that you cite the following articles when publishing papers and code using this app. 

1. **brainlife. io: A decentralized and open source cloud platform to support neuroscience research**. Hayashi, S., Caron, B. A., et al. & Pestilli, F. (2023). ArXiv. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10274934/

## Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project we kindly ask that you acknowledge the following funding sources:

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)


#### MIT Copyright (c) 2021 brainlife.io The University of Texas at Austin and Indiana University