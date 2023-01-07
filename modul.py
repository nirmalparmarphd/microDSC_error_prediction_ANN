import pandas as pd
import numpy as np
import sklearn.preprocessing
import pickle
import joblib
from tensorflow.keras.models import load_model

print('-'*70)
information ='''
* This is a Deep learning (DL) ANN model to predict a deviation due to an inappropriate amount combination of the sample and a reference material in a batch cell of Tian-Calvet micro-DSC.

* This ANN model predicts the possible deviation that may arise in the heat capacity measurement experiment due to in appropriate combination of the sample and the reference material amount!

-->ANN Model accuracy on the test data is 99.81 [%]<--'''

print(information)
print('-'*70)

class dsc_error_model():
  def __init__(self,Ref,Sam): 
    self.Ref = Ref
    self.Sam = Sam
    model = load_model('micro_dsc_dl.h5')
    with open('scaler.pkl' , 'rb') as f:
      scaler = pickle.load(f)
    vol_rel = (Ref*Ref)/Sam
    data = [self.Ref, self.Sam, vol_rel]
    data = pd.DataFrame([data])
    data_ = scaler.transform(data)
    pred = model.predict(data_)
    pred_ = np.round(((pred*100)-100).astype(np.float64),1)
    
    print('-'*70)
    print('Reference amount : ', Ref)
    print('Sample amount : ', Sam)
    
    if abs(pred_) <= 1:
      print('Heat capacity measurement deviation prediction (%): ', pred_)
      print('''COMMENT(s):
            The predicted deviation is below 1%!
            The combination of the sample and the reference amount is appropriate.
            NOTE:
            Consider 0.8~ml as standard amount to avoid any deviation in the measurement.''')
    else:
      print('Heat capacity measurement deviation prediction (%): ', pred_)
      print('''COMMENT(s): 
            The combination of the sample and the reference amount is NOT appropriate.
            NOTE:
            Consider 0.8~ml as standard amount to avoid any deviation in the measurement.
            ''')
    print('-'*70)
    
    
