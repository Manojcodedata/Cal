import streamlit as st
from Cal import *

st.header('Calculator')
st.write("This is the app for calculator")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

operator = st.selectbox("Operator",['+','-','*','/','%','power'])

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
    elif operator=='power':
        ans = power(a,b)
    elif operator=='floor_division':
        ans = floor_division(a,b)   
    elif operator=='square_root':       
        ans = square_root(a)

    st.write(f"The answer is {ans}")

