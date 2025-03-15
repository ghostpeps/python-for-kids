import streamlit as st

import math

st.title("Print")
st.write("A print statement is used to show text onto a screen. The text can be any Data Type and can be anything you want. A print statement looks like this:")
st.code(body="""
print("Hello World")
print(5)
print(5.3)
print("Hello", "Hi", "Hi again")
  """, line_numbers=True)
st.write("Output")
st.code(body="""
Hello World
5
5.3
Hello Hi Hi again
  """, language=None)
url1 = "https://ghostpeps208.streamlit.app/Variables"
st.write("You can also print [variables](%s)" % url1 + ":")
st.code(body="""
w = ("apples", "bannanas", "oranges")
x = 5
y = 4.6
z = "Hi again"
print(w)
print(x)
print(y)
print(z)
print(w, x, y, z)
  """, line_numbers=True)
st.write("Output")
st.code(body="""
('apples', 'bannanas', 'oranges')
5
4.6
Hi again
('apples', 'bannanas', 'oranges') 5 4.6 Hi again
  """, language=None)
st.write("You can also print variables using f-strings:")
st.code(body="""
x = 5
y = 4.6
z = "Hi again"
print(f"The variable x is {x}, the variable y is {y}, and the variable z is {z}.")
  """, line_numbers=True)
st.write("Output")
st.code(body="""
The variable x is 5, the variable y is 4.6, and the variable z is Hi again.
  """, language=None)
st.write("Or you can use the + :")
st.code(body="""
x = 5
y = 4.6
z = "Hi again"
print("The variable x is " + str(x) + ", the variable y is " + str(y) + ", and the variable z is " + z + ".")
  """, line_numbers=True)
st.write("Output")
st.code(body="""
The variable x is 5, the variable y is 4.6, and the variable z is Hi again.
  """, language=None)
st.write("You can also crate raw strings:")
st.code(body=r"""
print(r"This is a raw string\nSee")
  """, line_numbers=True)
st.write("Output")
st.code(body=r"""
This is a raw string\nSee
  """, language=None)
st.write("You can also use seperators:")
st.code(body="""
print("Hello", "How is you\'re day?", sep="--")
  """, line_numbers=True)
st.write("Output")
st.code(body="""
Hello--How is you're day?
  """, language=None)
st.write("You can also add different endings:")
st.code(body="""
print("Hi", end=" ")
print("Same line!!!")
  """, line_numbers=True)
st.write("Output")
st.code(body="""
Hi Same line!!!
  """, language=None)
st.write("Backslashes are also helpful in Python:")
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
st.code(body="""
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
