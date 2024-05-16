# import Necessary Libraries
import pandas as pd
import numpy as np
import pickle as pkl
import streamlit as st

model = pkl.load(open('MIPML.pkl','rb'))

st.header('Medical Insurance Premium Predictor')

gender = st.selectbox('Choose Gender',['Female','Male'])
smoker = st.selectbox('Are you a smoker ?',['Yes','No'])
region = st.selectbox('Choose Region',['Southeast','Southwest','Northwest','Northeast'])
age = st.slider('Enter Age',5,80)
bmi = st.slider('Enter BMI',5,100)
chidren = st.slider('Children No Of Children',0,5)

if gender == 'Female':
    gender = 0
else:
    gender = 1

if smoker == 'Yes':
    smoker = 0
else:
    smoker = 1

if region == 'Southeast':
    region = 0
elif region == 'Southwest':
    region = 1
elif region == 'Northwest':
    region = 2
else:
    region = 3


inpu_data = (age,gender,bmi,chidren,smoker,region)
inpu_data = np.asarray(inpu_data)
inpu_data = inpu_data.reshape(1,-1)

if st.button('Predicrt'):

    predict_prem = model.predict(inpu_data)
    display_string = 'Insurance Premium will be :- ' + str(round(predict_prem[0],2)) + 'USD Dollars'
    st.markdown(display_string)