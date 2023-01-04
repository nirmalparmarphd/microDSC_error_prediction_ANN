# prediction of error/deviation in the heat capacity measurement
# use: prediction = dsc_error_model(Reference amount, Sample amount)
# NOTE: enter the sample and reference material amount as mentioned below
    ## Full cell:               1.0 
    ## Two Third full cell:     0.66
    ## One half full cell:      0.5
    ## One third full cell:     0.33


### MINIMUM WORKING EXAMPLE ###

# import module
from modul import *

# defining values
Reference_amount = 0.3
Sample_amount = 1

# prediction of deviation in heat capacity measurement
error_pred = dsc_error_model(Reference_amount,Sample_amount)

