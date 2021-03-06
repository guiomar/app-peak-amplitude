# Copyright (c) 2020 brainlife.io
#
# Author: Guiomar Niso
# Indiana University

# set up environment
import os
import json
import mne
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)
    

# == GET CONFIG VALUES ==
fname = config['psd']
fmin  = config['fmin']
fmax  = config['fmax']

# == LOAD DATA ==
df_psd = pd.read_csv(fname, sep = '\t')
canales = df_psd['channels'].copy()

#Number of frequencies computed for the PSD
nfreqs = df_psd.shape[1]
df = df_psd.iloc[:, 1:nfreqs].copy() # To avoid the case where changing df also changes df_psd
#List of frequencies
freqs = df.columns.to_numpy()
freqs = freqs.astype(float)
#PSD values
psd_welch = df.to_numpy()
#Number of channels
nchannels = psd_welch.shape[0]


# Extract the frequencies that fall inside the alpha band
ifreqs = [i for i, f in zip(range(0, len(freqs)), freqs) if f > fmin  and f < fmax]
band_freqs = np.take(freqs, ifreqs)


# ==== FIND ALPHA MEAN AMPLITUDE VALUE ====
channel_peak = np.mean(psd_welch[:,ifreqs], axis=1)


# Average value across all channels
mean_peak=np.mean(channel_peak, axis=0)


# == SAVE FILE ==
# Save to TSV file
df_alpha = pd.DataFrame(channel_peak, index=canales, columns=['peak'])
df_alpha.to_csv(os.path.join('out_dir','psd.tsv'), sep ='\t')


# ==== PLOT FIGURES ====

# FIGURE 1
plt.figure(1)
#custom_params = {"axes.spines.right": False, "axes.spines.top": False}
#sns.set_theme(style="ticks", rc=custom_params)
sns.set_theme(style="ticks")
sns.histplot(data=channel_peak, binwidth=0.25,kde=True,kde_kws={'cut':10})
#plt.xlim(xmin=fmin, xmax=fmax)
plt.xlabel('Peak amplitude')
sns.despine()
# Save fig
plt.savefig(os.path.join('out_figs','hist_peak_amplitude.png'))
plt.close()
