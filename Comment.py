import streamlit as st

st.title("Commemnts")
st.write("A comment can be written on any part of a python code, but don't put it in the middle of a piece of code. A comment starts with a # and looks like this:")
st.code(body="# This is a comment", line_numbers=True)