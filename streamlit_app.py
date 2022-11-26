import streamlit as st

st.title("Hello, My name is Gunavardhan Reddy, learning streamlit!")

st.header("Here we are learning how BUTTTONS work in streamlit.")
result = st.button("Button.")
res = str(result)
st.write(res)
if st.button("click me"):
	st.write("Hey there, I am button. :heart:")
else:
	st.write("you haven't clicked the button. :point_up:")
