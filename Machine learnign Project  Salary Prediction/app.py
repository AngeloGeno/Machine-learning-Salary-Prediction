import streamlit as st
import numpy as np
import joblib


st.title("Salary Prediction App")

st.divider()
st.write("This app predicts the salary of a an employee based on the Year and the Job Rate")
years =st.number_input(value=1, step=1, min_value=0)
jobrate = st.number_input(value=3.5, step=0.5, min_value=0.0)

X=[years,jobrate]

st.divider()

predict = st.button("press the button for salary prediction")

st.divider()
model =joblib.load("linearmodel.pkl")


if predict:
    st.baloons()

    X1=np.array(X)
    prediction =model.predict(X1)
    st.write(f"The predicted salary is {prediction}")
else:"Press the button to get the salary prediction"