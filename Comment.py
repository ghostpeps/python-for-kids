import streamlit as st

st.title("Commemnts")
st.write("A comment can be written on any part of a python code, but don't put it in the middle of a piece of code. A comment starts with a # and looks like this:")
st.code(body="# This is a comment", line_numbers=True)
st.write("Output:")
st.code(body="", language=None)
st.write("A comment does not interfere with any of the code. Check this out:")
st.code(body="""
x = 53
#print("Hello")
print(x)
        """, line_numbers=True)
st.write("Output:")
st.code(body="53", language=None)
st.write("Comments can also be written on multiple lines using this: '''. Look at an example:")
st.code(body="""
'''
This
is
a
multiline
comment.
'''
        """, line_numbers=True)
st.write("Output:")
st.code(body="", language=None)
st.write("Comments can also be written on the same line as a piece of code:")
st.code(body="""
print("There is a comment next to me!!!") # There is a print statement next to me!!!
        """, line_numbers=True)
st.write("Output:")
st.code(body="There is a comment next to me!!!", language=None)
st.write("Please rate this site:")
comment_feedback = st.feedback(options="stars")
if comment_feedback is not None:
        st.write("Thank you!")
