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
    self.Ref = Ref/stable_ml 
    self.Sam = Sam/stable_ml
    model = load_model('micro_dsc_dl.h5')
    scaler = joblib.load('scaler.pkl')
    data = [self.Ref, self.Sam, self.Ref/self.Sam]
    data = pd.DataFrame([data])
    data_ = scaler.transform(data)
    pred = model.predict(data_)
    pred_ = np.round(((pred*100)-100).astype(np.float64),2)
    pred_df = pd.DataFrame(pred_)
    pred_df.columns=['Total-Deviation-(%)', 'Reference-Deviation-(%)']
    
    print('-'*70)
    print('Reference amount [ml]: ', Ref)
    print('Sample amount [ml]: ', Sam)

    if abs(pred_df.iloc[0,1]) <= 1.5:
      print('Heat capacity measurement deviation prediction (%): ')
      print(pred_df)
      print('''COMMENT(s): 
            Sample and reference amount combination is appropriate.
            Consider 0.8~ml as standard amount to avoid any deviation in the measurement.''')
    else:
      print('Heat capacity measurement deviation prediction (%): ')
      print(pred_df)
      print('''COMMENT(s): 
            Sample and reference amount maybe not appropriate.
            The reference material may too low!
            Re-run calibration with the fully filled reference material in a batch cell to avoid a large deviation.
            Consider 0.8~ml as standard amount to avoid any deviation in the measurement.
            ''')
    print('-'*70)
    
    
