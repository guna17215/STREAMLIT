import streamlit as st

st.header("Hello, My name is Gunavardhan Reddy, learning streamlit!")

st.header("Here we are learning how BUTTTONS work in streamlit.")
if st.button("click me"):
	st.write("Hey there, I am button.")
	st.write(":heart:")
else:
	st.write("you haven't clicked the button.")