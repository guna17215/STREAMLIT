import streamlit as st

st.title("Hello, My name is Gunavardhan Reddy, learning streamlit!")

st.header("Here we are learning how BUTTTONS work in streamlit.")
st.subheader("1. Normal Buttons.")
result = st.button("Button.")
res = str(result)
st.write("On Click, it becomes true: " + res)
if st.button("click me"):
	st.write("Hey there, I am button. :heart:")
else:
	st.write("you haven't clicked the button. :point_up:")
st.subheader("2.Download Buttons.")
