import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import metrics

with open('r33.pkl', 'rb') as f:
    data = pickle.load(f)
    


model_sensasi = data[0]
model_kenyamanan = data[1]
model_penerimaan = data[2]

output_sensasi=model_sensasi.predict([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
output_kenyamanan=model_kenyamanan.predict([[1,1,1,1,1,1]])
output_penerimaan=model_penerimaan.predict([[1,1,1,1,1,1,1]])


