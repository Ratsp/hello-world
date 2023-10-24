import streamlit as st
st.header("Tutorial 1 - st.write")
st.write("Hello World")
st.text("Unnakul Naane")

st.header("Tutorial 2 - st.button")
st.button("button 1")
st.write("______________________________________________")
if st.button("Learn"):
    st.write("Hello you are learning streamlit!!")
else:
    st.write("Goodbye")
st.write("______________________________________________")

if st.button("more"):
    st.write("Hello you are learning streamlit!!")
else:
    st.write("Goodbye")
st.button("Reset")


 