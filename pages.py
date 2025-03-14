import streamlit as st

pages = {
    "Home": [
        st.Page(page="python-for-kids.py", title="Python for Kids", icon=":material/code:"),
    ],
    "Data Types": [
        st.Page(page="String.py", title="Strings", icon=":material/abc:"),
        st.Page(page="Integer.py", title="Integers", icon=":material/123:"),
        st.Page(page="Float.py", title="Floats", icon=":material/speed_0_5:"),
        st.Page(page="Complex.py", title="Complexes", icon=":material/function:"),
        st.Page(page="Boolean.py", title="Booleans", icon=":material/check:"),
        st.Page(page="List.py", title="Lists", icon=":material/data_array:"),
        st.Page(page="Set.py", title="Sets", icon=":material/data_object:"),
        st.Page(page="Tuple.py", title="Tuples"),
        st.Page(page="Range.py", title="Ranges", icon=":material/exposure_plus_1:"),
        st.Page(page="Frozenset.py", title="Frozensets", icon=":material/ac_unit:"),
        st.Page(page="Dictionary.py", title="Dictionaries", icon=":material/dictionary:"),
        st.Page(page="Byte.py", title="Bytes"),
        st.Page(page="Bytearray.py", title="Bytearraies"),
        st.Page(page="Memoryview.py", title="Memoryviews", icon=":material/network_intelligence:"),
        st.Page(page="Nonetype.py", title="NoneType (None)"),
    ],
    "Comments": [
        st.Page(page="Comment.py", title="Comments", icon=":material/tag:"),
    ],
    "Print": [
        st.Page(page="Print.py", title="Print", icon=":material/print:"),
    ]
}
pgs = st.navigation(pages)
pgs.run()
