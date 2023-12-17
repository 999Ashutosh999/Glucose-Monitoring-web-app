import pickle
import numpy as np
import streamlit as st


loaded_model = pickle.load(open('C:/Users/tripa/Desktop/machine learning/trained_model.sav','rb'))
def prediction_model(n):

    n = np.asarray(n)
    n = n.reshape(1, -1)

    p = loaded_model.predict(n)
    print(p)
# prediction_model((4, 110, 92, 0, 0, 37.6, 0.191, 30))

def main():
    st.title('Diabetes Prediction Web App')
    p_n = st.text_input('Number of Pregnancies')
    g_v = st.text_input('Glucose value')
    b_p = st.text_input('Blood Pressure')
    s_t = st.text_input('Skin_Thickness')
    ins = st.text_input('Insuline Value')
    bmi = st.text_input('BMI')
    d_p = st.text_input('Diabetes Pedigree Function')
    age = st.text_input('Age')

    dig = ''
    if st.button('Submit'):
        dig = prediction_model([p_n,g_v,b_p,s_t,ins,bmi,d_p,age])
        if dig:
            return st.warning('Person is Diabetic')
        else:
            return st.success('Person in not Diabetic')
if __name__=='__main__':
    main()
