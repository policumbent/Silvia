#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 08:48:33 2022

@author: felixackermann
"""

import numpy as np 
import matplotlib.pylab as plt 
from scipy import fftpack as f
import scipy.signal as ssi
import scipy.io as sio
import pywt
import scipy.io.wavfile

import csv

"""with open('acc_data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    a_y = csv_reader[:,1] """
    
# Segnale test  
t = np.linspace(0,6*np.pi,300)
freq_camp = 100
durata = 3
a_y = np.sin(t)# + np.random.normal(0,1) 
a_y_r = a_y.reshape(durata,freq_camp)
plt.plot(t,a_y)
plt.show()

# Segnale accelorometro
N = np.size(a_y)
"""freq_camp = 1000
durata = np.round(N/freq_camp)
a_y_r = a_y.reshape(durata,freq_camp) # raggruppo le realizz in una fin temp """


# Determino matrice covarianza (anche indicata con gamma)
i = 0
Cov = np.zeros((durata,durata))
rho = np.zeros((durata,durata))
rho_ver = np.zeros((durata,durata))
while i<durata:
    for j in range(durata):
        Cov[i,j] = np.cov(a_y_r[i,:],a_y_r[j,:])[0][1] 
    i = i+1    

# Determino autocorrelazione    
i=0    
for i in range(durata):
    for j in range(durata):
        rho[i] = Cov[i,j]/np.sqrt(np.var(a_y_r[i,:])*np.var(a_y_r[j,:]))
        rho_ver[i]= Cov[0,i]/Cov[0,0] # verifica se processo è staz   
        

# Approssimazione nonlineare tramite base wavelet
cA, cD3, cD2, cD1 = pywt.wavedec(a_y, 'db4', level=3)

# soglia sotto la quale butto i coefficienti
m = np.mean(np.absolute(a_y))

# Assegno coefficienti non nulli
idx_d1 = np.where(np.absolute(cD1)>m)
cD1_c = np.zeros(cD1.shape)
cD1_c[idx_d1] = cD1[idx_d1]

idx_d2 = np.where(np.absolute(cD2)>m)
cD2_c = np.zeros(cD2.shape)
cD2_c[idx_d2] = cD2[idx_d2]

idx_d3 = np.where(np.absolute(cD3)>m)
cD3_c = np.zeros(cD3.shape)
cD3_c[idx_d3] = cD3[idx_d3]

a_y_rec = pywt.waverec((cA,cD3_c,cD2_c,cD1_c), 'db4')

error = np.sum((a_y-a_y_rec)**2)/a_y.shape[0]

print('Approximation error = ',error)

# FFT e spettro di potenza (freq. normalizzate)
a_y_dft = f.fft(a_y)
a_y_dft = a_y_dft[0:int(N/2)]

psd_a_y = 1/(N*np.pi)*np.power(np.abs(a_y_dft),2)
psd_a_y[1:int(N/2)+1] = 2*psd_a_y[1:int(N/2)+1]
# freq_2 = np.arange(0,np.pi,(2*np.pi)/N) # alternativ da 0-pi
freq_2 = np.arange(0,1,2/N)
plt.plot(freq_2,a_y_dft)
plt.title('Fourier transform')
plt.show()
plt.plot(freq_2,psd_a_y)
plt.title('Power spectral density (without denoising)')
plt.show()


