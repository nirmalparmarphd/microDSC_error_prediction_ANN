import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model

print('-'*70)
information ='''
* This is a Deep learning (DL) ANN model to predict a deviation due to an inappropriate amount combination of the sample and a reference material in a batch cell of Tian-Calvet micro-DSC.

* Predict the possible deviation that may arise in the heat capacity measurement experiment with the sample and a reference material amount in [ml]!

-->ANN Model accuracy on the test data is 99.99 [%]<--'''

print(information)
print('-'*70)

class dsc_error_model():
  def __init__(self,Ref,Sam):
    stable_ml = 0.8 # ml to vol_fraction conversion 0.8-ml=1 
    self.Ref = Ref
    self.Sam = Sam
    model = load_model('micro_dsc_dl.h5')
    scaler = joblib.load('scaler.pkl')
    list = [2.  , 1.67, 3.33, 0.09, 0.6 , 0.72, 0.25, 0.42, 1.2 , 0.5 , 0.83,0.36, 0.15, 0.18, 1. , 0.3 ]
    self.vol_rel = np.round(((Ref*Ref)/Sam),2)
    
    for idx, item in enumerate(list):
      if item / self.vol_rel == 1:
          list[idx] = 1 
      else:
          list[idx] = 0 
          
    print(list)
    #self.list_ = self.list
    data = [self.Ref, self.Sam, self.vol_rel] + list
    print(data)
    data = pd.DataFrame([data])
    data_ = scaler.transform(data)
    pred = model.predict(data_)
    pred_ = np.round(((pred*100)-100).astype(np.float64),2)
 
    print('-'*70)
    print('Reference amount [ml]: ', Ref)
    print('Sample amount [ml]: ', Sam)

    if abs(pred_) <= 1.5:
      print('Heat capacity measurement deviation prediction (%): ')
      print(pred_)
     
    else:
      print('Heat capacity measurement deviation prediction (%): ')
      print(pred_)
      
    print('-'*70)
    
    
