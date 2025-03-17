import streamlit as st

import math

st.title("Printing with Backslashes")
st.write(r"Printing with backslashes allows you to print things that you normally shouldn't. For example, \\' prints as '. Look at an example:")
st.code(body=r"""
print("It\'s okay")
	""", line_numbers=True)
st.write("Output:")
st.code(body="It\'s okay", language=None)
st.write(r"\\\\ allows you to print \\:")
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
\\" allows you to write " without any error:
  """)
st.code(body=r"""
print("Look, \"Double Quotes\"")
  """, line_numbers=True)
st.write("Output:")
st.code(body=r"""
Look, "Double Quotes"
  """, language=None)
st.write(r"""\r gives a carriage return, similar to \n, a carriage return replaces the
characters at the beginning of the current line and adds the remaining part
to the end of the part after \r. Look at an example:""")
st.code(body=r"""
print("First part\rSecond")
	""", line_numbers=True)
st.write("Output:")
st.code(body=r"""
First part
Second
	""", language=None)
st.write(r"""
\t makes a tab or an indent wherever it is written:
""")
st.code(body=r"""
print("Incoming indent!!!\tThere is an indent behind me...")
	""", line_numbers=True)
st.write("Output:")
st.code(body=r"""Incoming indent!!!	There is an indent behind me...""", language=None)
st.write(r"""
\b backspaces the previous character:
	""")
st.code(body=r"""
print("Hello \bWorld!")
	""", line_numbers=True)
st.write("Output:")
st.code(body="HelloWorld!", language=None)
st.write(r"""
\ooo where o represents an octal number, \ooo is an octal value:
	""")
st.code(body=r"""
print("The following is an octal value: \110\145\154\154\157")
	""", line_numbers=True)
st.write("Output:")
st.code(body=r"""
The following is an octal value: Hello
	""", language=None)
st.write(r"""
\xhh where hh represents a hexadecimal, \xhh is a hex value:
	""")
st.code(body=r"""
print("The following is a hex value: \x48\x65\x6c\x6c\x6f")
	""", line_numbers=True)
st.write("Output:")
st.code(body=r"""
The following is a hex value: Hello
	""", language=None)
st.write(r"""
\ucccc, where c represents the code point, \ucccc is a Unicode:
	""")
st.code(body=r"""
print("\u0041")
print("\u03B1")
print("\u2603")
	""", line_numbers=True)
st.write("Output:")
st.code(body=r"""
A
α
☃
	""", language=None)
st.write(r"""\f is a Form Feed, Unicode: U+000C, with different outputs depending on the system.
Look at possible output #1 if you run Python on an Online Python Interpreter.
Look at all possible outputs if you run Python on systems or terminals. Here is an example:""")
st.code(body=r"""
print("This is the first part.\fThis is the second part.")
	""", line_numbers=True)
st.write("Possible Output #1:")
st.code(body=r"""
This is the first part.
This is the second part.
	""", language=None)
st.write("Possible Output #2:")
st.code(body=r"""

	""", language=None)
st.write("Possible Output #3:")
st.code(body=r"""
This is the first part.This is the second part.
	""", language=None)
st.write("Possible Output #4:")
st.code(body="""
This is the first part.␌This is the second part.
	""", language=None)
st.write(r"""
\v inserts a vertical indent. The outputs may vary, but it generally looks like this:
	""")
st.code(body=r"""
print("Hello\vWorld!")
	""", line_numbers=True)
st.write("Output:")
st.code(body=r"""
Hello
     World
	""", language=None)
st.write(r"""
\a or \7 is used to create a beep or visual alert. Some systems may ignore the \a or \7 entirely. Sometimes \a or \7 may also print an ASCII
value of the bell character:
	""")
st.code(body=r"""
print("Testing Bell sound\a")
	""", line_numbers=True)
st.write("Or:")
st.code(body=r"""
print("Testing Bell sound\7")
	""", line_numbers=True)
st.write("Output:")
st.code(body=r"""
Testing Bell sound␇
	""", language=None)
url1 = "https://www.ascii-code.com/"
st.write("A backslash followed by an ASCII octal escape sequence will result in an ASCII symbol. Go to [ASCII table](%s)" % url1 + " for a full list of ASCII codes. Look at an example:")
st.code(body=r"""
print("\41")
print("\207")
print("\275")
	""", line_numbers=True)
st.write("Output:")
st.code(body=r"""
!
‡
½
	""", language=None)
st.write("Please rate this site:")
print_feedback = st.feedback(options="stars")
total_stars = 0
rates = 0
if print_feedback is not None:
	rates = rates + 1
	total_stars = total_stars + print_feedback
	average = total_stars / print_feedback
	rounded_average = math.ceil(average)
	st.write("Thank You!")
