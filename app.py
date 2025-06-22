import streamlit as st
import pickle
import numpy as np

# import model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor")

# brand
brand = st.selectbox('Brand',df['Company'].unique())

# type
type = st.selectbox('Type',df['TypeName'].unique())

# ram
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

# weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touch = st.selectbox('TouchScreen',['No','Yes'])

# ips
ips = st.selectbox('IPS',['No','Yes'])

# screen size
size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160',
                                               '3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

# cpu
cpu = st.selectbox('CPU brand',df['cpu brand'].unique())

# hdd
hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

# sdd
sdd = st.selectbox('SDD(in GB)',[0,8,128,256,512,1024])

# gpu brand
gpu = st.selectbox('GPU brand',df['gpu brand'].unique())

# os
os = st.selectbox('OS brand',df['os brand'].unique())

if st.button('Predict Price:'):
    # query
    ppi=None
    if touch=='Yes':
        touch=1
    else:
        touch=0

    if ips=='Yes':
        ips=1
    else:
        ips=0

    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi = (((x_res**2)+(y_res**2))**0.5)/size
    query = np.array([brand,type,ram,weight,touch,ips,size,resolution,cpu,hdd,sdd,gpu,os])

    query = query.reshape(1,12)
    st.title("The predicted price of the Laptop is ₹"+str(int(np.exp(pipe.predict(query)[0]))))



















