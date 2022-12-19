### MINIMUM WORKING EXAMPLE ###

# import module
from modul import *

# prediction of error/deviation in the heat capacity measurement
# use: prediction = dsc_error_model(Reference amount(ml), Sample amount(ml))
# NOTE: enter the sample and reference material amount in [ml] 

# Example 1: Reference amount(ml) = 0.8, Sample amount(ml)= 0.8
# 0.8~ml [full], 0.4~ml [half full], 2.6~ml [one third full]
Reference_amount = 0.8
Sample_amount = 0.8

error_pred = dsc_error_model(Reference_amount,Sample_amount)

