import streamlit as st


st.title("Hello, My name is Gunavardhan Reddy, learning streamlit!")


st.header("Here we are learning how BUTTTONS work in streamlit.")

st.subheader("1. Normal Buttons.")
result = st.button(label = "Button.", help = "This is button where its default value is false and on click it turns boolean value true.")
res = str(result)
st.write("On Click, it becomes true: " + res)
if st.button(
label = "Click Me.",
help = "This button has its own content to display, other than true false."
):
	st.write("Hey there, I am button. :heart:")
else:
	st.write("you haven't clicked the button. :point_up:")
	
st.subheader("2.Download Buttons.")
st.download_button(
	label = "Download a csv file.",
	data = csv,
	file_name = 'IPL 2022.csv',
	mime = 'txt/csv',
	help = "Not only csv files you can create dowload buttons for directing to dowload images, binaryfiles, textfiles.",
)
	
