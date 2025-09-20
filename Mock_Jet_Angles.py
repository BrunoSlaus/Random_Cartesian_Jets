import numpy as np
import astropy
from astropy.io import fits



######################################################
N_grid = 100000
N_rand = 10000

X_Column_Name    = 'X'
Y_Column_Name    = 'Y'
Z_Column_Name    = 'Z'
RPA_Column_Name  = 'RPA'
######################################################

x_vals = np.linspace(0,1,N_grid)
y_vals = np.linspace(0,1,N_grid)
z_vals = np.linspace(0,1,N_grid)
x_rand = np.random.choice(x_vals, N_rand)
y_rand = np.random.choice(y_vals, N_rand)
z_rand = np.random.choice(z_vals, N_rand)



phi_vals = np.linspace(0, 180, N_grid)
phi_rand = np.random.choice(phi_vals, N_rand)


c1 = fits.Column(name = X_Column_Name,   array = x_rand,    format='f8')            #Adding a column
c2 = fits.Column(name = Y_Column_Name,   array = y_rand,    format='f8')            #Adding a column
c3 = fits.Column(name = Z_Column_Name,   array = z_rand,    format='f8')            #Adding a column
c4 = fits.Column(name = RPA_Column_Name, array = phi_rand,  format='f8')            #Adding a column
Output_Fits_2 = fits.BinTableHDU.from_columns([c1, c2, c3, c4])   #Creatng a fits file 
Output_Fits_2.writeto('Output/Mock_Kartesian.fits', overwrite = 'True') 











