import numpy as np

Ref = 0.5
Sam = 0.3


list = [2.  , 1.67, 3.33, 0.09, 0.6 , 0.72, 0.25, 0.42, 1.2 , 0.5 , 0.83,0.36, 0.15, 0.18, 1. , 0.3 ]
vol_rel = np.round(((Ref*Ref)/Sam),2)
print(vol_rel)


for idx, item in enumerate(list):
    if item / vol_rel == 1:
        list[idx] = 1 
    else:
        list[idx] = 0 
   
print(list)
