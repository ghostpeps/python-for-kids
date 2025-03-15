import streamlit as st

import math

st.title("Printing with Backslashes")
st.write(r"Printing with backslashes allows you to print things that you normally shouldn't. For example, \' prints as '. Look at an example:")
'''
body = r"""
print("It\'s okay")
print("This is a single backslash: \\")
print("Hi\nNow I am on a new line")
print("Look, \"Double Quotes\"")
print("Hello\rHi")
print("\tMake sure to indent")
print("The following letter will dissapear: k\b")
print("The following is an octal value: \110\145\154\154\157")
print("The following is a hex value: \x48\x65\x6c\x6c\x6f")
  """
st.code(body=body, line_numbers=True)
st.write("Output")
st.code(body=r"""
It's okay
This is a single backslash: \
Hi
Now I am on a new line
Look, "Double Quotes"
Hello
Hi
	Make sure to indent
The following letter will disappear: 
The following is an octal value: Hello
The following is a hex value: Hello
  """, language=None)
  '''
st.code(body=r"It\'s okay", line_numbers=True)
st.write("Output:")
st.code(body="It\'s okay", language=None)
st.write(r"\\ allows you to print \:")
st.code(body=r"""
print("This is a single backslash: \\")
  """, line_numbers=True)
st.write("Output:")
st.code(body=r"""
This is a single backslash: \
  """, language=None)
st.write(r"\n prints a new line:")
st.code(body=r"""
print("Hi\nNow I am on a new line")
  """, line_numbers=True)
st.write("Output:")
st.code(body=r"""
Hi
Now I am on a new line
  """, language=None)
st.write(r"""
\" allows you to write " without any error:
  """)
st.code(body=r"""
print("Look, \"Double Quotes\"")
  """, line_numbers=True)
st.write("Output:")
st.code(body=r"""
Look, "Double Quotes"
  """, language=None)
st.write("Please rate this site:")
print_feedback = st.feedback(options="stars")
total_stars = 0
rates = 0
if print_feedback is not None:
	rates = rates + 1
	total_stars = total_stars + print_feedback
	average = total_stars / print_feedback
	math.ceil(average)
	st.write("Thank You!")
