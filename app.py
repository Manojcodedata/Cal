import streamlit as st
from Cal import *

st.header('Calculator')
st.write("This is the app for calculator")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

operator = st.selectbox("Operator",['+','-','*','/','%'])

submit = st.button("Answer")

if submit:
    if operator=='+':
        ans = addition(a,b)
    elif operator=='-':
        ans = subtract(a,b)
    elif operator=='*':
        ans = multiply(a,b)
    elif operator=='/':
        ans = divide(a,b)
    elif operator=='%':
        ans = modulus(a,b)

    st.write(f"The answer is {ans}")

