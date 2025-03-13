import streamlit as st

url1 = "https://www.python.org/downloads/"
url2 = "https://www.jetbrains.com/pycharm/download/other.html"
st.title("Python for Kids")
st.write("Welcome to Python for Kids. This website is made for kids to easily learn python. From print() to zip(), this site has everything to turn you into a python-pro.")
st.write("If you want to start learning, and you have not yet downloaded Python then [click here](%s)" % url1 + ", or [click here](%s)" % url2 + " if you use macOS/Linux.")